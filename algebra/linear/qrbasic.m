function D = qrbasic(A, tol, nmax)
% QRBASIC computes all the eigenvalues of a matrix A.
% D=QRBASIC (A,TOL ,NMAX ) computes by QR iterations all
% the eigenvalues of A within a tolerance TOL and a
% maximum number of iteration NMAX. The convergence of
% this method is not always guaranteed.
[n, m] = size(A);
if n ~= m, error('The matrix must be squared'); end
T = A; niter = 0; test = norm(tril (A,-1), inf);
while niter <= nmax & test >= tol
    [Q,R] = qr(T); T = R*Q;
