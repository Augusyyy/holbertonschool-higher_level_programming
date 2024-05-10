#!/usr/bin/python3
import sys


def factorial(n):
    """
    Calculate the factorial of a given number using recursion.

    Parameters:
    n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
    int: The factorial of the number 'n'.

    Description:
    The factorial of a number 'n' is the product of all positive integers less than or equal to 'n'.
    It is defined as n! = n * (n-1) * (n-2) * ... * 1. The factorial of 0 is defined as 1.
    This function uses a recursive approach to calculate the factorial.
    """

    if n == 0:
        # Base case: factorial of 0 is 1
        return 1
    else:
        # Recursive case: n! = n * (n-1)!
        return n * factorial(n - 1)


# Get the integer from the command line argument, calculate its factorial, and print it
f = factorial(int(sys.argv[1]))
print(f)
