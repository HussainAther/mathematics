function [xh ,uh] = bvp(a, b, N, mu, eta, sigma, bvpfun,...
                        ua, ub, varargin )
%BVP Solves two-point boundary value problems.
% [XH ,UH] = BVP(A, B, N, MU, ETA, SIGMA, BVPFUN, UA, UB)
% solves the boundary-value problem
% -MU*D(DU/DX)/DX+ETA*DU/DX+SIGMA*U=BVPFUN
% on the interval (A,B) with boundary conditions
% U(A)= UA and U(B)=UB , by the centered finite
% difference method at N equispaced nodes
% internal to (A,B). BVPFUN can be an inline
% function , an anonymous function or a function
% defined in a M-file.
% [XH ,UH ]=BVP(A,B,N,MU ,ETA ,SIGMA ,BVPFUN ,UA ,UB ,...
% P1 ,P2 ,...) passes the additional parameters
% P1 , P2 , ... to the function BVPFUN.
% XH contains the nodes of the discretization ,
% including the boundary nodes.
% UH contains the numerical solutions .
h = (b-a)/(N+1);
xh = (linspace (a,b,N+2))';
hm = mu/h^2;
hd = eta /(2* h);
e = ones (N ,1);
A = spdiags([-hm*e-hd (2* hm+sigma)*e -hm*e+hd ],...
             -1:1, N, N);
xi = xh (2:end -1);
f = feval(bvpfun ,xi ,varargin {:});
f(1) = f(1)+ ua*(hm+hd );
f(end) = f(end )+ub*(hm -hd);
uh = A\f;
uh = [ua; uh; ub];
return
