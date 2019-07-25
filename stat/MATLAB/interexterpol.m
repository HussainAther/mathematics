data = [1 4 3 6 2 19];
datatimes = 1:6;
newtimes = 1:.001:6;
F = griddedInterpolant(datatimes,data);
newdata = F(newtimes);
[eX,eY] = pol2cart(pi/180*[chanlocs.theta],... [chanlocs.radius]);
intFact = 100;
interpX = linspace(min(eX),max(eX),intFact); 
interpY = linspace(min(eY),max(eY),intFact); [gridX,gridY] = ndgrid(interpX,interpY);
F = scatteredInterpolant(eX',eY',eeg(:,300)); 
interpDat = F(gridX,gridY);

data = [1 4 3 6 2 19];
datatimes = 1:6;
newtimes = 1:.001:6;
newdat = interp1(datatimes,data,newtimes,’spline');
