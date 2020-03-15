%{
Euler's method (euler) to solve ordinary differential equation (ODE).
}%
function f = ode_euler(x, f_o)
%This function takes two arguments, x and f_o.
%x is a vector that specifies the time points that the function f should be
%approximated for.
%f_o is the initial condition.
%The function returns a vector, f, representing the approximate solution to the
%differential equation, df/dx=2x with f(0)=f_o.
%Set delta_x as the difference between successive x values.
delta_x=x(2)-x(1);
%Determine how many points we need to approximate by finding the length of
%vector x.
l_x=length(x);
%Initialize f by creating a vector of the right length. We will reset the elements to
%the correct values in the for loop below.
f=zeros(1, l_x);
%Set the initial value of f to f_o.
f(1)=f_o;
%Use a for-loop to implement Eq. 19.14
for i=1:(l_x-1)
    f(iþ1)=f(i) þ delta_x*2*x(i); % line 24
end;
