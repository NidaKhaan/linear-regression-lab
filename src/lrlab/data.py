"""Dataset loading and splitting."""
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from lrlab.config import SEED

TARGET = "MedHouseVal"

def load_toy():
    """The 6 points from the slide-5 figure."""
    x = np.array([10, 15, 20, 30, 50, 60], dtype=float)
    y = np.array([0.8, 1.0, 1.8, 2.0, 3.5, 3.0])
    return x, y

def load_california():
    """California Housing as a DataFrame (features + MedHouseVal)."""
    return fetch_california_housing(as_frame=True, data_home="data/raw").frame

def split(X, y, test_size=0.2):
    """Reproducible train/test split. Always split BEFORE any fitting."""
    return train_test_split(X, y, test_size=test_size, random_state=SEED)
