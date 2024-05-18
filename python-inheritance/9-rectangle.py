#!/usr/bin/python3
"""Rectangle module.

Contains a class Rectangle that inherits from
BaseGeometry and some methods.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines the Rectangle class that inherits from BaseGeometry."""
    def __init__(self, width, height):
        """Checks and sets the default attributes of Rectangle class."""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Sets the str behaviour."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
