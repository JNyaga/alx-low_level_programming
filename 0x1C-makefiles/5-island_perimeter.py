#!/usr/bin/python3
"""Module to define a function island_perimeter"""


def island_perimeter(grid):
    """Function to calculate an island described in a grid perimeter

    grid is a list of list of integers:
    0 represents a water zone
    1 represents a land zone
    One cell is a square with side length 1
    """
    width = len(grid[0])
    height = len(grid)
    edges = 0
    size = 0

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                size += 1
                if (j > 0 and grid[i][j - 1] == 1):
                    edges += 1
                if (i > 0 and grid[i - 1][j] == 1):
                    edges += 1
    return size * 4 - edges * 2


''' OR '''


''' class Solution:
    def solve(self, matrix):
        d = 0
        perimeter = 0
        height = len(matrix)
        length = len(matrix[0])
        for line in matrix:
            c = 0

            for val in line:
                if val == 1:
                    surround = 4
                    if c != length - 1:
                        if matrix[d][c + 1] == 1:
                            surround -= 1
                    if c != 0:
                        if matrix[d][c - 1] == 1:
                            surround -= 1
                    if d != height - 1:
                        if matrix[d + 1][c] == 1:
                            surround -= 1
                    if d != 0:
                        if matrix[d - 1][c] == 1:
                            surround -= 1
                    perimeter += surround
                c += 1
            d += 1
        return perimeter


ob = Solution()
matrix = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1],
    [0, 0, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
print(ob.solve(matrix)) '''
