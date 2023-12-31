#!/usr/bin/python3
"""
0-pascal_triangle
"""

def pascal_triangle(n):
    """
    Creates a list of lists of integers representing
    the Pascal's triangle of a given integer.
    """
    if n <= 0:
        return []

    # Initializing Pascal's triangle with the first row
    triangle = [[1]]

    while len(triangle) < n:
        # Generating the next row based on the previous row
        prev_row = triangle[-1]
        next_row = [1]

        for i in range(1, len(prev_row)):
            next_row.append(prev_row[i - 1] + prev_row[i])

        next_row.append(1)
        triangle.append(next_row)

    return triangle