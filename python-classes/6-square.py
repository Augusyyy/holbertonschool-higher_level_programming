#!/usr/bin/python3
"""
Module 6-square
Defines class Square with private size and position; and public area
Can access and update size and position
Can print to stdout the square using #'s
"""


class Square:
    """
        class Square definition

        Args:
            size (int): size of a side in square

        Functions:
            __init__(self, size, position)
            size(self)
            size(self, value)
            position(self)
            position(self, value)
            area(self)
            my_print(self)
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes square

        Attributes:
            size (int): defaults to 0 if none; don't use __size to call setter
            position (int): tuple of two positive integers
        """
        self.__size = size

        if type(position) is tuple and len(position) is 2 and \
                type(position[0]) is int and type(position[1]) is int and \
                position[0] >= 0 and position[1] >= 0:
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = position

    @property
    def size(self):
        """"
        Getter

        Return: size
        """
        return self.__size

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

    @property
    def position(self):
        """"
        Getter

        Return: position
        """
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is tuple and len(value) is 2 and \
                type(value[0]) is int and type(value[1]) is int and \
                value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

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
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
