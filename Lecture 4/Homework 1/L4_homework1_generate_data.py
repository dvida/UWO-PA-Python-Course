import numpy as np

import matplotlib.pyplot as plt

# Generate the data
x = np.linspace(np.random.randint(0, 10), np.random.randint(195, 210), 10000)

# Noise
y = (0.5*np.sin(2*x) + 5*np.random.random(x.size)) + np.cos(0.5*x + 0.1) + 0.3*np.cos(x + 0.3)

# Add a few signals
start = 1000
stop = 1310
y[start:stop] += 7*np.sin(0.01*(np.arange(start, stop)-start))

start = 2000
stop = 2310
y[start:stop] += 10*np.sin(0.01*(np.arange(start, stop)-start))

start = 5000
stop = 5310
y[start:stop] += 20*np.sin(0.01*(np.arange(start, stop)-start))

start = 8300
stop = 8610
y[start:stop] += 5*np.sin(0.01*(np.arange(start, stop)-start))

plt.plot(x, y)
plt.show()

# Save the data to a file
data = np.column_stack((x, y))

np.savetxt('data.txt', data, fmt='%.4f', delimiter=',', header='Time,Signal')