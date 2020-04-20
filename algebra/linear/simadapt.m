function [JSf ,nodes] = simpadpt(f, a, b, tol, hmin, varargin)
%SIMPADPT Adaptive Simpson quadrature formula
% JSF = SIMPADPT (FUN ,A,B,TOL ,HMIN ) tries to approximate
% the integral of function FUN from A to B within
% error TOL using recursive adaptive Simpson
% quadrature with H>= HMIN . The function FUN should
% accept a vector argument x and return a vector.
% FUN can be either an inline function , an anonymous
% function , or it can be defined by an external m-file.
% JSF = SIMPADPT(FUN, A, B, TOL, HMIN, P1, P2,...) calls the
% function FUN passing the optional parameters
% P1 ,P2 ,... as FUN(X,P1 ,P2 ,...).
% [JSF ,NODES] = SIMPADPT (...) returns the distribution
% of nodes used in the quadrature process.
