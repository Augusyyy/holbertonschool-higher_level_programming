#!/usr/bin/python3
"""Module for read_file method."""


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""
    with open(filename, "r", encoding="utf-8") as file_obj:
        print(file_obj.read(), end="")
