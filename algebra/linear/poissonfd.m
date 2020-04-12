function [xh, yh, uh, error] = poissonfd (a, b, c, d, nx, ny,...
                                          fun, bound, uex, varargin)
%POISSONFD two-dimensional Poisson solver
% [XH, YH, UH] = POISSONFD(A, B, C, D, NX, NY, FUN, BOUND) solves
% by the five-point finite difference scheme the
% problem -LAPL (U) = FUN in the rectangle (A,B)X(C,D)
