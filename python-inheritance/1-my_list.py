#!/usr/bin/python3
"""MyList module.

Contains a class MyList that inherits from list
and a method that prints the sorted list.
"""


class MyList(list):
    """Defines the MyList class."""
    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
