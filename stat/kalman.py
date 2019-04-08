from numpy import dot

"""
The Kalman filter estimates the state of x of a discrete-time controlled process
governed by the linear stochastic difference equation.
"""

def kf_predict(X, P, A, Q, B, U):
 X = dot(A, X) + dot(B, U)
 P = dot(A, dot(P, A.T)) + Q
 return(X,P) 
