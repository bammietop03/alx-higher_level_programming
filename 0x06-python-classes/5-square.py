#!/usr/bin/python3
# 5-square.py
"""Defines a square """


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initializing this square class """

        if isinstance(size, int):
            self.__size = size
        else:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ returns the current square area """

        return self.__size ** 2

    def my_print(self):
        """  prints in stdout the square with the character # """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
