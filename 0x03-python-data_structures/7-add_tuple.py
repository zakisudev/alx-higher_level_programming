#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)
    a1 = tuple_a[0]
    a2 = tuple_a[1]
    b1 = tuple_b[0]
    b2 = tuple_b[1]
    sum1 = a1 + b1
    sum2 = a2 + b2
    all_sum = [sum1, sum2]
    return (tuple(all_sum))
