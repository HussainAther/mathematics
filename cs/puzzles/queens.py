"""
A lovely chess problem.

The 8-Queens problem on a chessboard corresponds to finding a placement of 8 queens
such that no queen attacks any other queen. This means that
1. No two queens can be on the same column.
2. No two queens can be on the same row.
3. No two queens can be on the same diagonal.

Systematic search.

This is how I play chess: https://www.youtube.com/watch?v=8ghGvbdlTDQ
"""

def noConflicts(board, current):
    """
    Check to make sure we're playing by the rules.
    """
    for i in range(current):
        if (board[i] == board[current]):
            return False
        if (current - i == abs(board[current] - board[i])):
            return False
    return True

def EightQueens(numsol, n=8):
    """
    Place 8 queens on a board so they don't break rules.
    """
    board = [-1] * n
    sol = 0
    for i in range(n):
    
