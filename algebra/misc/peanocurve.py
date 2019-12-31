import inspect
import turtle as tt

"""
Peano curve.
"""

stack = [] # Mark the current stacks in run.
def peano(iterations=1):
    global stack
    # The turtle Ivan:
    ivan = tt.Turtle(shape = "classic", visible = True)
 
    # The app window:
    screen = tt.Screen()
    screen.title("Desenhin do Peano")
    screen.bgcolor("#232323")
    screen.delay(0) # Speed on drawing (if higher, more slow)
    screen.setup(width=0.95, height=0.9)

    # The size of each step walked (here, named simply "walk"). It's not a pixel scale. This may stay still:
    walk = 1
 
    def screenlength(k):
        """
        This is a function to make the image good to see (without it would result in a partial image).
        This will guarantee that we can see the the voids and it's steps.
        """
        if k != 0:
            length = screenlength(k-1)
            return 2*length + 1
        else: return 0
