% Classic Gram-Schmidt algorithm (gram schmidt) 
function [ Q, R ] = MGS( A )

  [ m, n ] = size( A );    % Extract sizes of A.
  Q = zeros( m, n );       % Create a matrix in which to compute Q.
  R = zeros( n, n );       % Create a matrix in which to compute R.
