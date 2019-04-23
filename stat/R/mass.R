"Glass fragment data.
The goal is to predict the variable type from the others. Note that 
type takes 6 different values. First combine the first three classes 
(different types of window glass) and the last three classes so that type
now only has two values. Classify the data (window or not window) 
using (i) linear regression, (ii) logistic regression, and (iii) lda 
(using the function lda()). Compare the results."
library(MASS)
data(fgl)
help(fgl)
