% Householder LQ Decomposition
function [ A_out, t_out ] = HLQ( A )

  [ m, n ] = size( A );
  t = zeros( m, 1 );
  
  [ ATL, ATR, ...
    ABL, ABR ] = FLA_Part_2x2( A, ...
                               0, 0, 'FLA_TL' );
  [ tT, ...
    tB ] = FLA_Part_2x1( t, ...
                         0, 'FLA_TOP' );

  while ( size( ATL, 1 ) < size( A, 1 ) )

    [ A00,  a01,     A02,  ...
      a10t, alpha11, a12t, ...
      A20,  a21,     A22 ] = FLA_Repart_2x2_to_3x3( ATL, ATR, ...
                                                    ABL, ABR, ...
                                                    1, 1, 'FLA_BR' );

    [ t0, ...
      tau1, ...
      t2 ] = FLA_Repart_2x1_to_3x1( tT, ...
                                    tB, ...
                                    1, 'FLA_BOTTOM' );

    [ alpha11, u2, tau1 ] = Housev( alpha11, ...
                                       a12t' );
      a12t = u2';
      
      w21 = ( a21 + A22 * a12t' )/ tau1;
    
      a21 = a21 - w21;
      A22  = A22 - w21 * a12t;


    [ ATL, ATR, ...
      ABL, ABR ] = FLA_Cont_with_3x3_to_2x2( A00,  a01,     A02,  ...
                                             a10t, alpha11, a12t, ...
                                             A20,  a21,     A22, ...
                                             'FLA_TL' );

    [ tT, ...
      tB ] = FLA_Cont_with_3x1_to_2x1( t0, ...
                                       tau1, ...
                                       t2, ...
                                       'FLA_TOP' );

  end

  A_out = [ ATL, ATR
            ABL, ABR ];

  t_out = [ tT
            tB ];

end
