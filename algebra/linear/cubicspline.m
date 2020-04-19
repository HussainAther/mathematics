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
