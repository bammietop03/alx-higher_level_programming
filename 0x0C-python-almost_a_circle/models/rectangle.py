#!/usr/bin/python3
""" Write the class Rectangle that inherits from Base: """
from models.base import Base


class Rectangle(Base):
    """ Rectangle Class Created """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializing... """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("Width must be an integer")
            if value <= 0:
                raise ValueError("Width must be greater than 0")
            self.__width = value

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("Height must be an integer")
            if value <= 0:
                raise ValueError("Height must be greater than 0")
            self.__height = value

        @property
        def x(self):
            return self.__x

        @x.setter
        def x(self, value):
            if not isinstance(value, int):
                raise TypeError("X must be an integer")
            self.__x = value

        @property
        def y(self):
            return self.__y

        @y.setter
        def y(self, value):
            if not isinstance(value, int):
                raise TypeError("Y must be an integer")
            self.__y = value

