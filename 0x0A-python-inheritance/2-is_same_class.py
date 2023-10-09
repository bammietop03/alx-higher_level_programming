#!/usr/bin/python3
""" Write a function that returns True if the object is
    exactly an instance of the specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """ returns true or false """
    return type(obj) is a_class
