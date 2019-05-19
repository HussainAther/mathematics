"""
Fibonacci series using recursion.
"""

def fib(n): 
    """
    Nth term of Fibonacci.
    """
    if n <= 1: 
        return n 
    return fib(n - 1) + fib(n - 2) 
