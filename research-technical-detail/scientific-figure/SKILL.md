---
name: scientific-figure
description: Unified publication-figure skill for Python/matplotlib. Covers grouped/ablation bars, trend lines, heatmaps, and conceptual diagrams with one consistent visual style and reproducible export rules.
---

# Scientific Figure

Use this single skill for all common paper figure tasks in this repository.

## Coverage

- Bar charts:
  - grouped comparison
  - ablation and method variants
- Trend plots:
  - training/evaluation curves
  - cumulative time-series trends
- Heatmaps:
  - correlation and matrix comparisons
- Concept diagrams:
  - scatter plus arrows/callouts
  - geometry/sphere illustrations

## Foundation

This skill is powered by:

- `scientific-figure/scripts/scientific_figure_pro.py`

Core APIs:

- `apply_publication_style(...)`
- `create_subplots(...)`
- `make_grouped_bar(...)`
- `make_trend(...)`
- `make_heatmap(...)`
- `make_scatter(...)`
- `make_sphere_illustration(...)`
- `finalize_figure(...)`

## Workflow

1. Import helper module from `scientific-figure/scripts/scientific_figure_pro.py`.
2. Apply style at script start:
   - Dense bar panels: `FigureStyle(font_size=22 to 24, axes_linewidth=3)`
   - Standard figures: `FigureStyle(font_size=14 to 18, axes_linewidth=2 to 2.5)`
3. Build plot(s) with relevant `make_*` helpers.
4. Keep axis ranges explicit and legends frameless.
5. Export via `finalize_figure(..., formats=["png", "pdf"])`.

## Starter Scripts

- `scripts/bar_figure_starter.py`
- `scripts/trend_heatmap_starter.py`
- `scripts/concept_diagram_starter.py`

## Quick Run

```bash
python research-technical-detail/scientific-figure/scripts/bar_figure_starter.py
python research-technical-detail/scientific-figure/scripts/trend_heatmap_starter.py
python research-technical-detail/scientific-figure/scripts/concept_diagram_starter.py
```
