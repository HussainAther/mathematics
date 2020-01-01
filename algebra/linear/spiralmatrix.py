def spiral(n):
    """
    Square numbers in a spiral matrix.
    """
    dx,dy = 1, 0 # starting increments
    x,y = 0, 0 # starting location
    myarray = [[None]* n for j in range(n)]
    for i in xrange(n**2):
        myarray[x][y] = i
        nx,ny = x+dx, y+dy
        if 0 <= nx< n and 0 <= ny < n and myarray[nx][ny] == None:
            x, y = nx, ny
        else:
            dx, dy = -dy, dx
            x,y = x+dx, y+dy
    return myarray
