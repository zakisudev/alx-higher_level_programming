#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    ans = None
    try:
        ans = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
    return (ans)
