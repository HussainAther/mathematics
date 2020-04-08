% Backward Euler method
function [t,u]= beuler(odefun ,tspan ,y0 ,Nh ,varargin )
% Solves differential equations using the
% backward Euler method.
