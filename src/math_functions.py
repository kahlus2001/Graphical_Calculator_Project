"""Graphical calculator program: the math functions.

Author: Mikolaj Kahl and Joris Wijnands

Copyright (c) 2021 - Eindhoven University of Technology, The Netherlands

This software is made available under the terms of the MIT License.
"""

from typing import Any

import math
import numpy as np
import matplotlib.pyplot as plt

def evaluate(expression: str) -> Any:
    """Evaluate mathematical expression provided by user.
    >>> evaluate('2*3')
    6
    >>> evaluate('3/3')
    1.0
    >>>evaluate('1/0')
    "invalid input"
    """
    try:
        print(expression, '=', eval(expression))
        return eval(expression)
    except:
        print('invalid input')
        return "invalid input"


def plot(formula: str, x_range):
    """Plot a graph using user input function.

    """
    # for now, the function only works if the input is in python: it will not plot 'sin(x)' or 'e^x'.

    i = True
    while i:
        try:
            x = np.array(x_range)
            y = eval(formula)
            plt.plot(x, y)
            plt.title(f"graph of y={formula}")
            plt.show()
            i = False
        except:
            return 'Cannot plot function. Invalid input. Please try again.'
            # now we need the user to input function once again
            i = False

