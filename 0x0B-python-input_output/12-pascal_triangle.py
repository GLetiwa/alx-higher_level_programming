#!/usr/bin/python3
"""pascal triangle function"""


def pascal_triangle(n):
    """returns a list of lists of integers"""

    if n <= 0:
        return []

    matrix = [[1]]
    while len(matrix) != n:
        row = matrix[-1]
        tmp = [1]
        for i in range(len(row) - 1):
            tmp.append(row[i] + row[i + 1])
        tmp.append(1)
        matrix.append(tmp)
    return matrix
