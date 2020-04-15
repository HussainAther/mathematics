function [t,u] = cranknic(odefun, tspan, y0, Nh, varargin)
% CRANKNIC Solves differential
% [T,Y]= CRANKNIC (ODEFUN ,TSPAN ,Y0 ,NH) with
% TSPAN=[T0 ,TF] integrates the system of differential
% equations y'=f(t,y) from time T0 to TF with initial
% condition Y0 using the Crank -Nicolson method on an
% equispaced grid of NH intervals.
% Function ODEFUN(T,Y) must return a vector , whose
% elements hold the evaluation of f(t,y), of the
% same dimension of Y.
% Each row in the solution array Y corresponds to a
% time returned in the column vector T.
% [T,Y] = CRANKNIC (ODEFUN, TSPAN, Y0, NH, P1, P2,...)
% passes the additional parameters P1, P2,... to the
% function ODEFUN as ODEFUN(T,Y,P1 ,P2 ...).
tt=linspace (tspan(1), tspan(2), Nh +1);
