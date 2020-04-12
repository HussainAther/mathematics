function [xh, yh, uh, error] = poissonfd (a, b, c, d, nx, ny,...
                                          fun, bound, uex, varargin)
%POISSONFD two-dimensional Poisson solver
% [XH, YH, UH] = POISSONFD(A, B, C, D, NX, NY, FUN, BOUND) solves
% by the five-point finite difference scheme the
% problem -LAPL (U) = FUN in the rectangle (A,B)X(C,D)
% with Dirichlet boundary conditions U(X,Y)= BOUND(X,Y)
% at any (X,Y) on the boundary of the rectangle .
% [XH ,YH ,UH ,ERROR]= POISSONFD (A, B, C, D, NX, NY, FUN,...
% BOUND ,UEX) computes also the maximum nodal error
% ERROR with respect to the exact solution UEX.
% FUN ,BOUND and UEX can be inline functions , anonymous
% functions , or functions defined in M-files.
% [XH, YH, UH, ERROR] = POISSONFD (A, B, C, D, NX, NY, FUN,...
% BOUND, UEX, P1, P2,...) passes the optional arguments
% P1, P2,... to the functions FUN, BOUND, UEX.
if nargin == 8
    uex = inline('0','x','y');
end
nx1 = nx +2; ny1=ny +2; dim = nx1*ny1;
hx = (b-a)/( nx +1); hy = (d-c)/(ny +1);
    hx2 = hx ^2; hy2 = hy ^2;
kii = 2/ hx2 +2/ hy2; kix = -1/hx2; kiy = -1/hy2;
K = speye(dim ,dim); rhs = zeros(dim ,1);
y = c;
for m = 2:ny+1
    x = a; y = y + hy;
    for n = 2:nx+1
        i = n+(m -1)* nx1; x = x + hx;
        rhs(i) = feval(fun ,x,y,varargin {:});
        K(i,i) = kii; K(i,i-1) = kix; K(i,i+1) = kix;
        K(i,i+nx1) = kiy; K(i,i-nx1) = kiy;
    end
end
