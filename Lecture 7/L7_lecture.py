from __future__ import print_function

import sys

import numpy as np
import matplotlib.pyplot as plt

from TextFileParser import parseTextFile

###################################

# INTEGRATING ODEs
# Source for this example: http://www.danham.me/r/2015/10/29/differential-eq.html

# We have a system  of ordinary differential equations discribing the predator-prey system, i.e. how the 
# number of predators in an ecosystem changes over time in respect to the number of prey in the system, 
# and vice versa.

# The equations describing the behaviour are:
# dx/dt = x(2 - y - x)
# dy/dt = -y(1 - 1.5x)
# where x is the number of prey, y is the number of predators

import scipy.integrate

def ecosystem(state, t):
    """ The predator-prey system described with ODEs. """
    
    # Unpack current values of x and y
    x, y = state

    # Differential equations
    d_x = x*(2 - y - x)
    d_y = -y*(1 - 1.5*x)

    return [d_x, d_y]


# We define the initial conditions (1 prey and 1 predator)
init_state = [5, 1]

# The range of times to investigate (time step = 0.01)
t_array = np.arange(0, 20, 0.01)

# Perform the integration
results = scipy.integrate.odeint(ecosystem, init_state, t_array)

# Print states in all timesteps
print(results)

# Show the results
results = np.array(results)
plt.plot(results[:,0], results[:,1])
plt.xlabel('Prey')
plt.ylabel('Predators')

plt.show()


###################################

# SPLINE INTERPOLATION

import scipy.interpolate

file_name = 'spline_data.csv'

# Import spline data
data = parseTextFile(file_name)
data = np.array(data).astype(np.float64)

# Unpack x and y
x, y = data.T

# Plot spline data
plt.scatter(x, y)
plt.show()

# Perform spline interpolation
spline = scipy.interpolate.CubicSpline(x, y)

# Draw samples from the interpolated model
x_spline = np.linspace(np.min(x), np.max(x), 1000)
y_spline = spline(x_spline)

# Plot the interpolated results
plt.scatter(x, y)
plt.plot(x_spline, y_spline)

plt.show()



###################################

import scipy.fftpack
import scipy.signal



# TIME SERIES DATA - FOURIER TRANSFORM

# Data file
data_file_name = 'radiometer_data.csv'

# Load data from the text file
data = parseTextFile(data_file_name)
data = np.array(data).astype(np.float64)

# Split the data into time and signal
time_data, signal_data = data.T

# Show data
plt.plot(time_data, signal_data)
plt.show()

# Detrend the data (making sure the low frequency component is small)
signal_data = signal_data - np.mean(signal_data)

# Calculate samples per second
sps = len(signal_data)/(np.max(time_data) - np.min(time_data))


### Time series data plots

# Plot power spectral density
plt.psd(signal_data, Fs=sps)
plt.show()

# Plot the spectrogram
plt.specgram(signal_data, Fs=sps, cmap='inferno')
plt.show()

###


# Number of samplepoints
N = len(signal_data)

# Temporal spacing of samples
T = 1.0/sps

# Run FFT
yf = scipy.fftpack.fft(signal_data)

# Make the range of frequencies
xf = np.linspace(0.0, 1.0/(2.0*T), N/2)

# Calculate the amplitude
fft_amplitude = 2.0/N*np.abs(yf[0:N//2])

plt.plot(xf, fft_amplitude)
plt.show()


### Filtering our signal data with a Butterworth low-pass filter

# Filter order
N = 2

# Cutoff frequency, Wn is given normalized to the Nyquist frequency (sps/2)
Wn = 10.0/(sps/2)

# Make a Butterworth filter
B, A = scipy.signal.butter(N, Wn)


### Show signal response - (lecture note: C/P, DO NOT GO IN DETAIL)
w, h = scipy.signal.freqz(B, A, len(xf))
plt.semilogx((xf*0.5/np.pi)*w, 20*np.log10(np.abs(h)))
plt.title('Butterworth filter frequency response')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude [dB]')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')
plt.axvline(Wn*sps/2, color='green') # cutoff frequency
plt.show()


###

# Apply the filter to our data
signal_data_filtered = scipy.signal.filtfilt(B, A, signal_data)

# Plot both the original and the filtered data
plt.plot(time_data, signal_data)
plt.plot(time_data, signal_data_filtered, linewidth=5)
plt.show()


###################################

# WAVELETS

# Let us try to detect the position and the duration of the event in the time series

# Define the widths for wavelets ('probe sizes'): from 0 to 2 seconds, 0.1 second resolution
resolution = 0.1
widths = np.arange(0.1, 2, resolution)*sps

# Run the wavelet transform
cwtmatr = scipy.signal.cwt(signal_data_filtered, scipy.signal.ricker, widths)

# Find the maximum peaks in the wavelet parameter space
max_peak = np.unravel_index(cwtmatr.argmax(), cwtmatr.shape)
max_width = widths[max_peak[0]]/sps
max_time = max_peak[1]/sps

print('Peak at:', max_time, 'Duration:', max_width)

plt.imshow(cwtmatr, cmap='inferno', aspect='auto')
plt.show()