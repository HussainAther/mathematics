data = [1 4 3 6 2 19];
datatimes = 1:6;
newtimes = 1:.001:6;
F = griddedInterpolant(datatimes,data);
newdata = F(newtimes);
