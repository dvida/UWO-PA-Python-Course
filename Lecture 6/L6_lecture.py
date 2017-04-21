from __future__ import print_function

import numpy as np
import matplotlib.pyplot as plt

# Let's create some noisy data that should follow a line

# Parameters of a line
m = 2.6
k = 10.8


# Let's define a function describing a line
def line(x, m, k):

    return m*x + k


# Generate the line data
x = np.linspace(0, 10, 100)
line_data = line(x, m, k)

# Add noise to the line
line_data += np.random.normal(0, 1, line_data.shape)

plt.hold(True)

# Plot the line data
plt.scatter(x, line_data)

# plt.show()

# Import needed scipy libraries
import scipy.optimize

# Fit the line
popt, pcov = scipy.optimize.curve_fit(line, x, line_data)

print('Fit params:', popt)

plt.plot(x, line(x, *popt))


# plt.show()

plt.clf()

# See the documentation how to get the stddev of each parameter
print('Stddev:', np.sqrt(np.diag(pcov)))

# CONGRATS! YOUR FIRST SUCCESSFUL LINEAR REGRESSION IN PYTHON!

# Why should we be very careful when we are doing any kind of regression:
# Anscobe's Quartet: https://en.wikipedia.org/wiki/Anscombe%27s_quartet

# What are the alternatives?
# http://scikit-learn.org/stable/auto_examples/linear_model/plot_theilsen.html


# Let's add some outliers to our data
line_data[10:12] -= 30
line_data[98:] += 50
x[-1] += 10

plt.scatter(x, line_data)

# plt.show()

# If we do the LS fit again...
popt, pconv = scipy.optimize.curve_fit(line, x, line_data)

# Plot fitted line
plt.plot(x, line(x, *popt), label='LS')

# Plot original line
plt.plot(x, line(x, m, k), color='k', label='Original')

# plt.show()

# CHECK THAT scikit-learn is installed!
from sklearn.linear_model import RANSACRegressor, TheilSenRegressor

# Reshaping the data (required by the scikit functions)
x = x.reshape(-1, 1)
line_data = line_data.reshape(-1, 1)


# RANSAC details: http://scipy-cookbook.readthedocs.io/items/RANSAC.html
# RANSAC works on non-linear problems as well, often using in Computer Vision.

# Init the RANSAC regressor
ransac = RANSACRegressor()

# Fit with RANSAC
ransac.fit(x, line_data)

# Get the fitted data result
line_ransac = ransac.predict(x)

# Show the RANSAC fit
plt.plot(x, line_ransac, color='yellow', label='RANSAC')

# plt.show()


# Theil-Sen estimator: 
# General info: https://en.wikipedia.org/wiki/Theil%E2%80%93Sen_estimator
# Good ONLY for LINEAR REGRESSION
# Sci-kit learn implementation: http://scikit-learn.org/stable/auto_examples/linear_model/plot_theilsen.html

# Init the Theil-Sen estimator instance
theil = TheilSenRegressor()

# Fit with the Theil-Sen estimator
theil.fit(x, line_data)

# Get the fitted data result
line_theil = theil.predict(x)

# Plot Theil-Sen results
plt.plot(x, line_theil, color='red', label='Theil-Sen')

plt.legend(loc='lower right')

plt.show()

plt.clf()

###################################

# Minimization - e.g. how to find a minimum of a function?

def f1(x):
	""" A tricky function to minimize. """

	return 0.1*x**2 + 2*np.sin(2*x)


x = np.linspace(-10, 10, 100)

# Plot the tricky function
plt.plot(x, f1(x))

# Try changing the inital estimage (first try 0, then try 5)
x0 = 5

# Find the minimum using BFGS algorithm
res = scipy.optimize.minimize(f1, x0)

# Find global minimum using basin hopping
res = scipy.optimize.basinhopping(f1, x0, niter=2000)

print (res.x)

# Plot mimumum point
plt.scatter(res.x, f1(res.x))

plt.show()
plt.clf()



###################################

# Fitting nonlinear models

# Task 1





###################################
### NOT IN LECTURE

### EXTRA: ROBUST FIT attempt

# Difficult function to fit
def func(x, a, b, c, d, e):

    return a*np.sin(b*x) + c*x**2 + d*x + e


x = np.linspace(0, 10, 1000)

# Generte function data
y_data = func(x, 1.5, 2, 0.1, 0.1, 3)

# Plot the model data
plt.plot(x, y_data, color='red', label='Underlying model')

# Add noise
y_data_noise = y_data + np.random.normal(0, 0.5, y_data.shape)

# Plot noisy data
plt.plot(x, y_data_noise, alpha=0.5, label='Noisy data')


# Fit the function to the noisy data, regular LS
popt, pcov = scipy.optimize.curve_fit(func, x, y_data_noise)

# Plot LS fit results
plt.plot(x, func(x, *popt), color='green', label='LS fit')

# Read more about robust regression:
# http://scipy-cookbook.readthedocs.io/items/robust_regression.html

# Define a function for computing residuals
def residuals(params, x, y):
    """ Returns the residuals between the predicted and input values of the model

    Arguments:
        params: [ndarray] function parameters
        x: [ndarray] independant variable
        y: [ndarray] prediction

    Return:
        residuals: [ndarray]

    """

    return func(x, *params) - y


# Set initial guess of parameters to 1 (array of size 5, same as the number of parameters of our function)
x0 = np.ones(5)

# Try to do a robust fit (doesn't always work, but it is better than ordinary LS)
fit_robust_ls = scipy.optimize.least_squares(residuals, x0, loss='cauchy', f_scale=0.1, args=(x, y_data_noise))



def residuals_minimize(params, x, y):
    """ Wrapper function for calculating fit residuals for minimization. """

    # Squared value of each residual
    z = residuals(params, x, y)**2

    # Smooth approximation of l1 (absolute value) loss
    return np.sum(2*((1 + z)**0.5 - 1))
    

# Treat the fit as a minimization problem, but use basinhopping for minimizing residuals
fit_robust_mini = scipy.optimize.basinhopping(residuals_minimize, x0, minimizer_kwargs={'args':(x, y_data_noise)})


# Plot the robust fit results
plt.plot(x, func(x, *fit_robust_ls.x), color='yellow', label='Robust fit - least squares')
plt.plot(x, func(x, *fit_robust_mini.x), color='black', label='Robust fit - basinhopping')

plt.legend(loc='lower right')
plt.show()

# For better results, Markov-Chain Monte Carlo fitting can be used:
# https://sciencehouse.wordpress.com/2010/06/23/mcmc-and-fitting-models-to-data/

# MCMC Python implementation:
# https://github.com/dvida/mcmc-fit-py/blob/master/MCMC%20fit.py