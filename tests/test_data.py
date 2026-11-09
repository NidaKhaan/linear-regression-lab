from lrlab.data import load_toy, split

def test_toy_shapes():
    x, y = load_toy()
    assert x.shape == y.shape == (6,)

def test_split_sizes_and_reproducibility():
    x, y = load_toy()
    X = x.reshape(-1, 1)
    a = split(X, y, test_size=0.33)
    b = split(X, y, test_size=0.33)
    assert len(a[0]) == 4 and len(a[1]) == 2
    assert (a[0] == b[0]).all()
