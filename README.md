[English Documentation](./README.en.md)

# 紳士打碼 v2.0.0

![紳士打碼 Logo](./logo-Photoroom.png)

## 介面預覽
![UI Demo](./UI.PNG)

## 更新資訊
- 版本：`v2.0.0`
- 更新日期：`2026-03-31`

### v2.0.0 新功能重點
- 批次上傳與圖片切換（最多 30 張）
- 每張圖片各自保存：待處理區域、歷史回溯（Undo/Redo）
- 縮圖右鍵選單：刪除圖片、下載該圖處理後結果
- 縮圖快捷選取：左鍵選擇、`Ctrl + 左鍵` 多選、`Shift + 左鍵` 區間選取、`Ctrl + A` 全選
- 支援 NSFW 自動偵測（NudeNet）：可調偵測閾值、模型 `320n` / `640m`
- 打碼方式：馬賽克、海苔（顏色、透明度、寬度、間隔、方向可調）
- 選取模式：框選、塗抹（圓形/方形筆刷）
- 支援深色模式與中英文介面切換

## 系統需求
- Windows（含 `.bat` 啟動流程）
- Python 3.9+（建議 3.10+）
- 可連網下載 Python 套件（第一次啟動時）

## 安裝與啟動（建議）

### 一鍵啟動（Standalone）
1. 進入專案根目錄。
2. 確認有下列檔案：`start_app.bat`、`launch.ini`、`standalone.html`。
3. 直接雙擊 `start_app.bat`。
4. 腳本會自動讀取設定、建立 `.venv`、安裝依賴、啟動後端，並開啟 `standalone.html`。

### `launch.ini` 主要設定
```ini
[backend]
enabled=1
use_venv=1
venv_dir=.venv
create_venv=1
python_cmd=python
host=127.0.0.1
port=7300
reload=0
auto_install_deps=1
```

說明：
- `port` 會同步寫入 `runtime-config.js`，前端會使用該埠連線後端。
- 想關閉後端可設 `enabled=0`（僅做手動打碼編輯）。

## 開發模式（React/Vite）
```bash
npm install
npm run dev
```

### 打包
```bash
npm run build
npm run preview
```

## 使用流程
1. 批次上傳圖片或拖曳圖片到畫布區。
2. 在上方縮圖列選擇要編輯的圖片。
3. 選擇打碼效果（馬賽克 / 海苔）。
4. 用框選或塗抹建立待處理區域。
5. 按「確定套用」完成本次打碼。
6. 需要時可用 Undo / Redo 回溯。
7. 右鍵縮圖可刪除或下載處理後圖片。

## 注意事項
- 第一次啟動會下載 Python 套件，時間較久屬正常。
- 若 Python 指令不是 `python`，可在 `launch.ini` 調整 `python_cmd`。
- 批次上限為 30 張，超過會提示並忽略多餘檔案。

