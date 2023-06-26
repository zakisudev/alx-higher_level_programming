#!/usr/bin/python3
def safe_print_division(a, b):
    answer = None
    try:
        res = a / b
    except ZeroDivisionError:
        return
    finally:
        print("Inside result: {:.1}".format(res))
    return (answer)
