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
