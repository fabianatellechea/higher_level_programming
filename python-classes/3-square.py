#!/usr/bin/python3
""" class square """


class Square:
    """ class Square that defines a square """

    def __init__(self, size=0):
        """ class Square init """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """ returns the current square area """

        return self.__size * self.__size
