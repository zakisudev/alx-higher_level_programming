#!/usr/bin/python3
""" Find the peak in an unsorted list """


def peak_rec(arr, lst, r):
    """Recursive way"""
    if lst == r:
        return arr[l]
    if r - lst == 1:
        return max(arr[r], arr[lst])
    m = (r + lst) // 2
    if arr[m] < arr[m + 1]:
        return peak_rec(arr, m + 1, r)
    return peak_rec(arr, lst, m)


def find_peak_rec(list_of_integers):
    """Function to find a peak in a list"""
    if list_of_integers == []:
        return None
    lng = len(list_of_integers)
    arr = list_of_integers
    return peak_rec(arr, 0, lng - 1)


def find_peak_0(list_of_integers):
    """Function to find a peak in a list"""
    if list_of_integers == []:
        return None
    lnn = len(list_of_integers)
    m = lnn // 2
    arr = list_of_integers
    while True:
        if m != 0 and m != lnn - 1 and arr[m - 1] < arr[m] < arr[m + 1]:
            m = (l + m) // 2
        elif m != 0 and m != lnn - 1 and arr[m - 1] > arr[m] > arr[m + 1]:
            m = m // 2
        elif m != 0 and m != lnn - 1 and arr[m - 1] > arr[m] < arr[m + 1]:
            m = m // 2
        else:
            return arr[m]


def find_peak(list_of_integers):
    """Function to find a peak in a list"""
    if list_of_integers == []:
        return None
    lngg = len(list_of_integers)
    m = lngg // 2
    arr = list_of_integers
    while True:
        if m in (0, lngg - 1) or arr[m - 1] < arr[m] > arr[m + 1]:
            return arr[m]
        if arr[m] < arr[m + 1]:
            m = (lngg + m) // 2
        else:
            m = m // 2


def find_peak_2(list_of_integers):
    """Function to find a peak in a list"""
    if list_of_integers == []:
        return None
    p = 0
    arr = list_of_integers
    while True:
        try:
            if arr[p] > arr[p + 1]:
                return arr[p]
            p += 1
        except IndexError:
            return arr[p]
