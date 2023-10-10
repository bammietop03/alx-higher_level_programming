#!/usr/bin/python3
"""Module Defines a Python class-to-JSON function."""


def class_to_json(obj):
    """ class to json """
    return obj.__dict__
