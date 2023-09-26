#!/usr/bin/python3
"""My square module"""

class Square:
    """defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Create a Square"""
        self.size = size
        self.position = position


    @property
    def size(self):
        """"The propery of size as the len of a side of Square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """property of the coordinates of this Square """
        return self.__position

    @position.setter
    def position(self, value):
        """set the position of this Square"""
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Get the area of a Square"""
        return self.__size ** 2

    def my_print(self):
        """print the square in position"""
        if(self.size == 0):
            print()
        else:
            for x in range(self.position[1]):
                print()
            for x in range(self.size):
                print("{}{}".format(" " * self.position[0], "#" * self.size))
