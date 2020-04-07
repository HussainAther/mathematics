% Numerical solution of Neumann boundary-value problem
function [xh ,uh] = neumann(a,b,N,mu ,eta ,sigma ,bvpfun ,...
                    ua ,ub ,varargin )
h = (b-a)/(N+1); xh = (linspace (a,b,N+2)) ’;
hm = mu/h^2; hd = eta /(2* h); e =ones (N+2 ,1);
A = spdiags ([-hm*e-hd (2* hm+sigma)*e -hm*e+hd ],...
    -1:1, N+2, N+2);
A(1 ,1)=3/(2*h); A(1 ,2)= -2/h; A(1 ,3)=1/(2*h); f(1)= ua;
A(N+2,N+2)=3/(2* h); A(N+2,N+1)= -2/ h; A(N+2,N)=1/(2*h);
f =feval(bvpfun ,xh ,varargin {:}); f(1)= ua; f(N+2)= ub;
uh = A\f;
