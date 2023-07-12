#!/usr/bin/python3
""" Define a pascal triangle function """


def pascal_triangle(n):
    """ defines a pascal triangle of size n """
    if n <= 0:
        return []

    tris = [[1]]
    while len(tris) != n:
        tr = tris[-1]
        temp = [1]
        for i in range(len(tr) - 1):
            temp.append(tr[i] + tr[i + 1])
        temp.append(1)
        tris.append(temp)
    return tris
