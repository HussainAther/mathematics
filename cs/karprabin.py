
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

    for i in range(len(p)-1):
        h = (h * d)% q
    
    for i in range(len(p)):
        p = (d * p + ord(p[i]))% q
        t = (d * t + ord(t[i]))% q

    for i in range(len(t) - len(p) + 1):
        if p == t:
            for j in range(len(p)):
                if t[i + j] != p[j]:
                    break
