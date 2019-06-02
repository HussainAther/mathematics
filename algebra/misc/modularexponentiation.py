"""
Modular exponentiation is a type of exponentiation 
performed over a modulus. It is useful in computer science, 
especially in the field of public-key cryptography.
"""

def modularExponential(base, power, mod):
    """
    For a base, power, and modulus, perform modular
    exponentiation.
    """
    if power < 0:
        return -1
    base %= mod
    result = 1
    while power > 0:
        if power & 1:
            result = (result * base) % mod
	power = power >> 1
	base = (base * base) % mod
    return result
