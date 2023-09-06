#!/usr/bin/python3
"""Divide a matrix Module"""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix.

    Args:
        matrix: list of lists of integer or float
        div: number integer or float

    Raises:
        TypeError: matrix must be a matrix (list of lists)
        TypeError: Each row of the matrix
        TypeError: div must be a number
        ZeroDivisionError: division by zero
    """
    if not isinstance(matrix, list):
        raise TypeError("\
            matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    size = len(matrix[0])
    new_matrix = []
    i = 0
    for lst in matrix:
        j = 0
        if not isinstance(lst, list):
            raise TypeError("matrix\
                must be a matrix (list of lists) of integers/floats")
        if size != len(lst):
            raise TypeError("Each row of the matrix must have the same size")

        lst_tmp = []
        for item in lst:
            if not isinstance(item, (float, int)):
                raise TypeError("matrix must be\
                    a matrix (list of lists) of integers/floats")
            lst_tmp.append(round(item / div, 2))
            j += 1
        new_matrix.append(lst_tmp)
        i += 1

    return new_matrix
