import pandas as pd
import numpy as np

"""
Suppose we want to generate samples from a fair six-sided die. Our workhouse uniform random variable is defined continuously
over the unit interval and the fair six-sided die is discrete. We must first create a mapping between the continuous random
variable u and the discrete outcomes of the die. Each individual segment is assigned to one of the die outcomes. For example,
if u ∈ [1/6, 2/6), then the outcome for the die is 2. Because the die is fair, all segments on the unit interval are the same
length. Thus, our new random variable v is derived from u by this assignment.
"""

u = np.random.rand(100)
df = pd.DataFrame(data=u,columns=["u"])


