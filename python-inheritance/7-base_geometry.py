#!/usr/bin/python3
"""BaseGeometry module.

Contains a class BaseGeometry, and some methods.
"""


class BaseGeometry:
    """Defines the BaseGeometry class."""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
