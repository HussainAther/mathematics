"""
Performs complex algebra with dummy information
"""

class Complex:
    def __init__(z, x, y):
        z.re = x # real component
        z.im = y # imaginary

    def addt(z1, z2): # add z1 + z2
        return Complex(z1.re + z2.re, z1.im, z2.im)

    def subt(z1, z2): # subtract
