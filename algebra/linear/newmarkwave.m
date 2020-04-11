function [xh ,uh] = newmarkwave(xspan, tspan, nstep, param, ...
                                c, u0, v0, g, f, varargin)
%NEWMARKWAVE solves the wave equation with the Newmark
% method.
% [XH ,UH ]= NEWMARKWAVE (XSPAN ,TSPAN ,NSTEP ,PARAM ,C,...
% U0,V0,G,F)
% solves the wave equation D^2 U/DT ^2 - C D^2U/DX ^2 = F
% in (XSPAN(1), XSPAN (2)) X (TSPAN(1), TSPAN (2)) using
% Newmark method with initial conditions U(X,0)= U0(X),
% DU/DX(X ,0)= V0(X) and Dirichlet boundary conditions
% U(X,T)=G(X,T) for X=
% positive constant.
% NSTEP (1) is the number of space-integration intervals.
% NSTEP (2) is the number of time-integration intervals.
% PARAM (1)= ZETA and PARAM (2)= THETA.
% U0(X), V0(X), G(X,T) and F(x,T) can be defined
% by inline functions , anonymous functions , or
% M-files.
% XH contains the nodes of the discretization .
% UH contains the numerical solutions at time TSPAN (2).
% [XH ,UH ]= NEWMARKWAVE (XSPAN ,TSPAN ,NSTEP ,PARAM ,C,...
% U0 ,V0 ,G,F,P1 ,P2 ,...) passes the additional parameters
% P1 ,P2 ,... to the functions U0 ,V0 ,G,F.
