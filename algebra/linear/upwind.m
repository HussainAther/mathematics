function [xh ,th ,uh] = hyper(xspan, tspan, u0, ul,... 
                              scheme, cfl, deltax, deltat)
% HYPER solves hyperbolic scalar equations 
% with Lax-Friedrichs, Lax-Wendroff, upwind (lax friendrichs lax wnendroff)
% [XH ,TH ,UH]= HYPER(XSPAN ,TSPAN ,U0 ,UL ,SCHEME ,CFL ,...
% DELTAX ,DELTAT)
% solves the hyperbolic scalar equation
% DU/DT+ A * DU/DX=0
% in (XSPAN(1), XSPAN (2)) x(TSPAN(1), TSPAN (2))
% with A>0, initial condition U(X ,0)= U0(X) and
% boundary condition U(T)=UL(T) given at XSPAN
% with several finite difference schemes .
% scheme = 1 Lax - Friedrichs
%          2 Lax - Wendroff
%          3 Upwind
