def spiral(n):
    """
    Square numbers in a spiral matrix.
    """
    dx,dy = 1, 0 # starting increments
    x,y = 0, 0 # starting location
    myarray = [[None]* n for j in range(n)]
