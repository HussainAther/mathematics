%{
Logistic map
%}

function [iterates] = logistic(x0, r, n)
    iterates = [];
    currentX = x0;
    for index = [0:n]
        iterates = [iterates, currentX];
        currentX = r*currentX*(1-currentX);
    end
    end
