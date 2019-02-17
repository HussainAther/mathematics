
def verifyFactor(I, S, H):
    """
    Checks solutinos to computational problems. It takes three strings: I instance of the problem,
    S the proposed soultion, and H a hint.
    """
    if S == "no":
        return "unsure"
    M = int(I)
    m = int(S)
    if m >= 2 and
