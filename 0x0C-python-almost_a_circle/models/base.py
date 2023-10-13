#!/usr/bin/python3
""" this file contain a class called Base """


class Base:
    """ creates a class called Base """

    __nb_objects = 0

    def __init__(self, id=None):
        """ initializing class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
