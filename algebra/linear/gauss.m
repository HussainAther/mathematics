%{
Fitting Gaussian model.
}%
peak = 4;
fwhm = 1;
cent = 3;
nois = .5;
x = -10:.1:10;

gaus = peak*exp(-(x-cent).^2 / (2*fwhm^2));
gaus = gaus + nois*randn(size(gaus));

InitParms = [ 2 2 –2 ];
funch = @(initParms) fitGaussian(initParms,x,gaus); [outparams,sse] = fminsearch(funch,initParms);
funch = @(x) -sin(x)./x;
[xval,funcval] = fminsearch(funch,0);
