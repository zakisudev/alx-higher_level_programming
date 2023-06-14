#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new = a_dictionary.copy()
    try:
        for x in new:
            if value == a_dictionary[x]:
                del a_dictionary[x]
        return (a_dictionary)
    except KeyError:
        return (a_dictionary)
