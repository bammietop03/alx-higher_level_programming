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
