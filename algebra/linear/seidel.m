% Apply Jacob's method to Seidel matrix
rng(0)

m = 5

% Create a symmetric m x m matrix.
A = rand( m,m );
A = tril( A ) + tril( A,-1)';

% Remember the original matrix.
Aold = A;
