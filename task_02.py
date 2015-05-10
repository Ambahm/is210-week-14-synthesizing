#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A Fibonacci List Comprehension"""

import task_01

def fibo(count):
    """Function generates a Fibonacci Number Series comprehension,
    using generator from other module

    Args:
        count (int): Number of integers to return in the sequence.

    Returns:
        list: Yields a list of Fibonacci numbers.

    Examples:
        >>> print fibo(5)
            [0, 1, 1, 2, 3]
        >>> print fibo(10)
            [0, 1, 1, 2, 3, 5, 8]
    """
    return [listitem for listitem in task_01.xfibo(count)] # list comprehension


if __name__ == '__main__':
        print fibo(5)
        print fibo(10)
