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
% with several finite difference schemes.
% scheme = 1 Lax - Friedrichs
%          2 Lax - Wendroff
%          3 Upwind
% The propagation velocity 'a' is not required as
% input of the function, since it can be derived
% from CFL = A * DELTAT / DELTAX
% Output: XH is the vector of space nodes
% TH is the vector of time nodes
% UH is a matrix containing the computed solution
% UH(n,:) contains the solution at time TT(n)
% U0 and UL can be either inline , anonymous
% functions or functions defined by M-file.
