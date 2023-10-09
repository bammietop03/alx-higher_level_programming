#!/usr/bin/python3
""" Write a class MyList that inherits from list """


class MyList(list):
    """ the mylist class """

    def print_sorted(self):
        """ prints the list, but sorted (ascending sort) """
        sorted_list = sorted(self)
        print(sorted_list)
