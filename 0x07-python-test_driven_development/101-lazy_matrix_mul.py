#!/usr/bin/python3
""" function that multiplies 2 matrices by using the module NumPy"""


import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices m_a and m_b using NumPy.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        A new matrix as the result of the multiplication.

    Raises:
        ValueError: If m_a or m_b is not a valid matrix for multiplication.
    """
    try:
        np_a = np.array(m_a)
        np_b = np.array(m_b)
        result = np.dot(np_a, np_b)

        return result.tolist()
    except ValueError:
        raise ValueError("m_a and m_b can't be multiplied")
