function s = cubicspline(x, y, zi, type, der)
% CUBICSPLINE Computes a cubic spline
% S=CUBICSPLINE (X,Y,ZI) computes the value at the
% abscissae ZI of the natural interpolating cubic
% spline that interpolates the values Y at the nodes X.
% S=CUBICSPLINE (X,Y,ZI ,TYPE ,DER) if TYPE = 0 computes the
% values at the abscissae ZI of the cubic spline
% interpolating the values Y with first derivative at
% the endpoints equal to the values DER (1) and DER (2).
% If TYPE =1 the values DER (1) and DER (2) are
% the second derivative at the endpoints.
[n,m]= size (x);
if n == 1
    x = x'; y = y'; n = m;
end
if nargin == 3
    der0 = 0; dern = 0; type = 1;
else
    der0 = der (1); dern = der (2);
end
h = x(2: end) - x(1:end -1);
e = 2*[h(1); h(1:end -1) + h(2: end); h(end)];
A = spdiags([[h; 0] e [0; h]], -1:1, n, n);
d = (y(2: end)-y(1:end -1))./h;
rhs = 3*(d(2: end)-d(1:end -1));
if type == 0
    A(1,1) = 2*h(1); A(1,2) = h(1);
    A(n,n) = 2*h(end); A(end ,end -1) = h(end);
    rhs = [3*( d(1)- der0 ); rhs; 3*(dern -d(end ))];
else
    A(1,:) = 0; A(1,1) = 1;
    A(n,:) = 0; A(n,n) = 1;
    rhs = [der0 ; rhs; dern];
end
