pic = imread('saturn.png');
imagesc(pic)
pic2 = pic;
pic2(:,:,4) = pic(:,:,1);
imagesc(pic2)
