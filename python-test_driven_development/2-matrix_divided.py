#!/usr/bin/python3
"""Module 2-matrix_divided"""


def matrix_divided(matrix, div):
    """
    function that divides all elements of a matrix
    The value matrix list of lists of integers or floats
    Arguments:
        matrix and div
    Return:
        a new matrix with the results of division
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    message = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(message)

    new_matrix = []
    result = 0
    list_len = len(matrix[0])
    for i in matrix:
        if type(i) is not list:
            raise TypeError(message)
        if len(i) != list_len:
            raise TypeError("Each row of the matrix must have the same size")
        new_list = []
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError(message)
            result = j / div
            new_list.append(round(result, 2))
        new_matrix.append(new_list)
    return new_matrix
