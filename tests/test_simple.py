import numpy as np
from lrlab.data import load_toy
from lrlab.simple import fit_simple, add_bias

def test_matches_polyfit():
    x, y = load_toy()
    assert np.allclose(fit_simple(x, y), np.polyfit(x, y, 1))

def test_add_bias_shape_and_ones():
    Xb = add_bias(np.zeros((5, 3)))
    assert Xb.shape == (5, 4) and (Xb[:, 0] == 1).all()
