function Imp = midpointc(a, b, M, f, varargin)
%MIDPOINTC Composite midpoint numerical integration.
% IMP = MIDPOINTC (A,B,M,FUN) computes an approximation
% of the integral of the function FUN via the midpoint
% method (with M equal subintervals ). FUN accepts a
% real vector input x and returns a real vector value.
% FUN can be either an inline function , an anonymous
% function , or it can be defined by an external m-file.
% IMP=MIDPOINT (A,B,M,FUN ,P1 ,P2 ,...) calls the function
% FUN passing the optional parameters P1 ,P2 ,... as
% FUN(X,P1 ,P2 ,...).
