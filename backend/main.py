from functools import lru_cache
import os
import shutil
import tempfile

from fastapi import FastAPI, File, HTTPException, Query, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from nudenet import NudeDetector

app = FastAPI(title="Gentleman Mosaic NSFW API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL_RESOLUTION = {
    "320n": 320,
    "640m": 640,
}


@lru_cache(maxsize=2)
def get_detector(model: str) -> NudeDetector:
    resolution = MODEL_RESOLUTION[model]
    return NudeDetector(inference_resolution=resolution)


@app.get("/health")
def health():
    return {"ok": True, "models": list(MODEL_RESOLUTION.keys())}


@app.post("/detect-nsfw")
async def detect_nsfw(
    file: UploadFile = File(...),
    threshold: float = Query(0.45, ge=0.01, le=0.99),
    model: str = Query("320n"),
):
    if model not in MODEL_RESOLUTION:
        raise HTTPException(status_code=400, detail="Unsupported model. Use 320n or 640m.")

    suffix = os.path.splitext(file.filename or "image.png")[1] or ".png"
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        shutil.copyfileobj(file.file, tmp)
        tmp_path = tmp.name

    try:
        detector = get_detector(model)
        preds = detector.detect(tmp_path) or []
        out = []
        for p in preds:
            score = float(p.get("score", 0))
            if score < threshold:
                continue

            box = p.get("box") or [0, 0, 0, 0]
            if len(box) != 4:
                continue

            x, y, w, h = box
            out.append(
                {
                    "class": p.get("class", "unknown"),
                    "score": score,
                    "box": [int(x), int(y), int(w), int(h)],
                    "model": model,
                }
            )

        return {"detections": out, "model": model}
    finally:
        try:
            os.remove(tmp_path)
        except OSError:
            pass
