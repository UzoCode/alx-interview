#!/usr/bin/python3
"""
Function that generate pascal triangle to the nth row
"""


def pascal_triangle(n):
    """
    Args: n (int): The row of the pascal triangle to generate

    Returns: A list of lists, each sublist is a row of the pascal triangle.
        Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # The first row is always [1]

    for i in range(1, n):
        row = [1]  # First element is always 1
        for j in range(1, i):
            # Each element is the sum of the two elements directly above it
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # Last element is always 1
        triangle.append(row)

    return triangle
