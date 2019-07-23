%{
Model fitting practice.
}%
funch = @(t) t.^2;
[xval,funcval] = fminbnd(funch,-30,-2);

% parameters
a=.2; c=.6; b=.9;

% generate random data and then modulate
x = rand(1,10000);
y(x<c) = a + sqrt(x(x<c).*(b-a).*(c-a));
y(x>c) = b—sqrt((1-x(x>c)).*(b-a).*(b-c));
% plot distribution
hist(y,100)
