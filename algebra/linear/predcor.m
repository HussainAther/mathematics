function [t,u] = predcor(odefun, tspan, y, Nh ,...
                        predictor, corrector, varargin )
%PREDCOR Solves differential equations using a
% predictor -corrector method
% [T,Y]= PREDCOR (ODEFUN ,TSPAN ,Y0 ,NH ,PRED ,CORR ) with
% TSPAN=[T0 TF] integrates the system of differential
% equations y’ = f(t,y) from time T0 to TF with
% initial condition Y0 using a general predictor
% corrector method on an equispaced grid of NH steps.
% Function ODEFUN(T,Y) must return a vector , whose
% elements hold the evaluation of f(t,y), of the
% same dimension of Y.
% Each row in the solution array Y corresponds to a
% time returned in the column vector T.
% [T,Y]= PREDCOR (ODEFUN ,TSPAN ,Y0 ,NH ,PRED ,CORR ,P1 ,..)
% passes the additional parameters P1 ,... to the
% functions ODEFUN ,PRED and CORR as ODEFUN(T,Y,P1 ,..),
% PRED (T,Y,P1 ,P2 ...), CORR
h = (tspan(2)-tspan(1))/Nh;
y = y0(:); w=y; u=y.';
tt = linspace(tspan(1), tspan(2), Nh+1);
