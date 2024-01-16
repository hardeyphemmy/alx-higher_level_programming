#!/usr/bin/python3
"""Module that multiplies matrices."""


def matrices_mul(m_a, m_b):
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

    if not (isinstance(m_a, list) and isinstance(m_b, list)):
        raise TypeError("m_a must be a list or m_b must be a list")

    for matrix in [m_a, m_b]:
        # check if is not list of lists
        if not all(isinstance(row, list) for row in matrix) and not all(
                isinstance(element, (int, float)) for element in row for row
                           in matrix):
            raise TypeError("m_a must be a list of lists or m_b must be a list"
                            "of lists")

        # check if list is empty
        if m_a == [] or m_a == [[]]:
            raise ValueError("m_a can't be empty")

        if m_b == [] or m_b == [[]]:
            raise ValueError("m_b can't be empty")

        # check if all row have the same size
        row_sizes = set(len(row) for row in matrix)
        if len(row_sizes) > 1:
            raise TypeError("each row of m_a must be of the same size or "
                            "each row of m_b must be of the same size")

    # check if matrices can be multiplied
    num_column_m_a = len(m_a[0] if m_a else 0)
    num_row_m_b = len(m_b) if m_b else 0

    if num_column_m_a != num_row_m_b:
        raise ValueError("m_a and m_b can't be multiplied")

    pass


if __name__ == "__main__":
    print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
    
    print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
