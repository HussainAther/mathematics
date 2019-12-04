import sys, os
import random
import time

"""
Bean machine galton box to show the central limit theorem
"""

def print_there(x, y, text):
    """
    Print function for each layer. 
    """
    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
    sys.stdout.flush()

class Ball():
    def __init__(self):
        """
        Initialize x and y positions.
        """
        self.x = 0
        self.y = 0
 
    def update(self):
        """
        How does the ball move? We use the y coordinate to show
        how deep we've fallen.
        """
        self.x += random.randint(0,1)
        self.y += 1
 
    def fall(self):
        """
        It falls! Increase y to show how far we've fallen.
        """
        self.y += 1 

class Board():
    def __init__(self, width, well_depth, N):
        """
        Keep track of each ball on the board.
        """
        self.balls = []
        self.fallen = [0] * (width + 1)
        self.width = width
        self.well_depth = well_depth
        self.N = N
        self.shift = 4

    def update(self):
        """
        Determine if the ball falls.
        """
        for ball in self.balls:
            if ball.y < self.width:
                ball.update()
            elif ball.y < self.width + self.well_depth - self.fallen[ball.x]:
                ball.fall()
            elif ball.y == self.width + self.well_depth - self.fallen[ball.x]:
                self.fallen[ball.x] += 1
            else:
                pass

    def balls_on_board(self):
        """
        What's going on?
        """
        return len(self.balls) - sum(self.fallen)
 
    def add_ball(self):
        if(len(self.balls) <= self.N):
            self.balls.append(Ball())
