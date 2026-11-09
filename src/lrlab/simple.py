"""Simple linear regression (closed form) and design-matrix helper."""
import numpy as np

def fit_simple(x, y):
    """Least squares for y = a*x + b.  a = cov(x,y)/var(x),  b = y_mean - a*x_mean."""
    x, y = np.asarray(x, float), np.asarray(y, float)
    x_bar, y_bar = x.mean(), y.mean()
    a = ((x - x_bar) * (y - y_bar)).sum() / ((x - x_bar) ** 2).sum()
    b = y_bar - a * x_bar
    return a, b

def add_bias(X):
    """Prepend a column of ones so that h(X) = X @ theta (slide 9: X0 = 1)."""
    X = np.asarray(X, float)
    return np.c_[np.ones(len(X)), X]
