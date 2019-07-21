%{
Mexican hat wavelet.
}%
% mexican_hat.m
% this script produces an N by N matrix whose values are
% a 2 dimensional mexican hat or difference of Gaussians
%
N = 5; %matrix size is NXN
IE=6; %ratio of inhibition to excitation
Se=2; %variance of the excitation Gaussian
Si=6; %variance of the inhibition Gaussian
S = 500; %overall strength of mexican hat connectivity
%
[X,Y]=meshgrid((1:N)-round(N/2));
% -floor(N/2) to floor(N/2) in the row or column positions (for N odd)
% -N/2+1 to N/2 in the row or column positions (for N even)
%
[THETA,R] = cart2pol(X,Y);
% Switch from Cartesian to polar coordinates
% R is an N*N grid of lattice distances from the center pixel
% i.e. R=sqrt((X).^2 + (Y).^2)+eps;
EGauss = 1/(2*pi*Se^2)*exp(-R.^2/(2*Se^2)); % create the excitatory Gaussian
IGauss = 1/(2*pi*Si^2)*exp(-R.^2/(2*Si^2)); % create the inhibitory Gaussian
%
MH = S*(EGauss-IE*IGauss); %create the Mexican hat filter
figure; imagesc(MH) %visualize the filter
title('mexican hat "filter"','fontsize',22)
colormap(bone); colorbar
axis square; set(gca,'fontsize',20)
