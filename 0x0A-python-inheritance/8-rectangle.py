#!/usr/bin/python3
""" Write an empty class BaseGeometry. """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
