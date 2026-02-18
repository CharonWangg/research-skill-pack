"""Starter template for publication-style grouped bar figures."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import sys

import matplotlib.pyplot as plt


def _load_style_module():
    """Dynamically load shared plotting helpers from the base helper module."""
    module_path = Path(__file__).resolve().parent / "scientific_figure_pro.py"
    spec = importlib.util.spec_from_file_location("scientific_figure_pro", module_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load helper module at {module_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def plot_bar_comparison(out_stem: Path) -> None:
    mod = _load_style_module()
    mod.apply_publication_style(mod.FigureStyle(font_size=16, axes_linewidth=2.5))

    categories = ["AUC", "F1", "Recall", "Precision"]
    series = [
        [0.79, 0.74, 0.71, 0.77],
        [0.82, 0.76, 0.75, 0.79],
        [0.86, 0.81, 0.80, 0.84],
    ]
    labels = ["Baseline", "Ablation+", "Proposed"]
    colors = [mod.PALETTE["neutral"], mod.PALETTE["green_2"], mod.PALETTE["blue_main"]]

    fig, ax = plt.subplots(figsize=(10, 5.5))
    mod.make_grouped_bar(
        ax=ax,
        categories=categories,
        series=series,
        labels=labels,
        ylabel="Score",
        colors=colors,
        annotate=True,
    )
    ax.set_ylim(0.65, 0.92)
    ax.set_title("Model Comparison Across Metrics", loc="left", fontweight="bold")
    ax.grid(alpha=0.2, linestyle="--", axis="y")

    mod.finalize_figure(fig, out_stem, formats=["png", "pdf"], dpi=350, pad=0.06)


def main() -> None:
    out_dir = Path(__file__).resolve().parent / "output"
    out_dir.mkdir(parents=True, exist_ok=True)
    plot_bar_comparison(out_dir / "bar_figure_starter")


if __name__ == "__main__":
    main()
