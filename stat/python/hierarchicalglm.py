import matplotlib.pyplot as plt
import numpy as np
import pymc3 as pm
import pandas as pd
import theano

"""
Hierachical GLM.
"""

data = pd.read_csv(pm.get_data("radon.csv"))
data["log_radon"] = data["log_radon"].astype(theano.config.floatX)
county_names = data.county.unique()
county_idx = data.county_code.values

n_counties = len(data.county.unique())

# Unpooled (non-hierarchical model)

with pm.Model() as unpooled_model:

    # Independent parameters for each county
    a = pm.Normal("a", 0, sigma=100, shape=n_counties)
    b = pm.Normal("a", 0, sigma=100, shape=n_counties)

    # Model error
    eps = pm.HalfCauchy("eps", 5)

    # Model prediction of radon level
    # a[county_idx] translates to a[0, 0, 0, 1, 1, ...],
    # we thus link multiple household measures of a county
    # to its coefficients.
    radon_est = a[county_idx] + b[county_idx]*data.floor.values

    # Data likelihood
    y = pm.Normal("y", radon_est, sigma=eps, observed=data.log_radon)
    
with unpooled_model:
    unpooled_trace = pm.sample(2000)

# Hierarchical

with pm.Model() as hierarchical_model:
    # Hyperpriors for group nodes
    mu_a = pm.Normal("mu_a", mu=0., sigma=100)
    sigma_a = pm.HalfNormal("sigma_a", 5.)
    mu_b = pm.Normal("mu_b", mu=0., sigma=100)
    sigma_b = pm.HalfNormal("sigma_b", 5.)

    # Intercept for each county, distributed around group mean mu_a
    # Above we just set mu and sd to a fixed value while here we
    # plug in a common group distribution for all a and b (which are
    # vectors of length n_counties).
    a = pm.Normal("a", mu=mu_a, sigma=sigma_a, shape=n_counties)
    # Intercept for each county, distributed around group mean mu_a
    b = pm.Normal("b", mu=mu_b, sigma=sigma_b, shape=n_counties)

    # Model error
    eps = pm.HalfCauchy("eps", 5.)

    radon_est = a[county_idx] + b[county_idx]*data.floor.values

    # Data likelihood
    radon_like = pm.Normal("radon_like", mu=radon_est,
                           sigma=eps, observed=data.log_radon)
# Inference button (TM)!
with hierarchical_model:
    hierarchical_trace = pm.sample(2000, tune=2000, target_accept=.9)
    
pm.traceplot(hierarchical_trace,
             var_names=["mu_a", "mu_b",
                        "sigma_a", "sigma_b",
                        "eps"]);

pm.traceplot(hierarchical_trace,
             var_names=["a"], coords={"a_dim_0": range(5)});

# Posterior predictive check

selection = ["CASS", "CROW WING", "FREEBORN"]
fig, axis = plt.subplots(1, 3, figsize=(12, 6), sharey=True, sharex=True)
axis = axis.ravel()
for i, c in enumerate(selection):
    c_data = data[data.county == c]
    c_data = c_data.reset_index(drop=True)
    c_index = np.where(county_names == c)[0][0]
    z = list(c_data["county_code"])[0]

    xvals = np.linspace(-0.2, 1.2)
    for a_val, b_val in zip(unpooled_trace["a"][:, c_index], unpooled_trace["b"][:, c_index]):
        axis[i].plot(xvals, a_val + b_val * xvals, "b", alpha=.1)
    axis[i].plot(xvals, unpooled_trace["a"][:, c_index].mean() + unpooled_trace["b"][:, c_index].mean() * xvals,
                 "b", alpha=1, lw=2., label="individual")
    for a_val, b_val in zip(hierarchical_trace["a"][z], hierarchical_trace["b"][z]):
        axis[i].plot(xvals, a_val + b_val * xvals, "g", alpha=.1)
    axis[i].plot(xvals, hierarchical_trace["a"][z].mean() + hierarchical_trace["b"][z].mean() * xvals,
                 "g", alpha=1, lw=2., label="hierarchical")
    axis[i].scatter(c_data.floor + np.random.randn(len(c_data))*0.01, c_data.log_radon,
                    alpha=1, color="k", marker=".", s=80, label="original data")
    axis[i].set_xticks([0, 1])
    axis[i].set_xticklabels(["basement", "no basement"])
    axis[i].set_ylim(-1, 4)
    axis[i].set_title(c)
    if not i % 3:
        axis[i].legend()
        axis[i].set_ylabel("log radon level")