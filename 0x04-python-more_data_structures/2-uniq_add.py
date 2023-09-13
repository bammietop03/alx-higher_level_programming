#!/usr/bim/python3
def uniq_add(my_list=[]):
    unique = set()
    sum = 0
    for num in my_list:
        if num not in unique:
            unique.add(num)
            sum += num
    return sum
