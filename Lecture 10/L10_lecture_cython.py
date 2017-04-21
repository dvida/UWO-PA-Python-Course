from __future__ import print_function, division

import time

import numpy as np
import matplotlib.pyplot as plt


size = 256

# Let's create a checkerboard image
img = np.zeros((size, size))

step = 32
for n in range(step):
    for m in range(step):
        img[n::2*step, m::2*step] = 1
        img[n + step::2*step, m + step::2*step] = 1

plt.imshow(img, cmap='gray')
plt.show()



def averageImg(img, region):
    """ Averages image pixels in (region)x(region) neighbourhood.
    
    Arguments:
        img: [2D ndarray] image as numpy array
        region: [int] averaging neighbourhood, should be an odd number (3, 5, 7, 9, etc.)
    
    Return:
        img_avg: [2D ndarray] averaged image
    """

    reg_r = region//2

    # Output image
    img_avg = np.zeros_like(img)

    x_size = img.shape[0]
    y_size = img.shape[1]

    # Average pixels in the 3x3 region
    for i in range(x_size):
        for j in range(y_size):

            s = 0
            for x in range(-reg_r, reg_r + 1):
                for y in range(-reg_r, reg_r + 1):

                    m = i + x
                    n = j + y

                    # Wrap the borders
                    m = m%x_size
                    n = n%y_size

                    s += img[m, n]


            img_avg[i, j] = s/(region**2)


    return img_avg


t1 = time.clock()
img_avg = averageImg(img, 11)

print('Python:', time.clock() - t1)

plt.imshow(img_avg, cmap='gray')
plt.show()


# Let's convert the averageImg function to cython code!
#   Convert the function in cython...


# Initialize Cython-type imports are enable cython-numpy compatibility
import pyximport
pyximport.install(setup_args={'include_dirs':[np.get_include()]})

# Import cythonized function
from AverageImage import cyAverageImg


t1 = time.clock()

# Run the cythonized average image function
img_avg = cyAverageImg(img, 11)

print('Cython:', time.clock() - t1)


plt.imshow(img_avg, cmap='gray')
plt.show()


# To see which parts of our code are slow, we can run in terminal:

# cython -a AverageImage.pyx

# This will create an annotated HTML document which will color the slow lines in yellow. If you have yellow
# lines which deep in some loops, you should work to simplify/optimize that code until the lines are white. 
# The reason you want to optimize those lines is that they are executed many times, thus they are contributing 
# the most to the runtime.

# Lecture note: now show how to disable boundscheck, wraparound and C division



# Let's write a simple mathematical function in Python
def euclidDist(x1, y1, x2, y2):
    """ Calculate the Euclidian distance of two points in 2D. """
    
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Now, let us write a cython function which returns a single number (we can optimize those function further)

from AverageImage import cyEuclidDist


# Let's compare execution times between the Python and the Cython version

# First the Python version
t1 = time.clock()

for i in range(1000):
    dist = euclidDist(1, 2, 3, 4)

print('Python:', time.clock() - t1)

# Now the Cython version
t1 = time.clock()

for i in range(1000):
    dist = cyEuclidDist(1, 2, 3, 4)

print('Cython:', time.clock() - t1)