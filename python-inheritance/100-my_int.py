#!/usr/bin/python3
"""MyInt module.

Contains a class MyInt that inherits from int.
"""


class MyInt(int):
    """Defines the MyInt class."""

    def __eq__(self, value):
        """Sets the == behaviour."""
        return self.real != value

    def __ne__(self, value):
        """Sets the != behaviour."""
        return self.real == value
