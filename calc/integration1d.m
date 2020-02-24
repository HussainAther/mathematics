% math_1D_integration.m
% One-dimensioanl integration using Simpon's 1/3 rule

% Alter the mscript for 
% number of partitions
%    lower bound a and upper bound b
%    function y to be integrated
%    titles for graph

% INPUTS ===============================================================

% Number of partitions
    N = 9999;
% Lower bound    
    a = -4;  
% Upper bound
    b = 4;                    

             x = linspace(a,b,N);         
% Function to  be integrated
   y = -4.*x.^4  + 20.*x.^3 - 40.*x.^2 - 320.*x + 1664;

% X and Y label for graph axes
    tx = 'x';
    ty = 'y';
    
% OUTPUTS ================================================================

% Simpson's 1/3 rule ----------------------------------------------------- 
    Integral = simpson1d(y,a,b);

    disp('  ');
    format long
    disp('Integral =  ');
    disp(Integral);
 
% title
   t1 = 'Integral =  ';
   t2 = num2str(Integral,6);
   tm = [t1 t2];
   
% Graphics ---------------------------------------------------------------
    figure(1)
    fs = 14;
    plot(x,y,'b','linewidth',2);
    xlabel(tx,'fontsize',fs); ylabel(ty,'fontsize',fs);
    title(tm);
    box on;
    grid on;
    
    

