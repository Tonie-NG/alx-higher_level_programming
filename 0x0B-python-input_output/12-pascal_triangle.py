#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    p_triangle = [[1]]
    while len(p_triangle) != n:
        last_entry = p_triangle[-1]
        new_entry = [1]
        for i in range(len(last_entry) - 1):
            new_entry.append(last_entry[i] + last_entry[i+1])
        new_entry.append(1)
        p_triangle.append(new_entry)
    return p_triangle
