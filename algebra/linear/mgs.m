% Modified Gram-Schmidt (gram schmidt) algorithm
function [ Q, R ] = MGS( A )

  [ m, n ] = size( A );    % extract sizes of A
  R = zeros( n, n );       % create a matrix in which to compute R
  
  [ AL, AR ] = FLA_Part_1x2( A, ...
                               0, 'FLA_LEFT' );
