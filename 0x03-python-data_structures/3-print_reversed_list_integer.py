#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list) - 1, -1, -1):
        if len(my_list) <= 0:
            return None
        else:
            print("{:d}".format(my_list[i]))
    print(end="")
