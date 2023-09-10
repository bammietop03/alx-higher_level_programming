#!/usr/bin/python3
def max_integer(my_list=[]):
    max = 0
    if not my_list:
        return None
    else:
        for i in my_list:
            if i > max:
                max = i
        return max
