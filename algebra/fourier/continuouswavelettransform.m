Fs ¼ 5000;
total_time ¼ 5;
t ¼ (1/Fs):(1/Fs):(total_time/3);
f ¼ [100 500 1000];
x ¼ [cos(f(1)*2*pi*t) cos(f(2)*2*pi*t) cos(f(3)*2*pi*t)];
t ¼ (1/Fs):(1/Fs):total_time;
%add short transients
trans_time ¼ 0:(1/Fs):0.05;
trans_f ¼ 1000;
for secs ¼ 0.5:0.5:4
    trans ¼ cos(trans_f*2*pi*trans_time);
    x((secs*Fs):(secs*Fsþlength(trans)-1)) ¼ trans;
end
function coefs ¼ simple_cwt(t, x, mother_wavelet, max_wavelet, scales, params)
% Generates coefs for a continuous wavelet transform
% t, x are time and data points for time series data
% mother_wavelet is a function, taking parameters (t, params),
% where the value of params depends on the specific function used
% max_wavelet is the maximum range of the wavelet function (beyond which
% the wavelet is essentially zero)
% scales is a vector of desired scales
% params is the parameter for the mother wavelet function
max_t ¼ max(t);
dt ¼ t(2)-t(1);
full_t ¼ -(max_t/2):dt:(max_t/2);
coefs ¼ zeros(length(scales), length(x));
points ¼ length(x);
t_scale ¼ linspace(-max_wavelet, max_wavelet, points);
dt ¼ (max_wavelet*2)/(points-1);
mom_wavelet ¼ feval(mother_wavelet, t_scale, params);
row = 1;
for scale = scales
time_scale = [1þfloor([0:scale*max_wavelet*2]/(scale*dt))];
wavelet ¼ mom_wavelet(time_scale);
w ¼ conv(x,wavelet)/sqrt(scale);
mid_w ¼ floor(length(w)/2);
mid_x ¼ floor(length(x)/2);
w ¼ w(((-mid_x:mid_x)þmid_w));
scale % print scale to show progress
coefs(row,:) ¼ abs(w);
row ¼ row þ 1;
end
