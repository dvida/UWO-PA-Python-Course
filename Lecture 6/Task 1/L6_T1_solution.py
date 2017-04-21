from __future__ import print_function

import numpy as np
import scipy.optimize
import matplotlib.pyplot as plt

from TextFileParser import parseTextFile


def meteor_model(x, a, b, c, d):
    """ Time vs. meteor lag. """

    return a*np.exp(b*x) + c*x + d



if __name__ == "__main__":

    # File name of the data file
    file_name = 'meteor_data.txt'

    # Load the data
    star_data = parseTextFile(file_name, header=1)

    # Convert to float numpy array
    star_data = np.array(star_data, dtype=np.float64)

    # Extract x and y data
    x = star_data[:,0]
    y = star_data[:,1]

    # Fit the model
    popt, pconv = scipy.optimize.curve_fit(meteor_model, x, y)

    print(popt)

    # Plot original data
    plt.scatter(x, y)

    # Generate new X data (original data is not sorted and not well distributed)
    x_plot = np.linspace(x.min(), x.max(), 100)

    # Plot fitted model
    plt.plot(x_plot, meteor_model(x_plot, *popt))

    plt.show()


    # Calculate residuals
    res = y - meteor_model(x, *popt)
    
    plt.scatter(x, res)

    plt.grid()
    plt.show()