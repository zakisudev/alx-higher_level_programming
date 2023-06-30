#!/usr/bin/python3
""" Defines matrix_devide function """


def matrix_divided(matrix, div):
    """ Devides matrix by integers or floats of
    two decimal places."""
    import decimal
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(msg)
    len_row = []
    row_count = 0
    for row in matrix:
        if type(row) is not list:
            raise TypeError(msg)
        len_row.append(len(row))
        for dat in row:
            if type(dat) not in [int, float]:
                raise TypeError(msg)
        row_count += 1
    if len(set(len_row)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if int(div) == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = list(map(lambda row:
            list(map(lambda x: round(x/div, 2), row)), matrix))
    return new_matrix
