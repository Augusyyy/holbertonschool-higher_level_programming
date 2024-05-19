#!/usr/bin/python3
import math
from abc import ABC, abstractmethod
"""
This is the Shape module.
This module supplies abstractmethod
"""


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * self.width + self.height


def shape_info(shape):
    """ Print the area and perimeter of the shape """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
