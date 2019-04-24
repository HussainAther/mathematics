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

# Compute actual false alarm rate for those critical values.
FA1 = sum((0:N1 <= loCritN1 | 0:N1 >= hiCritN1) * dbinom(0:N1, N1, theta))
cat("N1:", N1, ", lo:", loCritN1, ", hi:",hiCritN1, ", FA:", FA1, "\n")

# Determine critical values for NT.
loCritNT = (0:NT)[max(which(cumsum(dbinom(0:NT,NT,theta)) <= FAmax/2))]
hiCritNT = (NT:0)[max(which(cumsum(dbinom(NT:0,NT,theta)) <= FAmax/2))]

# Compute actual false alarm rate for those critical values.
FAT = sum((0:NT <= loCritNT | 0:NT >= hiCritNT) * dbinom(0:NT, NT,theta))
cat("NT:", NT, ", lo:", loCritNT, ", hi:", hiCritNT, ", FA:", FAT, "\n")

# Determine actual false alarm rate for the two-tier test.
Z1mat = matrix(0:N1, nrow=N2+1, ncol=N1+1, byrow=TRUE)
ZTmat = outer(0:N2, 0:N1, "+")
pZTmat = outer(dbinom(0:N2, N2, theta), dbinom(0:N1, N1, theta))

FA1or2 = sum(((ZTmat <= loCritNT | ZTmat >= hiCritNT) # double dagger matrix
            | (Z1mat <= loCritN1 | Z1mat >= hiCritNT) # single dagger matrix
            ) * pZTmat)

cat( "Two tier FA:" , FA1or2 , "\n" )
