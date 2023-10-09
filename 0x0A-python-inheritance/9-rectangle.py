#!/usr/bin/python3
""" Write an empty class BaseGeometry. """


class BaseGeometry:
    """ class created """

    def area(self):
        """ raises an Exception with the message """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """  validates value """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ Rectangle that inherits from BaseGeometry """

    def __init__(self, width, height):
        """ Intialize a new Rectangle. """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
