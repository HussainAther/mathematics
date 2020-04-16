% Householder LQ Decomposition
function [ A_out, t_out ] = HLQ( A )

  [ m, n ] = size( A );
  t = zeros( m, 1 );
  
  [ ATL, ATR, ...
    ABL, ABR ] = FLA_Part_2x2( A, ...
                               0, 0, 'FLA_TL' );
