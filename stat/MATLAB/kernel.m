%{
Gaussian kernel smoothing.
}%
gx = -20:20;
gaus2d = zeros(length(gx));
sx = 10;
sy = 30;
for xi=1:length(gx)
    for yi=1:length(gx)
        xval = (gx(xi)^2)/(2*sx^2);
        yval = (gx(yi)^2)/(2*sy^2);
        gaus2d(xi,yi) = exp(-(xval+yval));
end end
