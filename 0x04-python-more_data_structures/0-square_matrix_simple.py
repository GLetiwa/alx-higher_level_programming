#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    a = []
    for i in matrix:
        b = []
        for j in i:
            b.append(j ** 2)
        a.append(b)
    return (a)


if __name__ == "__main__":
    square_matrix_simple()
