function f=threebody(t, y)
[n,m]=size (y); f=zeros(n,m); Ms=330000; Me=1; Mm=0.1;
D1=((y(5)-y(1))^2+( y(7)-y(3))^2)^(3/2);
