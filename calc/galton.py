import os
import random
import sys
import time

"""
Bean machine galton box to show the central limit theorem
"""

def printit(x, y, text):
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
 
    def addball(self):
        """
        Should we add a ball? This is following an update.
        """
        if(len(self.balls) <= self.N):
            self.balls.append(Ball())

    def printboard(self):
        """
        Print it line by line.
        """
        for y in range(self.width + 1):
            for x in range(y):
                printit( y + 1 ,self.width - y + 2*x + self.shift + 1, "#")

    def printball(self, ball):
        """
        Show us the ball's status.
        """
        if ball.y <= self.width:
            x = self.width - ball.y + 2*ball.x + self.shift
        else:
            x = 2*ball.x + self.shift
        y = ball.y + 1
        printit(y, x, "*")

    def printall(self):
        """
        Print everything as they are.
        """
        print(chr(27) + "[2J")
        self.print_board();
        for ball in self.balls:
            self.print_ball(ball)

def main():
    """
    Run it.
    """
    board = Board(width = 15, well_depth = 5, N = 10)
    board.addball() # initialization
    while(board.balls_on_board() > 0):
         board.printall()
         time.sleep(0.25)
         board.update()
         board.printall()
         time.sleep(0.25)
         board.update()
         board.addball()
 
if __name__=="__main__":
    main() 
