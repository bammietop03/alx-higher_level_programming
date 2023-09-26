#!/usr/bin/python3
# 3-square.py
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

    def area(self):
        """ returns the current square area """

        return self.__size ** 2
