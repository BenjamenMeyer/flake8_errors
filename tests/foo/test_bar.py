"""Dummy test file."""
import numpy as np

from foo.bar import bar_function


def dummy_function():
    """Dummy function to use 3rd party lib."""
    return np.array()


def test_bar():
    """Dummy test."""
    assert bar_function() == 4
