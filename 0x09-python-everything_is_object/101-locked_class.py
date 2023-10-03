#!/usr/bin/python3
""" LockedClass with no class or object attribute """


class LockedClass:
    """ Prevent the user from instantiating new 
    LockedClass attributes 
    """

    __slots__ = ['first_name']
