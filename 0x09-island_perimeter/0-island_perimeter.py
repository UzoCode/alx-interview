#!/usr/bin/python3
"""
The Island Perimeter
"""

def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid
    :param grid:
    :return:
    """
    area = 0
    for row in grid + list(map(list, zip(*grid))):
        for i1, i2 in zip([0] + row, row + [0]):
            area += int(i1 != i2)
    return area
