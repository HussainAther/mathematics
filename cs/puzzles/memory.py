"""
Here’s a cute coin row game that corresponds to an optimization problem. We have a set
of coins in a row all with positive values. We need to pick a subset of the coins to
maximize their sum, but with the additional constraint that we are not allowed to pick two
adjacent coins.

Given:

14    3    27    4    5    15    1

You should pick 14, skip 3, pick 27, skip 4 and 5, pick 15 and skip 1. This gives a total of
56, which is optimal. Note that alternately picking and skipping coins does not work for
this example (or in general). If we picked 14, 27, 5 and 1, we would only get 47. And if
we picked 3, 4, and 15, we would get a pathetic score of 22.

Can you find the maximum value for the coin row problem below?

3    15    17    23    11   3    4    5    17    23    34    17    18    14    12    15
"""
