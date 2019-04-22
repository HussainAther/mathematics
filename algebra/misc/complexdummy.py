"""
Performs complex algebra with dummy information. Because reasons.
"""

class Complex:
    def __init__(z, x, y):
        z.re = x # real component
        z.im = y # imaginary

    def addt(z1, z2): 
        """
        Add two complex vectors
        """
        return Complex(z1.re + z2.re, z1.im, z2.im)

    def subt(z1, z2): 
        """
        Subtract two complex vectors
        """
        return Complex(z1.re - z2.re, z1.im - z2.im)
    
    def mult(z1, z2):
	"""
	Multiply
	"""
        return Complex(z1.re * z1.re - z1.im * z2.im, z1.re * z2.im + z1.im * z2.re)

    def __repr__(z): # convert to string for printing
	"""
	Convert to string
	"""
        return "(%f, %f) " %(z.re, z.im)

print("Operations with two complex numbers\n")

# Print the complex numbers
z1 = Complex(2.0, 3.0)
print("z1=", z1)
z2 = Complex(4.0, 6.0)
print("z2=", z2)
z3 = Complex.addt(z1, z2) # add em up!
print("z1 + z2= ", z3)
print("z1 - z2=", Complex.subt(z1, z2))
print("z1 * z2=", Complex.mult(z1, z2))
print("Enter and return any character to quit")
s = raw.input()
