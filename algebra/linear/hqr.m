% Householder QR factorization
function [ A_out, t_out ] = HQR( A )

  [ m, n ] = size( A );
  t = zeros( n,1 );
  
  [ ATL, ATR, ...
    ABL, ABR ] = FLA_Part_2x2( A, ...
                               0, 0, 'FLA_TL' );

