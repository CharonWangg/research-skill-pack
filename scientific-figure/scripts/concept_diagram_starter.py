"""Starter template for conceptual figure panels."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import sys

import numpy as np


def _load_style_module():
    """Load shared plotting helpers used by this unified skill."""
    module_path = Path(__file__).resolve().parent / "scientific_figure_pro.py"
    spec = importlib.util.spec_from_file_location("scientific_figure_pro", module_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load helper module at {module_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def plot_concept_diagram(out_stem: Path) -> None:
    mod = _load_style_module()
    mod.apply_publication_style(mod.FigureStyle(font_size=14, axes_linewidth=2.2))

    fig, axes = mod.create_subplots(1, 2, figsize=(13, 5), constrained_layout=True)

    rng = np.random.default_rng(5)
    cluster_a = rng.normal(loc=(-1.0, 0.8), scale=(0.22, 0.25), size=(70, 2))
    cluster_b = rng.normal(loc=(1.0, -0.6), scale=(0.25, 0.23), size=(70, 2))

    mod.make_scatter(
        axes[0],
        x=cluster_a[:, 0],
        y=cluster_a[:, 1],
        label="Before Alignment",
        color=mod.PALETTE["red_2"],
        size=42,
        alpha=0.75,
    )
    mod.make_scatter(
        axes[0],
        x=cluster_b[:, 0],
        y=cluster_b[:, 1],
        label="After Alignment",
        color=mod.PALETTE["blue_main"],
        size=42,
        alpha=0.78,
    )
    axes[0].annotate(
        "Representation shift",
        xy=(0.5, -0.2),
        xytext=(-0.2, 0.5),
        arrowprops={"arrowstyle": "->", "lw": 2.2, "color": mod.PALETTE["red_strong"]},
        fontsize=13,
    )
    axes[0].set_xlabel("Latent dimension 1")
    axes[0].set_ylabel("Latent dimension 2")
    axes[0].set_title("A. Alignment Dynamics", loc="left", fontweight="bold")
    axes[0].grid(alpha=0.2, linestyle="--")

    mod.make_sphere_illustration(
        axes[1],
        light_dir=(-0.55, 0.60, 0.55),
        resolution=320,
        alpha=0.95,
    )
    axes[1].text(
        0.0,
        -1.25,
        "Hyperspherical regularization",
        ha="center",
        va="center",
        fontsize=13,
        color=mod.PALETTE["blue_main"],
    )
    axes[1].set_title("B. Geometric Prior", loc="left", fontweight="bold")

    mod.finalize_figure(fig, out_stem, formats=["png", "pdf"], dpi=350, pad=0.06)


def main() -> None:
    out_dir = Path(__file__).resolve().parent / "output"
    out_dir.mkdir(parents=True, exist_ok=True)
    plot_concept_diagram(out_dir / "concept_diagram_starter")


if __name__ == "__main__":
    main()
