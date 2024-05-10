#!/usr/bin/python3
"""
Module 5-square
Defines class Square with private size and public area
Can access and update size
Can print to stdout the square using #'s
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
            print(self)
        """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

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
            value: sets size to value if int and >= 0
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
        return self.__size * self.__size

    def my_print(self):
        """
        Prints square with #'s
        """
        if self.__size == 0:
            print("")
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end="")
            print("")
