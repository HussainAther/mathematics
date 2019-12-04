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
        How does the ball move?
        """
        self.x += random.randint(0,1)
        self.y += 1
 
    def fall(self):
        """
        It falls!
        """
        self.y += 1 
