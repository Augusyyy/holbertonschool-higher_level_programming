#!/usr/bin/python3
"""
Module 102-square
Defines class Square with private size and public area
Can access and update size
"""


class Square:
    """
    class Square definition

    Args:
        size (int): size of a side in square

    Functions:
        __init__(self, size)
        size(self)
        size(self, value)
        area(self)
    """

    def __init__(self, size=0):
        """
        Initializes square

        Attributes:
            size (int): defaults to 0 if none; don't use __size to call setter
        """
        self.size = size

    @property
    def size(self):
        """"
        Getter

        Return: size
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Setter

        Args:
            value: sets size to value, if int and >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates area of square
        Returns:
            area
        """
        return (self.__size * self.__size)

    def __eq__(self, other):
        """
        Compares and returns if equal
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Compares and returns if not equal
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Compares and returns if lesser than
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Compares and returns if lesser than or equal to
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Compares and returns if greater than
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Compares and returns if greater than or equal to
        """
        return self.area() >= other.area()
