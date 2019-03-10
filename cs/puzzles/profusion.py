
"""
Having solved the 8-queens problem, we turn our attention to solving the N-queens
problem for arbitrary N. That is, we need to place N queens on an N × N board such that
no pair of queens attack each other.

Let’s now assume that we are not allowed to write nested for loops (or other types of
loops) that have a degree of nesting more than 2. You might say that this is an artificial
constraint, but not only is the deeply nested 8-queens code aesthetically displeasing, but
the code is also not general. If you wanted to write a program to solve the N-queens
problem for N up to say 20, you would have to write functions to solve 4-queens (with 4
nested loops), 5-queens (with 5 nested loops), all the way to 20-queens (with 20 nested
loops!), and invoke the appropriate function depending on the actual value of N when the
code is run. What happens if you then want a solution to the 21-queens problem?

We will need to use recursion to solve the general N-queens problem. Recursion occurs
when something is defined in terms of itself. The most common application of recursion
in programming is where a function being defined is applied within its own definition.

In Python a function can call itself. If a function calls itself, it is called a recursive
function. Recursion may also correspond to a function A calling a function B, which in
turn calls function A. We’ll focus on the simple case of recursion here, namely a function
f calling f again. 
"""
