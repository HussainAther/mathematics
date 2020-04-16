% Apply Jacob's method to Seidel matrix
rng(0)

m = 5

% Create a symmetric m x m matrix.
A = rand( m,m );
A = tril( A ) + tril( A,-1)';

% Remember the original matrix.
Aold = A;
disp( A );
disp( 'Every time the matrix is displayed, pick the i and j entry you want to zero' );
disp( 'i = -1 means: leave the loop' );

