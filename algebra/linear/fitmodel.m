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

yHat = [b1(1)+b1(2)*x1(:,2); b2(1)+b2(2)*x2(:,2)]; 
sse = sum((yHat-y).^2) / sum(y.^2);
x = [ 1 2 3 4 5 ];
x = [ 3 4 1 2 5 ];
[~,i]=sort(x);
x=x(i); y=y(i);

[~,initB] = min(abs(x-.5));
funch = @(initB)fit2segLinear(initB,x,y); [optBreakPoint,sse,exitflag,fmininfo] = ...
            fminsearch(funch,initB);

