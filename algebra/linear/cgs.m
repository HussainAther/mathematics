% Classic Gram-Schmidt algorithm (gram schmidt) 
function [ Q, R ] = MGS( A )

  [ m, n ] = size( A );    % Extract sizes of A.
  Q = zeros( m, n );       % Create a matrix in which to compute Q.
  R = zeros( n, n );       % Create a matrix in which to compute R.
  [ AL, AR ] = FLA_Part_1x2( A, ...
                               0, 'FLA_LEFT' );

  [ QL, QR ] = FLA_Part_1x2( Q, ...
                               0, 'FLA_LEFT' );
                           
  [ RTL, RTR, ...
    RBL, RBR ] = FLA_Part_2x2( R, ...
                               0, 0, 'FLA_TL' );

  while ( size( AL, 2 ) < size( A, 2 ) )
