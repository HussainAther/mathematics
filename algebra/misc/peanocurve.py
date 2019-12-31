import inspect
import turtle as tt

"""
Peano curve.
"""

stack = [] # Mark the current stacks in run.
def peano(iterations=1):
    global stack
