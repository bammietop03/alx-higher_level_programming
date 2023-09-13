#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    score_sum = 0
    weight_sum = 0
    for score, weight in my_list:
        score_sum += score * weight
        weight_sum += weight
    if weight_sum != 0:
        weighted_average = score_sum / weight_sum
    else:
        weighted_average = 0.0
    return weighted_average
