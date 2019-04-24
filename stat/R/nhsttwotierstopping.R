"We use Null Hypothesis Significance Testing (NHST). Suppose an experimenter plans to collect data based on a two-tier stopping criterion. The experimenter will"
"collect an initial batch of data with N = 30 and then do a NHST. If the result is not significant, then an"
"additional 15 subjects’ data will be collected, for a total N of 45. Suppose the researcher intends to use the"
"standard critical values for determining significance at both the N = 30 and N = 45 stages. Our goal is determine"
"the actual false-alarm rate for this two-stage procedure, and to ponder what the mere intention of doing a second"
"phase implies for interpreting the first stage, even if data collection stops with the first stage."

N1 = 30 # Number of flips for first test.
N2 = 15 # Number of _additional_ flips for second test.

theta = .5 # Hypothesized bias of coin.
FAmax = .05 # False Alarm maximum for a single test.
NT = N1 + N2 # Total number of flips.

# Determine critical values for N1.
loCritN1 = (0:N1)[max(which(cumsum(dbinom(0:N1,N1,theta)) <= FAmax/2))]
hiCritN1 = (N1:0)[max(which(cumsum(dbinom(N1:0,N1,theta)) <= FAmax/2))]
