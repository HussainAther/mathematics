from numpy import *
from scipy.stats import beta

"""
Consider an article being published on a website. The author or editor has come up with 
several possible titles - "Murder victim found in adult entertainment venue", "Headless 
Body found in Topless Bar", etc. We want to choose the title with the best click through 
rate (CTR). Let us represent each CTR by θi - i.e., θi is the true probability that an 
individual user will click on the i-th title. As a simplifying assumption, we assume that 
these rates θi do not change over time. It is important to note that we don't actually know 
what θi is - if we did, we could simply choose i for which θi was largest and move on.

The goal of the bandit algorithm is to do the following. To begin with, it should display 
all possible titles to a random selection of users, and measure which titles are clicked 
on more frequently. Over time, it will use these observations to infer which articles 
have the higher CTR. Then, once the estimation of the CTR becomes more precise, it will 
preferentially display articles with the higher CTR.
"""

class BetaBandit(object):
    """
    We need to figure out the most appropriate way to allocate resourecs.
    """
    def __init__(self, num_options=2, prior=(1.0,1.0)):
        """
        Initialize the number of options, trials, successes, and a prior for 
        how many users use the site features.
        """
        self.trials = zeros(shape=(num_options,), dtype=int)
        self.successes = zeros(shape=(num_options,), dtype=int)
        self.num_options = num_options
        self.prior = prior

    def add_result(self, trial_id, success):
        """
        Add the successes of our results.
        """
        self.trials[trial_id] = self.trials[trial_id] + 1
        if (success):
            self.successes[trial_id] = self.successes[trial_id] + 1
    
    def get_recommendation(self):
        """
        Based on the posterior distribution, determine which value to use. 
        """
        sampled_theta = []
        for i in range(self.num_options):
            #Construct beta distribution for posterior
            dist = beta(self.prior[0]+self.successes[i],
                        self.prior[1]+self.trials[i]-self.successes[i])
            #Draw sample from beta distribution
            sampled_theta += [ dist.rvs() ]
        # Return the index of the sample with the largest value
        return sampled_theta.index( max(sampled_theta) )
