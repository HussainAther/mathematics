%ramp.m
% This script generates the image that creates the Mach band visual illusion.
In=10*ones(64,128); %initiates the visual stimulus with a constant value of 10
for i=1:65
In(:,32+i)=10+i;
%ramps up the value for the middle matrix elements (column 33 to column 97)
end
In(:,98:end)=75; %sets the last columns of the matrix to the final brightness value of 75
figure
imagesc(In); colormap(bone); set(gca, 'fontsize',20) %view the visual stimulus
