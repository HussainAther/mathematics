%{
Image reading functionality.
}%
pic = imread('saturn.png');
imagesc(pic)
pic2 = pic;
pic2(:,:,4) = pic(:,:,1);
imagesc(pic2)
colorchans = { ’red';'green';'blue' };
for chani=1:3
    subplot(2,2,chani)
    imagesc(pic(:,:,chani))
    axis off
    set(gca,'clim',[0 255])
    title([ colorchans{chani} ' channel' ])
end
contourf(pic(:,:,1),40) % 10 is the default number 
contourf(pic(:,:,1),40,'linecolor','m') 
contourf(pic(:,:,1),40,'linecolor','none')
surf(pic(:,:,1))
