#!/usr/bin/python3
def element_at(my_list, idx):
    for i in my_list:
        if idx < 0:
            return None
        elif idx > len(my_list):
            return None
        elif idx == my_list.index(i):
            return i
