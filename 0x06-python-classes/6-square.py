#!/usr/bin/python3
# 5-square.py
"""Defines a square """


class Square:
    """Represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializing this square class """

        self.size = size
        self.position = position

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
    
    @property
    def position(self):
        return self.__position

    @size.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """ returns the current square area """

        return self.__size ** 2

    def my_print(self):
        """  prints in stdout the square with the character # """
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.size):
                print("{}{}".format(" " * self.position[0], "#" * self.size))
