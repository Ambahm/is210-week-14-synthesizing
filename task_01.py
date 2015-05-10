#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A Fibonacci generator (yield)"""


def xfibo(count):
    """Function generates a Fibonacci Number Series, using generator
        Setting F0=0, F1=1, and then using the recursive formula
        Fn = Fn-1 + Fn-2 
 
    Args:
        count (int): Number of integers to return in the sequence.

    Returns:
        list: Yields a list of Fibonacci numbers.

    Examples:
        >>> for i in xfibo(10):
                print i
        0
        1
        1
        2
        3
        5
        8
    """
    x, y = 0, 1
    while x < count:
        yield x
        x, y = y, x + y # x, y increment




if __name__ == '__main__':
    for i in xfibo(10):
        print i
