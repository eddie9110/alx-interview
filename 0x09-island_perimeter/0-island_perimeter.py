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

    for x in range(len(grid)):
        for a in range(len(grid[x])):
            if grid[x][a] == 1:
                if grid[x][a - 1] == 0 or a == 0:
                    perimeter += 1
                if grid[x - 1][a] == 0 or x == 0:
                    perimeter += 1
                if grid[x][a + 1] == 0 or a == len(grid[x]) - 1:
                    perimeter += 1
                if grid[x + 1][a] == 0 or x == len(grid) - 1:
                    perimeter += 1
    return perimeter
