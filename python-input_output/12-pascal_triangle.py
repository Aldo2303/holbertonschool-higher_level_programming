#!/usr/bin/python3
"""Module 12-pascal_triangle"""


def pascal_triangle(n):
    """
    function that returns the representation of the Pascal's Triangle
    """
    triangle = []
    if n <= 0:
        return triangle
    else:
        triangle.append([1])

        for i in range(1, n):
            triangle.append([1])
            for j in range(1, i + 1):
                try:
                    triangle[i].append(triangle[i-1][j] + triangle[i-1][j-1])
                except IndexError:
                    triangle[i].append(1)
                    continue
    return triangle
