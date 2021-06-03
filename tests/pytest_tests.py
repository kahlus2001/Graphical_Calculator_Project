"""Graphical calculator program: the pytests.

Author: Mikolaj Kahl and Joris Wijnands

Copyright (c) 2021 - Eindhoven University of Technology, The Netherlands

This software is made available under the terms of the MIT License.
"""

from math_functions import *
import doctest


def test_evaluate() -> None:
    """Tests evaluate function for chosen values.
    """
    doctest.run_docstring_examples(evaluate, globals(), verbose=True, name='evaluate')


def test_find_roots() -> None:
    """Tests find_roots function for chosen values.
    """
    doctest.run_docstring_examples(find_roots, globals(), verbose=True, name='find_roots')


