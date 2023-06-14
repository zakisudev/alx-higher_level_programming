#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    product_sum = sum([score * weight for score, weight in my_list])
    weight_sum = sum([weight for score, weight in my_list])
    return product_sum / weight_sum
