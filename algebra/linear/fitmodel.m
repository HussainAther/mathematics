%{
Model fitting practice.
}%
funch = @(t) t.^2;
[xval,funcval] = fminsearch(funch,-2);
