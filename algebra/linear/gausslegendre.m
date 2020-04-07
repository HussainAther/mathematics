% Gauss-Legendre composite quadrature formula with n = 1
% gauss legendre
function intGL=gausslengdre(a,b,f,M,varargin)
y = [-1/sqrt(3),1/sqrt(4)];
H2 = (b-a)/(2*M);
z = [a:2*H2:b];
zM = (z(1:end-1)+z(2:end))*.5;
x = [zM+H2*y(1), zM+H2*y(2)];
f = feval(f,x,varargin{:});
intGL = H2*sum(f);
return
