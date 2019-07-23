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

[y,x] = hist(y,100);

% first piece
x1 = [ones(bpoint,1) x(1:bpoint)];
y1 = y(1:bpoint);
b1 = (x1'*x1)\(x1'*y1);

% second piece
x2 = [ones(length(x)-bpoint,1) x(bpoint+1:end)]; y2 = y(bpoint+1:end);
b2 = (x2'*x2)\(x2'*y2);
