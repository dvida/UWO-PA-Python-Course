import numpy as np
import matplotlib.pyplot as plt
import scipy.signal



def func(x):

	signal = np.zeros_like(x)

	base_freq = 50
	amps = [2800, 2132, 867, 195]

	for i, amp in enumerate(amps):
		signal += amp*np.sin((i+1)*(base_freq*2*np.pi)*x)


	signal += 31*np.sin(192*2*np.pi*x)
	signal += 101*np.sin(242*2*np.pi*x)

	st = 2515
	en = 2670
	signal[st:en] += 200*np.sin(8*x[st:en] + np.pi + 0.7)


	# Add noise
	signal += 20*np.random.random(size=len(x))




	return signal


file_name = 'radiometer_data.csv'

x_data = np.arange(0, 10.24, 1.0/500)

y_data = func(x_data)

with open(file_name, 'w') as f:

	for x, y in zip(x_data, y_data):

		f.write("{:.6f},{:.6f}".format(x, y)+'\n')

plt.plot(x_data, y_data)
plt.show()

