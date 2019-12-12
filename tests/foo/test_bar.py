# -*- coding: utf-8 -*-

"""
Dummy test file.

Example file
"""
import unittest

import numpy as np

from foo.bar import bar_function


def dummy_function():
    """
    Show usage of 3rd party lib.

    Returns:
        NumPy Array
    """
    return np.array()


def test_bar():
    """
    Dummy test.

    Raises:
        Assertion Error if the values do not match
    """
    unittest.TestCase.assertEqual(bar_function(), 4)
