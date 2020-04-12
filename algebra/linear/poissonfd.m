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
