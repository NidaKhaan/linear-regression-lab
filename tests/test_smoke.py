from lrlab.config import SEED


def test_seed_is_fixed():
    assert SEED == 42
