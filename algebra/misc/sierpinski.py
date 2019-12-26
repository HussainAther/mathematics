def st(n):
    """
    Print a Sierpinski triangle of rows n.
    """
    d = ["*"]
    for i in range(n):
        sp = " " * (2**i)
        d = [sp+x+sp for x in d] + [x + " " + x for x in d]

