function m=morlet(t, params)
sigma = params(1);
m = pi∧-0.25*exp(-i*sigma.*t-0.5*t.∧2);
In plot_cwt.m:
function plot_cwt(t, coefs, scales)
imagesc(t, scales, coefs);
colormap(hot);
axis xy;
end
