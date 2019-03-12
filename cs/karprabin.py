
"""
The Karp-Rabin algorithm matches a pattern to a string, the basic principle of database search.

It computes scores of the substrings against the main string. It compares each position of the
substrings against the main string.
"""

def kr(p, t, q):
    """
    Search for patterns p within a string t for some prime number q.
    """
    i = 0
    j = 0
    p = 0    # hash value for pattern
    t = 0    # hash value for txt
    h = 1

    for i in range(len(pat)-1):
        h = (h * d)% q
