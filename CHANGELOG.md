# Change Log

## [2.0.0] - 2026-03-31

### Added
- Batch image upload workflow (up to 30 files) with thumbnail list, quick switching, and per-image state isolation.
- Thumbnail context menu (right-click): delete image and download processed image.
- Thumbnail selection shortcuts:
  - Left click to select
  - `Ctrl + Click` multi-select
  - `Shift + Click` range-select
  - `Ctrl + A` select all
- NSFW auto-detection integration (NudeNet backend endpoint), including:
  - Adjustable threshold in UI
  - Model switch support (`320n`, `640m`)
- Nori redaction effect with configurable:
  - Color
  - Opacity
  - Stripe width
  - Stripe gap
  - Direction (horizontal / vertical)
- Brush shape options for manual masking:
  - Circle
  - Square
- Multi-language docs split:
  - `README.md` (default Chinese entry)
  - `README.zh.md`
  - `README.en.md`

### Changed
- UI top layout refactor: first-row status block and upload/menu block aligned into the same row.
- README structure updated to a language-switch entry model, with Chinese as default.
- Project version metadata updated to `v2.0.0` across UI and package manifest.

### Fixed
- Fixed intermittent canvas rendering bug where images could appear overlapped after switching between batch items.
- Fixed unexpected canvas cropping by synchronizing canvas dimensions with restored image state.
- Added async image-load race guard to prevent late image responses from overriding the current view.

## [1.0.0] - 2026-03-31

### Added
- Initial standalone image redaction tool UI.
- Core redaction workflows:
  - Rectangle selection
  - Brush selection
  - Mosaic effect
  - Basic export
- Undo/redo and history panel baseline.
- Light/dark theme support and Chinese/English UI switching.

### Changed

### Fixed
