close all
% Poisson Gauss–Seidel (GS gauss seidel) iteration

% Set number of iterations to be performed
nk = 300

% Set parameters alpha and beta
alpha = 2;
beta  = 3;

% Set the number of meshpoints so the interior has N x N such points
N = 50;

% Compute the distance between mesh points, in each direction
h = 1/(N+1);

% We will have arrays that capture the boundary as well as the interior
% meshpoints.  As a result, we need those arrays to be of size (N+2) x
% (N+2) so that those indexed 2:N+1, 2:N+1 represent the interior.  

% Compute the x-values at each point i,j, including the boundary
x = h * [ 0:N+1 ];   % Notice this creates a row vector

% Compute the y-values at each point i,j, including the boundary
y = h * [ 0:N+1 ];   % Notice this creates a row vector

% Create an array that captures the load at each point i,j
for i=1:N+2
    for j=1:N+2
        F( i,j ) = ...
            ( alpha^2 + beta^2 ) * pi^2 * sin( alpha * pi * x( i ) ) * sin( beta * pi * y( j ) );
    end
end

% Set the initial values at the mesh points
U = zeros( N+2, N+2 );

% Perform nk iterations
for k = 1:nk
    k           % print current iteration index
    
    % update all the interior points
    for i=2:N+1
        for j=2:N+1
            U( i,j ) = ( U( i, j-1 ) + U( i-1, j ) + U( i+1, j ) + U( i, j+1 ) + h^2 * F( i, j ) ) / 4;
        end
    end 
    mesh( x, y, U );
    axis( [ 0 1 0 1 -1.5 1.5 ]);
    
    % wait to continue to the next iteration
    next = input( 'press RETURN to continue' );
end

