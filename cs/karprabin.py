
"""
The Karp-Rabin algorithm matches a pattern to a string, the basic principle of database search.

It computes scores of the substrings against the main string
"""


def search(pat, txt, q):
    M = len(pat)
    N = len(txt)
    i = 0
    j = 0
    p = 0    # hash value for pattern
    t = 0    # hash value for txt
    h = 1
  

