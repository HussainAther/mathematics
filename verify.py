"""
Complexity classes in computer science have varying times in finding solutions. Verifying that
solutions exist exist in complexity classes.
"""

def verifyFactor(I, S, H):
    """
    Checks solutinos to computational problems. It takes three strings: I instance of the problem,
    S the proposed soultion, and H a hint.
    """
    if S == "no":
        return "unsure"
    M = int(I)
    m = int(S)
    if m >= 2 and m < M and M % m == 0:
        # m is a nontrivial factor of M
        return "correct"
    else:
        # m is nontrivial
        return "unsure"

"""
In the next example uses the hint H to work in a reasonable amount of time. Decision variant of TSP, which originally takes
an undirected, weighted graph G and outputs a solution of the shortest Hamilton cycle of G (or "no" if none exists).
"""

def verifyTspD(I, S, H):
    if S == "no":
        return "unsure"
    # extract G, L, and I and convert to correct data types
    (G, L) = I.split(";")

    # split the hint string into a list of verticies, which will
    # form a Hamilton cycle of length at most L, if the hint is correct
    cycle = Path(H.split(","))

    # verify the hint is a Hamilton cycle, and has length at most L
    if G.isHamiltonCycle(cycle) and G.cycleLength(cycle) <= L:
        return "correct"
    else:
        return "unsure"
