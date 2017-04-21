from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt

file_name = 'spline_data.csv'



def func(x):

	freq = 1.4

	return 10*np.sin(freq*x + 0.457) + 5*np.sin(3*freq*x + 0.247) + 2.5*np.sin(6*freq*x + 0.247) + 3*np.random.random(size=len(x))


# Generate X range
x = np.linspace(11.875, 16.5478, 80)


y = func(x)

plt.scatter(x, y)
plt.show()


with open(file_name, 'w') as f:
	for row in zip(x, y):
		f.write('{:.6f},{:.6f}\n'.format(row[0], row[1]))
	
