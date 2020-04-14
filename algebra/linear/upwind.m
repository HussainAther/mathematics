function [xh ,th ,uh] = hyper(xspan, tspan, u0, ul,... 
                              scheme, cfl, deltax, deltat)
% HYPER solves hyperbolic scalar equations 
% with Lax-Friedrichs, Lax-Wendroff, upwind (lax friendrichs lax wnendroff)
% [XH ,TH ,UH]= HYPER(XSPAN ,TSPAN ,U0 ,UL ,SCHEME ,CFL ,...
% DELTAX ,DELTAT)
