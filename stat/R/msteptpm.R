# m-step Transition Probability Matrix Computation
# The m-step transition probability matrix computation is provided in this function. The equation is based on the well-known "Chapman-Kolmogorov equation".
msteptpm <-
function(TPM,m){
  if(m==1) return(TPM) else {
    temp <- TPM
    for(i in 1:(m-1)) temp=temp%*%TPM
    return(temp)
  }
}
