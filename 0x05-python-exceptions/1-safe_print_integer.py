#!/usr/bin/python3
def safe_print_integer(value):
    answer = false
    try:
        print("{:d}".format(value))
        answer = True
    except:
        answer = False
    return (answer)
