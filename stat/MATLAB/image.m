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
subplot(121) contourf(pic(:,:,1),40,'linecolor','none') 
title('contourf')
subplot(122)
imagesc(pic(:,:,1))
title('imagesc')
plot(rand(3))
get(gca,'xlim')
yTik = get(gca,'ytick');

pic = imread(’saturn.png');
picX = fft2(pic);
picX1 = fft(pic);
picX1 = fft(picX1,[],2);

