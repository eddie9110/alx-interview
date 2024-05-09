#!/usr/bin/python3
"""
module contains function that returns
the perimeter of the island described in grid
"""


def island_perimeter(grid):
    """
    Function that calculates the perimeter of Island i.e grid
    Returns perimeter
    """

    perimeter = 0
    rows = 0
    cols = 0
    for x in range(len(grid)):
        for a in range(len(grid[0])):
            if grid[x][a] == 1:
                cols += 2
                if a > 0 and grid[x][a - 1] == 1:
                    rows += 1
                if x > 0 and grid[x - 1][a] == 1:
                    rows += 1
    perimeter = cols * 2 - rows * 2

    return perimeter
