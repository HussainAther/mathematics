import numpy as np


"""
We use coemission probability to compute the L2-distance between the probability distributions
of two Markov models.

When using a profile hidden Markov model, it is sometimes sufficient just to focus on the most probable path through the model,
e.g. when using a profile hidden Markov model to generate alignments. It is, however, well known that profile hidden Markov models
possess a lot more information than the most probable paths, as they allow the generation of an infinity of sequences, each by a multitude of paths.

Thus, when comparing two profile hidden Markov models, one should look at the entire spectrum of sequences and probabilities.
The probability two profile hidden Markov models independently generate the same sequence, we compute the co-emission probability:

the summation over PM1(s) * PM2 (s)

in which PM1 and PM2 are the probabilities for either model to produce a sequence s.
"""

def coemission(m1, m2):
    """
    Return the co-emission probability for models m1 and m2.
    """
    return np.inner(m1, m2)



def angle(m1, m2):
    """
    Return the angle between two hidden Markov Models m1 and m2.
    """
    num = coemission(m1, m2)
    den = coemission(np.sqrt((m1, m2)*(np.sqrt(m2,m2))))
    return np.arccos(num/den)
