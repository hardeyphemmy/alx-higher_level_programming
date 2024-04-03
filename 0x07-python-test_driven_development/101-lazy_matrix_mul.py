#!/usr/bin/python3
"""Module that multiply matrix."""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of matrices.

    Arg:
        m_a: first matrix
        m_b: second matrix
    """

    return (np.matmul(m_a, m_b))


if __name__ == "__main__":
    print(lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
    print(lazy_matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
