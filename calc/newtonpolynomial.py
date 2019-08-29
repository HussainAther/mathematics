import scipy.linalg as sl

class NewtonPolynomial(PolyNomial):
    """
    Newton polynomial.
    """
    def __init__(self, **args):
        if "coeff" in args:
            try:
                self.xi = array(args["xi"])
            except KeyError:
                raise ValueError("Coefficients need to be given together" \
                                 "with abscissae values xi.")
                super(NewtonPolynomial, self).__init__(**args)
