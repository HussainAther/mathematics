%{
Second derivative operator.
}%

function V=secDer(v,dx,BC)
%
%F is the discrete 2nd derivative filter in 1D
F = [1 -2 1 ]/dx^2;
%
%BC determines your boundary conditions
switch BC
    case 1 %free bc's
        Vconv(v,F);
        V=V(2:end-1); %return an array the same size as the input array
    case 2 %periodic bc's
        %since the convolution filter is of length 3 then we only have to
        %pad the input array v by 1 element on either side
        pv=zeros(1,length(v)+2); %extend the input array by 2
        pv(2:end-1) = v;
        %now we fill in these two padded points with the values that the extended
        %input array would have if the first element of v and the last element of v
        %were neighbors
        pv(1)=v(end);
        pv(end)=v(1);
        V=conv(pv,F);
        V=V(3:end-2); %return the valid portion of the convolution
    end
x=linspace(-pi,pi,100); %forces even spacing in array of 100 pts from –pi to pi
dx=x(2)-x(1); %determines this spacing, the spatial mesh size
x=x(2:end); % for periodicity knock of 1st term in x array so that we don’t have repeat
% value of cos(x) at the endpoints of x (since cos(-pi)=cos(pi))
f=cos(x); %input array
d2f=secDer(f,dx,2); %computational solution to the second derivative of f with
periodic BC
d2fA=-cos(x); %analytic solution to the second derivative of f
plot(x,f,'k','LineWidth',3) %plot input f
hold on
plot(x,d2f,'b','LineWidth',5) %plot computational result of f"
plot(x,d2fA,'k:','LineWidth',3) %plot analytic result of f"
axis([-pi pi -1 1]); set(gca,'fontsize',20)
