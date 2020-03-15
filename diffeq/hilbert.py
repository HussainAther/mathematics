import matplotlib.pyplot as plt
import numpy as np

from scipy.signal import hilbert, chirp

"""
Hilbert transform.
"""

duration = 1.0
fs = 400.0
samples = int(fs*duration)
t = np.arange(samples) / fs
signal = chirp(t, 20.0, t[-1], 100.0)
signal *= (1.0 + 0.5 * np.sin(2.0*np.pi*3.0*t) )
analytic_signal = hilbert(signal)
amplitude_envelope = np.abs(analytic_signal)
instantaneous_phase = np.unwrap(np.angle(analytic_signal))
instantaneous_frequency = (np.diff(instantaneous_phase) /
                           (2.0*np.pi) * fs)
fig = plt.figure()
ax0 = fig.add_subplot(211)
ax0.plot(t, signal, label="signal")
ax0.plot(t, amplitude_envelope, label="envelope")
ax0.set_xlabel("time in seconds")
ax0.legend()
ax1 = fig.add_subplot(212)
ax1.plot(t[1:], instantaneous_frequency)
ax1.set_xlabel("time in seconds")
ax1.set_ylim(0.0, 120.0)

"""
When we use the Hilbert Transform to compute the instantaneous frequency of a signal, 
a real vlaued function can be transformed into an analytic function using a complex 
part.
"""

# Analytic function for Hilbert transform
x = np.linspace(1,100,10)
y = np.linspace(1, 200, 20)
z = np.sqrt(x**2 + y**2) * np.exp(np.imag(np.arctan(y/x)))
