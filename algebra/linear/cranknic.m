function [t,u] = cranknic(odefun, tspan, y0, Nh, varargin)
% CRANKNIC Solves differential
% [T,Y]= CRANKNIC (ODEFUN ,TSPAN ,Y0 ,NH) with
% TSPAN=[T0 ,TF] integrates the system of differential
% equations y'=f(t,y) from time T0 to TF with initial
% condition Y0 using the Crank -Nicolson method on an
% equispaced grid of NH intervals.
% Function ODEFUN(T,Y) must return a
