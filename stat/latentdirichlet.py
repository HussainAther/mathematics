import pandas as pd
import numpy as np

"""
In the area of topic modeling, we use latent dirichlet allocation (lda) to classify
text in a document about a specific topic. We build a topic-per-document model and
words-per-topic model using Dirichlet distributions.
"""

# read in the data of news headliens from the .csv file
data = pd.read_csv('abcnews-date-text.csv', error_bad_lines=False)
