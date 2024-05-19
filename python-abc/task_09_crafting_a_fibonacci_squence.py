#!/usr/bin/python3
from collections.abc import Iterator
"""
This is the Fibonacci module.
This module supplies override
"""


class Fibonacci(Iterator):
    def __init__(self):
        """
        Initialize the first two Fibonacci numbers.
        """
        self.a, self.b = 0, 1

    def __iter__(self):
        """
        Return the iterator object itself.
        """
        return self

    def __next__(self):
        """
        Save the current Fibonacci number, update to the
        next Fibonacci numbers,
        and return the current Fibonacci number.
        """
        current = self.a
        self.a, self.b = self.b, self.a + self.b
        return current

    def reset(self):
        """
        Reset the Fibonacci sequence to the beginning.
        """
        self.a, self.b = 0, 1
