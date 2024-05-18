#!/usr/bin/python3
"""
This is the say_my_name module.

This module supplies one function, say_my_name().
"""


def say_my_name(first_name, last_name=""):
    """
    Print My name is <first name> <last name>.

    Args:
        first_name (str): the first name.
        last_name (str): the last name.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if first_name and last_name:
        print("My name is {:s} {:s}".format(first_name, last_name))
    elif first_name:
        print("My name is {:s}".format(first_name))
    elif last_name:
        print("My name is  {:s}".format(last_name))
    else:
        print("My name is")