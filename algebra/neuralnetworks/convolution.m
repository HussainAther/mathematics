setup;

%%
% -------------------------------------------------------------------------
% Part 1.1: Linear convolution
% -------------------------------------------------------------------------

%% Read an example image.
x = imread("peppers.png");

%% Convert to single format.
x = im2single(x);

%% Visualize the input x.
figure(1); clf; imshow(x);

%% Create a bank of linear filters.
w = randn(5,5,3,10,"single");

%% Apply the convolutional operator.
y = vl_nnconv(x, w, []);

%% Visualize the output y.
figure(2); clf; vl_imarraysc(y); colormap gray;

%% Try again, downsampling the output.
y_ds = vl_nnconv(x, w, [], "stride", 16);
figure(3); clf; vl_imarraysc(y_ds); colormap gray;

%% Try padding.
y_pad = vl_nnconv(x, w, [], "pad", 4);
figure(4); clf; vl_imarraysc(y_pad); colormap gray;

%% Manually design a filter.
w = [0  1 0;
     1 -4 1;
     0  1 0 ];
w = single(repmat(w, [1, 1, 3]));
y_lap = vl_nnconv(x, w, []);
figure(5); clf; colormap gray;
subplot(1,2,1); imagesc(y_lap); title("filter output"); axis("image");
subplot(1,2,2); imagesc(-abs(y_lap)); title("- abs(filter output)"); axis("image");


%% -------------------------------------------------------------------------
% Part 1.2: Non-linear gating (ReLU)
% -------------------------------------------------------------------------

w = single(repmat([1 0 -1], [1, 1, 3]));
w = cat(4, w, -w);
y = vl_nnconv(x, w, []);
z = vl_nnrelu(y);

figure(6); clf; colormap gray;
subplot(1,2,1); vl_imarraysc(y); axis("image");
subplot(1,2,2); vl_imarraysc(z); axis("image");

%% -------------------------------------------------------------------------
% Part 1.2: Pooling
% -------------------------------------------------------------------------

y = vl_nnpool(x, 15);
figure(7); clf; imagesc(y);

%% -------------------------------------------------------------------------
% Part 1.3: Normalization
% -------------------------------------------------------------------------

rho = 5;
kappa = 0;
alpha = 1;
beta = 0.5;
y_nrm = vl_nnnormalize(x, [rho kappa alpha beta]);
figure(8); clf; imagesc(y_nrm);
setup;

%% -------------------------------------------------------------------------
% Part 2.1: Linear convolution derivatives
% -------------------------------------------------------------------------

%% Read an example image.
x = im2single(imread("peppers.png"));

%% Create a bank of linear filters and apply them to the image.
w = randn(5,5,3,10,"single");
y = vl_nnconv(x, w, []);

%% Create the derivative dz/dy.
dzdy = randn(size(y), "single");

% Back-propagation
[dzdx, dzdw] = vl_nnconv(x, w, [], dzdy);

% Check the derivative numerically.
ex = randn(size(x), "single");
eta = 0.0001;
xp = x + eta * ex ;
yp = vl_nnconv(xp, w, []);

dzdx_empirical = sum(dzdy(:) .* (yp(:) - y(:)) / eta);
dzdx_computed = sum(dzdx(:) .* ex(:));

fprintf(...
  "der: empirical: %f, computed: %f, error: %.2f %%\n", ...
  dzdx_empirical, dzdx_computed, ...
  abs(1 - dzdx_empirical/dzdx_computed)*100);

%% -------------------------------------------------------------------------
% Part 2.2: Back-propagation
% -------------------------------------------------------------------------

% Parameters of the CNN.
w1 = randn(5,5,3,10,"single");
rho2 = 10;

% Run the CNN forward.
x1 = im2single(imread("peppers.png"));
x2 = vl_nnconv(x1, w1, []);
x3 = vl_nnpool(x2, rho2);

% Create the derivative dz/dx3.
dzdx3 = randn(size(x3), "single");

% Run the CNN backward.
dzdx2 = vl_nnpool(x2, rho2, dzdx3);
[dzdx1, dzdw1] = vl_nnconv(x1, w1, [], dzdx2);

% Check the derivative numerically.
ew1 = randn(size(w1), "single");
eta = 0.0001;
w1p = w1 + eta * ew1;

x1p = x1;
x2p = vl_nnconv(x1p, w1p, []);
x3p = vl_nnpool(x2p, rho2);

dzdw1_empirical = sum(dzdx3(:) .* (x3p(:) - x3(:)) / eta);
dzdw1_computed = sum(dzdw1(:) .* ew1(:));

fprintf(...
  "der: empirical: %f, computed: %f, error: %.2f %%\n", ...
  dzdw1_empirical, dzdw1_computed, ...
  abs(1 - dzdw1_empirical/dzdw1_computed)*100);
%% -------------------------------------------------------------------------
% Part 3: Learning a simple CNN
% -------------------------------------------------------------------------

setup;

%% -------------------------------------------------------------------------
% Part 3.1: Load an example image and generate its labels
% -------------------------------------------------------------------------

%% Load an image.
im = rgb2gray(im2single(imread("data/dots.jpg")));

%% Compute the location of black blobs in the image.
[pos,neg] = extractBlackBlobs(im);

figure(1); clf;
subplot(1,3,1); imagesc(im); axis equal; title("image");
subplot(1,3,2); imagesc(pos); axis equal; title("positive points (blob centres)");
subplot(1,3,3); imagesc(neg); axis equal; title("negative points (not a blob)");
colormap gray;

%% -------------------------------------------------------------------------
% Part 3.2: Image preprocessing
% -------------------------------------------------------------------------

%% Pre-smooth the image.
im = vl_imsmooth(im,3);

%% Subtract median value.
im = im - median(im(:));

%% -------------------------------------------------------------------------
% Part 3.3: Learning with stochastic gradient descent
% -------------------------------------------------------------------------

% SGD parameters:
% - numIterations: maximum number of iterations
% - rate: learning rate
% - momentum: momentum rate
% - shrinkRate: shrinkage rate (or coefficient of the L2 regulariser)
% - plotPeriod: how often to plot

numIterations = 500;
rate = 5;
momentum = 0.9;
shrinkRate = 0.0001;
plotPeriod = 10;

%% Initial CNN parameters.
w = 10 * randn(3, 3, 1);
w = single(w - mean(w(:)));
b = single(0);

%% Create pixel-level labels to compute the loss.
y = zeros(size(pos),"single");
y(pos) = +1;
y(neg) = -1;

%% Initial momentum.
w_momentum = zeros("like", w);
b_momentum = zeros("like", b);

%% SGD with momentum (stochastic gradient descent)
for t = 1:numIterations

  % Forward pass
  res = tinycnn(im, w, b);

  % Loss
  z = y .* (res.x3 - 1);

  E(1,t) = ...
    mean(max(0, 1 - res.x3(pos))) + ...
    mean(max(0, res.x3(neg)));
  E(2,t) = 0.5 * shrinkRate * sum(w(:).^2);
  E(3,t) = E(1,t) + E(2,t);

  dzdx3 = ...
    - single(res.x3 < 1 & pos) / sum(pos(:)) + ...
    + single(res.x3 > 0 & neg) / sum(neg(:));

  % Backward pass
  res = tinycnn(im, w, b, dzdx3);

  % Update momentum
  w_momentum = momentum * w_momentum + rate * (res.dzdw + shrinkRate * w);
  b_momentum = momentum * b_momentum + rate * 0.1 * res.dzdb;

  % Gradient step
  w = w - w_momentum;
  b = b - b_momentum;

  % Plots
  if mod(t-1, plotPeriod) == 0 || t == numIterations
    fp = res.x3 > 0 & y < 0;
    fn = res.x3 < 1 & y > 0;
    tn = res.x3 <= 0 & y < 0;
    tp = res.x3 >= 1 & y > 0;
    err = cat(3, fp|fn , tp|tn, y==0);

    figure(2); clf;
    colormap gray;

    subplot(2,3,1);
    plot(1:t, E(:,1:t)");
    grid on; title("objective");
    ylim([0 1.5]); legend("error", "regularizer", "total");

    subplot(2,3,2); hold on;
    [h,x]=hist(res.x3(pos(:)),30); plot(x,h/max(h),"g");
    [h,x]=hist(res.x3(neg(:)),30); plot(x,h/max(h),"r");
    plot([0 0], [0 1], "b--");
    plot([1 1], [0 1], "b--");
    xlim([-2 3]);
    title("histograms of scores"); legend("pos", "neg");

    subplot(2,3,3);
    vl_imarraysc(w);
    title("learned filter"); axis equal;

    subplot(2,3,4);
    imagesc(res.x3);
    title("network output"); axis equal;

    subplot(2,3,5);
    imagesc(res.x2);
    title("first layer output"); axis equal;

    subplot(2,3,6);
    image(err);
    title("red: pred. error, green: correct, blue: ignore");

    if verLessThan("matlab", "8.4.0")
      drawnow;
    else
      drawnow expose;
    end
  end
end
% EXERCISE4   Part 4 of the VGG CNN practical

setup;

%% -------------------------------------------------------------------------
% Part 4.1: prepare the data
% -------------------------------------------------------------------------

%% Load character dataset.
imdb = load("data/charsdb.mat");

%% Visualize some of the data.
figure(10); clf; colormap gray;
subplot(1,2,1);
vl_imarraysc(imdb.images.data(:,:,imdb.images.label==1 & imdb.images.set==1));
axis image off;
title("training chars for ""a""");

subplot(1,2,2);
vl_imarraysc(imdb.images.data(:,:,imdb.images.label==1 & imdb.images.set==2));
axis image off;
title("validation chars for ""a""");

%% -------------------------------------------------------------------------
% Part 4.2: initialize a CNN architecture
% -------------------------------------------------------------------------

net = initializeCharacterCNN();

%% -------------------------------------------------------------------------
% Part 4.3: train and evaluate the CNN
% -------------------------------------------------------------------------

trainOpts.batchSize = 100;
trainOpts.numEpochs = 15;
trainOpts.continue = true;
trainOpts.learningRate = 0.001;
trainOpts.expDir = "data/chars-experiment";

%% Take the average image out.
imdb = load("data/charsdb.mat");
imageMean = mean(imdb.images.data(:));
imdb.images.data = imdb.images.data - imageMean;

%% Call training function in MatConvNet.
[net,info] = cnn_train(net, imdb, @getBatch, trainOpts);

%% Save the result for later use.
net.layers(end) = [];
net.imageMean = imageMean;
save("data/chars-experiment/charscnn.mat", "-struct", "net");


%% -------------------------------------------------------------------------
% Part 4.4: visualize the learned filters
% -------------------------------------------------------------------------

figure(2); clf; colormap gray;
vl_imarraysc(squeeze(net.layers{1}.filters),"spacing",2)
axis equal; title("filters in the first layer");


%% -------------------------------------------------------------------------
% Part 4.5: apply the model
% -------------------------------------------------------------------------

%% Load the CNN learned before.
net = load("data/chars-experiment/charscnn.mat");

%% Load the sentence.
im = im2single(imread("data/sentence-lato.png"));
im = 256 * (im - net.imageMean);

%% Apply the CNN to the larger image.
res = vl_simplenn(net, im);

%% Visualize the results.
figure(3); clf;
decodeCharacters(net, imdb, im, res);


%% -------------------------------------------------------------------------
% Part 4.6: train with jitter
% -------------------------------------------------------------------------

trainOpts.batchSize = 100;
trainOpts.numEpochs = 15;
trainOpts.continue = true;
trainOpts.learningRate = 0.001;
trainOpts.expDir = "data/chars-jit-experiment";

%% Initlialize a new network.
net = initializeCharacterCNN();

%% Call training function in MatConvNet.
[net,info] = cnn_train(net, imdb, @getBatchWithJitter, trainOpts);

%% Save the result for later use.
net.layers(end) = [];
net.imageMean = imageMean;
save("data/chars-experiment/charscnn-jit.mat", "-struct", "net");

%% Visualize the results on the sentence.
figure(4); clf;
decodeCharacters(net, imdb, im, vl_simplenn(net, im));



% EXERCISE5   Part 5 of the VGG CNN practical

setup;

%% -------------------------------------------------------------------------
% Part 5.1: load a pretrained model
% -------------------------------------------------------------------------

net = load("data/imagenet-vgg-verydeep-16.mat");
vl_simplenn_display(net);

%% -------------------------------------------------------------------------
% Part 5.2: use the model to classify an image
% -------------------------------------------------------------------------

%% Obtain and preprocess an image.
im = imread("peppers.png");
im_ = single(im); % note: 255 range
im_ = imresize(im_, net.normalization.imageSize(1:2));
im_ = im_ - net.normalization.averageImage;

%% Run the CNN.
res = vl_simplenn(net, im_);

%% Show the classification result.
scores = squeeze(gather(res(end).x));
[bestScore, best] = max(scores);
figure(1); clf; imagesc(im); axis image;
title(sprintf("%s (%d), score %.3f",...
net.classes.description{best}, best, bestScore));
