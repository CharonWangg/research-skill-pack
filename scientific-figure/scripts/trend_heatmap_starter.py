"""Starter template for trend + heatmap publication figures."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import sys

import numpy as np


def _load_style_module():
    """Load shared style helpers to keep visual consistency."""
    module_path = Path(__file__).resolve().parent / "scientific_figure_pro.py"
    spec = importlib.util.spec_from_file_location("scientific_figure_pro", module_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load helper module at {module_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def plot_trend_heatmap_panel(out_stem: Path) -> None:
    mod = _load_style_module()
    mod.apply_publication_style(mod.FigureStyle(font_size=14, axes_linewidth=2.2))

    fig, axes = mod.create_subplots(1, 2, figsize=(14, 5), constrained_layout=True)

    epochs = np.arange(1, 101)
    curve_a = 0.50 + 0.38 * (1 - np.exp(-epochs / 35.0))
    curve_b = 0.48 + 0.33 * (1 - np.exp(-epochs / 40.0))
    curve_c = 0.46 + 0.29 * (1 - np.exp(-epochs / 45.0))
    mod.make_trend(
        axes[0],
        x=epochs,
        y_series=[curve_a, curve_b, curve_c],
        labels=["Model A", "Model B", "Model C"],
        colors=[mod.PALETTE["blue_main"], mod.PALETTE["teal"], mod.PALETTE["red_strong"]],
        xlabel="Epoch",
        ylabel="Validation Accuracy",
        show_shadow=True,
    )
    axes[0].set_ylim(0.45, 0.92)
    axes[0].set_title("A. Accuracy Trend", loc="left", fontweight="bold")
    axes[0].grid(alpha=0.2, linestyle="--")

    rng = np.random.default_rng(7)
    raw = rng.normal(size=(700, 8))
    corr = np.corrcoef(raw, rowvar=False)
    labels = [f"F{i}" for i in range(1, 9)]
    mod.make_heatmap(
        axes[1],
        matrix=corr,
        x_labels=labels,
        y_labels=labels,
        cmap="magma",
        cbar_label="Correlation",
        annotate=False,
    )
    axes[1].set_title("B. Feature Correlation", loc="left", fontweight="bold")

    mod.finalize_figure(fig, out_stem, formats=["png", "pdf"], dpi=350, pad=0.06)


def main() -> None:
    out_dir = Path(__file__).resolve().parent / "output"
    out_dir.mkdir(parents=True, exist_ok=True)
    plot_trend_heatmap_panel(out_dir / "trend_heatmap_starter")


if __name__ == "__main__":
    main()
