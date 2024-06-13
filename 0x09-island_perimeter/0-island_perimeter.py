#!/usr/bin/python3
"""this is a function"""


def island_perimeter(grid):
    """function to get island perimeter"""
    lenofrow = len(grid)
    lenofcol = len(grid[0])
    p = 0
    connections = 0

    for row in range(0, lenofrow):
        for col in range(0, lenofcol):
            if grid[row][col] == 1:
                p += 4
                if row != 0 and grid[row - 1][col] == 1:
                    connections += 1
                if col != 0 and grid[row][col - 1] == 1:
                    connections += 1
    return p - (connections * 2)
