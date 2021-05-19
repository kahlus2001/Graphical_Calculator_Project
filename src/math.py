import math


def add(input_1: float, input_2: float) -> float:
    """Add two inputs got from the user.

    :examples:
    >>> add(2.0,3.0)
    5.0
    >>> add(1.1,0.0)
    1.1
    >>> add(77.0, 13.0)
    90.0
    """

    result = input_1 + input_2
    return result

def subtract(input_1: float, input_2: float) -> float :
    """Subtract two inputs got from the user.

    :examples:
    >>> subtract(4.111, 2.0)
    2.111
    >>> subtract(5.2, 6.0)
    -0.8
    >>> subtract(0.2,0.1)
    0.1
    """

    result = input_1 - input_2
    return result

def multiply(input_1: float, input_2: float) -> float:
    """Multiple two inputs got from the user.

    :examples:
    >>> multiply(2.0, 3.0)
    6.0
    >>> multiply(2.2, 3.14)
    6.908
    >>> multiply(2.0, 0.0)
    0.0
    """

    result = input_1 * input_2
    return result

def divide(input_1: float, input_2: float):
    """Divides first input from user by second input from user.

    :examples:
    >>> divide(2.0, 1.0)
    2.0
    >>> divide(13.3, 12.0)
    1.1083333333333334
    >>> divide(12.0, 0.0)
    "Math error. Division by 0 is not defined."
    """

    if input_1 == 0.0:
        return "Math error. Division by 0 is not defined."
    else:
        result = input_1 / input_2
        return result

def modulo(input_1: float, input_2: float) -> float:
    """Perform integer division of first user input by second user input.

    :examples:
    >>> modulo(2, 3)
    2
    >>> modulo(2, 2)
    0
    >>> modulo(5,3)
    2
    """

    result = input_1 % input_2
    return result