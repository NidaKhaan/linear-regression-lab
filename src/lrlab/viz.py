"""Shared plotting theme so every figure looks consistent."""
import os
import matplotlib.pyplot as plt
from lrlab.config import FIG_DIR

PALETTE = {"primary": "#4C78FF", "accent": "#FF5A5F", "good": "#2EC4B6",
           "warn": "#FFB703", "ink": "#1B1F3B", "grid": "#E6E8F0"}

def set_theme():
    plt.rcParams.update({
        "figure.dpi": 110, "axes.facecolor": "white", "axes.edgecolor": PALETTE["ink"],
        "axes.grid": True, "grid.color": PALETTE["grid"], "grid.linewidth": 0.8,
        "axes.spines.top": False, "axes.spines.right": False,
        "axes.titleweight": "bold", "axes.titlesize": 12, "font.size": 11,
        "legend.frameon": False,
    })

def save(fig, name):
    os.makedirs(FIG_DIR, exist_ok=True)
    path = f"{FIG_DIR}/{name}.png"
    fig.savefig(path, dpi=200, bbox_inches="tight")
    return path
