#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary) == 0 or a_dictionary is None:
        return None
    else:
        x = list(a_dictionary.keys())
        y = list(a_dictionary.values())
        return (x[y.index(max(y))])
