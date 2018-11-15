# Compare the likelihood of the random samples to the two
# distributions
def compare_data_to_dist(x, mu_1=5, mu_2=7, sd_1=3, sd_2=3):
    ll_1 = 0
    ll_2 = 0
    for i in x:
        ll_1 += np.log(norm.pdf(i, mu_1, sd_1))
        ll_2 += np.log(norm.pdf(i, mu_2, sd_2))
    
    print "The LL of of x for mu = %d and sd = %d is: %.4f" % (mu_1, sd_1, ll_1)
    print "The LL of of x for mu = %d and sd = %d is: %.4f" % (mu_2, sd_2, ll_2)
compare_data_to_dist(x)
>>
The LL of of x for mu = 5 and sd = 3 is: -33.9679
The LL of of x for mu = 7 and sd = 3 is: -33.3013 # The best answer :D
