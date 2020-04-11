function [xh ,uh] = bvp(a, b, N, mu, eta, sigma, bvpfun,...
                        ua, ub, varargin )
%BVP Solves two -point boundary value problems .
% [XH ,UH ]=BVP(A,B,N,MU ,ETA ,SIGMA ,BVPFUN ,UA ,UB)
% solves the boundary -value problem
% -MU*D(DU/DX)/DX+ETA*DU/DX+SIGMA*U=BVPFUN
% on the interval (A,B) with boundary conditions
% U(A)= UA and U(B)=UB , by the centered finite
% difference method at N equispaced nodes
% internal to (A,B). BVPFUN can be an inline
% function , an anonymous function or a function
% defined in a M-file .
