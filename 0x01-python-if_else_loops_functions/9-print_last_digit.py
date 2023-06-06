#!/usr/bin/python3
def print_last_digit(number):
    my_num = abs(number) % 10
    print("{}".format(my_num), end="")
    return my_num
