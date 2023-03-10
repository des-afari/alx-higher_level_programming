#!/usr/bin/python3

def print_square(size):
    """Function that prints a square of a given size in '#' characters:

    Args:
        size (int): length of side of square, in monospace chars

    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for row in range(size):
        for col in range(size):
            print('#', end="")
        print()
