#!/usr/bin/python3
def max_integer(my_list=[]):
    max = 0
    if not my_list:
        return None
    else:
        for i in my_list:
            if int(i) > max:
                max = int(i)
        return max
