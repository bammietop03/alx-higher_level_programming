#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    temp_dic = {}
    for key, value in a_dictionary.items():
        temp_dic.update({key:value * 2})
    return temp_dic
