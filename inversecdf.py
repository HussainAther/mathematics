import pandas as pd
import numpy as np

"""
Inverse cumulative distribution function

Suppose we want to generate samples from a fair six-sided die. Our workhouse uniform random variable is defined continuously
over the unit interval and the fair six-sided die is discrete. We must first create a mapping between the continuous random
variable u and the discrete outcomes of the die. Each individual segment is assigned to one of the die outcomes. For example,
if u ∈ [1/6, 2/6), then the outcome for the die is 2. Because the die is fair, all segments on the unit interval are the same
length. Thus, our new random variable v is derived from u by this assignment.
"""

u = np.random.rand(100)
df = pd.DataFrame(data=u,columns=["u"])

labels = [1,2,3,4,5,6]
df["v"]=pd.cut(df.u,np.linspace(0,1,7), include_lowest=True,labels=labels)

df.head()

df.groupby("v").count()
