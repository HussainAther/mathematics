Fs = 5000;
total_time = 5;
t = (1/Fs):(1/Fs):(total_time/3);
f = [100 500 1000];
x = [cos(f(1)*2*pi*t) cos(f(2)*2*pi*t) cos(f(3)*2*pi*t)];
t = (1/Fs):(1/Fs):total_time;
%add short transients
trans_time = 0:(1/Fs):0.05;
trans_f = 1000;
for secs = 0.5:0.5:4
    trans = cos(trans_f*2*pi*trans_time);
    x((secs*Fs):(secs*Fsþlength(trans)-1)) = trans;
end
function coefs = simple_cwt(t, x, mother_wavelet, max_wavelet, scales, params)
% Generates coefs for a continuous wavelet transform
% t, x are time and data points for time series data
% mother_wavelet is a function, taking parameters (t, params),
% where the value of params depends on the specific function used
% max_wavelet is the maximum range of the wavelet function (beyond which
% the wavelet is essentially zero)
% scales is a vector of desired scales
% params is the parameter for the mother wavelet function
max_t = max(t);
dt = t(2)-t(1);
full_t = -(max_t/2):dt:(max_t/2);
coefs = zeros(length(scales), length(x));
points = length(x);
t_scale = linspace(-max_wavelet, max_wavelet, points);
dt = (max_wavelet*2)/(points-1);
mom_wavelet = feval(mother_wavelet, t_scale, params);
row = 1;
for scale = scales
time_scale = [1þfloor([0:scale*max_wavelet*2]/(scale*dt))];
wavelet = mom_wavelet(time_scale);
w = conv(x,wavelet)/sqrt(scale);
mid_w = floor(length(w)/2);
mid_x = floor(length(x)/2);
w = w(((-mid_x:mid_x)þmid_w));
scale % print scale to show progress
coefs(row,:) = abs(w);
row = row þ 1;
end
