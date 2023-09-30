#!/usr/bin/python3
""" Get the peak of an unsorted list """

def find_peak(list_of_integers):
    """ finds the peak of an unsorted list """

    if list_of_integers is None or list_of_integers == []:
        return None
    peak = None
    for num in list_of_integers:
        if peak is None or peak < num:
            peak = num
    return peak
