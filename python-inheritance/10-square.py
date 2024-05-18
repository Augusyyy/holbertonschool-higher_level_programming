"""
10-square.py
题目要求：
1 在9的基础上，添加类class Square，继承自 Rectangle
2 class Square 中增加 def __init__(self, size):
    检查size的合法性
    并且赋值给class Square的成员变量self.__size
    并且调用父亲的__init__
        super.__inti__(self.__size,self.__size)
"""


class BaseGeometry:

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):

    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string


class Square(Rectangle):

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
