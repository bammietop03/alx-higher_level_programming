#!/usr/bin/python3
""" Write a function that returns the JSON representation of an object """
import json


def to_json_string(my_obj):
    """ Return the JSON representation  """
    return json.dumps(my_obj)
