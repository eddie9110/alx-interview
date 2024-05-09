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

    for a, b in enumerate(grid):
        for i, j in enumerate(b):
            if j == 1:
                if grid[a][i + 1] != 1 or i == len(grid[0]) - 1:
                    perimeter += 1
                if grid[a][i - 1] != 1 or i == 0:
                    perimeter += 1
                if grid[a + 1][i] != 1 or a == len(grid) - 1:
                    perimeter += 1
                if grid[a - 1][i] != 1 or a == 0:
                    perimeter += 1
    return perimeter
