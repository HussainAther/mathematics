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
