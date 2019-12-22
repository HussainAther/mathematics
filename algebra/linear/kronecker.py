"""
Kronecker product one-liner
"""

def kp(m1, m2):
    """
    For matrices m1 and m2, calculate the Kronecker
    product.
    """
    return [[n1 * n2 for n1 in elem2 for n2 in m2[row]] for elem1 in m2 for row in range(len(m2))]
