#!/usr/bin/python3
"""Defines a function that adds attributes to objects"""


def add_attribute(obj, attr, value):
    """ Adds new attribute """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr, value)
