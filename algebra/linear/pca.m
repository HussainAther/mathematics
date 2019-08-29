close all, clear all, clc, format compact
% industrial data
load data2.mat
whos
% show data
figure
plot(force(find(target==1),:)','b') % OK (class 1)
grid on, hold on
plot(force(find(target>1),:)','r') % NOT OK (class 2 & 3)
xlabel('Time')
ylabel('Force')
