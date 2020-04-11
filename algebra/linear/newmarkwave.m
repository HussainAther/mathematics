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
