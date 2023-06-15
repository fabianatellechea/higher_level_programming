#!/usr/bin/python3
""" class Rectangle """


class Rectangle:
    """ defines a rectangle """

    def __init__(self, width=0, height=0):

        self.__width = width
        self.__height = height

        if type(self.__width) is not int:
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        if type(self.__height) is not int:
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

        if type(self.__width) is not int:
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

        if type(self.__height) is not int:
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ("")

        return (("#" * self.__width + "\n") * self.__height).rstrip()

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)
