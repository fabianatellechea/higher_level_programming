#!/usr/bin/python3
""" class square """


class Square:
    """ Coordinates of a square """

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

        if type(value) is not tuple or value[0] < 0 or value[1] < 0 or value[0] is not int or value[1] is not int:
            raise TypeError("position must be a tuple of 2 positive integers")


    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print('_' * self.__position[0], end="")
            print('#' * self.__size)
