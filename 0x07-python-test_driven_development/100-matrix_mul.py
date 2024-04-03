#!/usr/bin/python3
"""Module that multiplies matrices."""


def matrix_mul(m_a, m_b):
    """The functions multiplies 2 matrices.

    Arg:
        m_a (list of lists of int/floats): first matrix
        m_b (list of lists of int/floats): second matrix

    Raise:
        TypeError: If not a list
        ValueError: If it is empty
        TypeError: If not an int/float
        TypeError: If not a rectangle
        ValueError: If it can't be multiplied
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    # check if is a list of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    # check if list is empty
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    # Check to contain integer or float
    if not all(all(isinstance(val, (int, float)) for row in m_a) for val in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(all(isinstance(val, (int, float)) for row in m_b) for val in row):
        raise TypeError("m_b should contain only integers or floats")
    # check if all row have the same size or not
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("Each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("Each row of m_b must be of the same size")
    # check if matrices can't be multiplied

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result


if __name__ == "__main__":
    matrix_mul = __import__('100-matrix_mul').matrix_mul
    print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))

    print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
