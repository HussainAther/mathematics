"""
Sudoku is a popular number-placement puzzle. The objective is to fill a partially filled 9
× 9 grid with digits so that each column, each row, and each of the nine 3 × 3 sub-grids or
sectors that compose the grid contains all of the digits from 1 to 9.

These constraints are used to determine the missing numbers. In the puzzle below,
several sub-grids have missing numbers. Scanning rows (or columns as the case may be)
can tell us where to place a missing number in a sector.

Our goal is to write a recursive Sudoku solver that solves any Sudoku puzzle regardless
of how many numbers are filled in. Then, we will add “human intelligence” to the solver.

Given a partially filled in Sudoku board, complete the puzzle.
"""

sectors = [ [0, 3, 0, 3], [3, 6, 0, 3], [6, 9, 0, 3],
            [0, 3, 3, 6], [3, 6, 3, 6], [6, 9, 3, 6],
            [0, 3, 6, 9], [3, 6, 6, 9], [6, 9, 6, 9] ]


def findNextCellToFill(grid):
    """
    Find the next cell to fill in. This should be an unused location.
    """
    for x in range(0, 9):
        for y in range(0, 9):
            if grid[x][y] == 0:
                return x,y
    return -1,-1

def isValid(grid, i, j, e):
    """
    Check if the position is valid.
    """
    rowOk = all([e != grid[i][x] for x in range(9)])
    if rowOk:
        columnOk = all([e != grid[x][j] for x in range(9)])
        if columnOk:
            #finding the top left x,y co-ordinates of
            #the section or sub-grid containing the i,j cell
            secTopX, secTopY = 3 *(i//3), 3 *(j//3)
            for x in range(secTopX, secTopX+3):
                for y in range(secTopY, secTopY+3):
                    if grid[x][y] == e:
                        return False
            return True
    return False
