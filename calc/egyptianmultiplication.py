"""
We use ancient Egyptian (Ancient egyptian) multiplication (or Ethiopian ethiopian 
Russian russian peasant) as scribes used as a systematic method to multiply two
numbers without a multiplication table. We are only able to multiply and divide
by 2 and add.

We will take two numbers to be multiplied and write them down at the top of two columns.I n the left-hand column 
repeatedly halve the last number, discarding any remainders, and write the result below the last in the same column, 
until you write a value of 1. In the right-hand column repeatedly double the last number and write the result below. 
stop when you add a result in the same row as where the left hand column shows 1. Examine the table produced and 
discard any row where the value in the left column is even. Sum the values in the right-hand column that remain 
to produce the result of multiplying the original two numbers together. 

We'll use lambda functions for defining these methods.
"""

halve  = lambda x: x // 2
double = lambda x: x*2
even   = lambda x: not x % 2
