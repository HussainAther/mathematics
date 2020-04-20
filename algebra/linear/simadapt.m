function [JSf ,nodes] = simpadpt(f, a, b, tol, hmin, varargin)
%SIMPADPT Adaptive Simpson quadrature formula
% JSF = SIMPADPT (FUN ,A,B,TOL ,HMIN ) tries to approximate
% the integral of function FUN from A to B within
% error TOL using recursive adaptive Simpson
% quadrature with H>= HMIN . The function FUN should
% accept a vector argument x and return a vector.
% FUN can be either an inline function , an anonymous
% function , or it can be defined by an external m-file.
% JSF = SIMPADPT(FUN, A, B, TOL, HMIN, P1, P2,...) calls the
% function FUN passing the optional parameters
% P1 ,P2 ,... as FUN(X,P1 ,P2 ,...).
% [JSF ,NODES] = SIMPADPT (...) returns the distribution
% of nodes used in the quadrature process.
A=[a,b]; N=[]; S=[]; JSf = 0; ba = 2*(b - a); nodes =[];
while ~isempty(A),
    [deltaI ,ISc ]=caldeltai (A,f,varargin {:});
    if abs(deltaI) < 15* tol *(A(2)-A(1))/ba;
        JSf = JSf + ISc; S = union(S,A);
        nodes = [nodes , A(1) (A(1)+ A(2))*0.5 A(2)];
        S = [S(1), S(end)]; A = N; N = [];
    elseif A(2)-A(1) < hmin
        JSf=JSf+ISc; S = union(S,A);
        S = [S(1), S(end)]; A=N; N=[];
        warning('Too small integration -step ');
    else
        Am = (A(1)+ A(2))*0.5;
        A = [A(1) Am]; N = [Am, b];
    end
end
nodes=unique(nodes);
return

function [deltaI, ISc]= caldeltai (A, f, varargin)
L=A(2)-A(1);
t=[0; 0.25; 0.5; 0.75; 1];
x=L*t+A(1); L=L/6;
w=[1; 4; 1]; wp =[1;4;2;4;1];
fx=feval(f,x,varargin {:}).* ones (5 ,1);
IS=L*sum(fx([1 3 5]).*w);
ISc =0.5*L*sum(fx.*wp);
deltaI=IS -ISc;
return
