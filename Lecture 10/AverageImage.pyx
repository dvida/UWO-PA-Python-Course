

# Import cython libraries
cimport cython
import numpy as np
cimport numpy as np


# Define cython types for numpy arrays
FLOAT_TYPE = np.float64
ctypedef np.float64_t FLOAT_TYPE_t


#@cython.boundscheck(False) # This disables checking that the indices of an array are valid
#@cython.wraparound(False) # This disables negative indexing, e.g. array[-1]
#@cython.cdivision(True) # This disables checks for divisions by zero
def cyAverageImg(np.ndarray[FLOAT_TYPE_t, ndim=2] img, int region):
    """ Averages image pixels in (region)x(region) neighbourhood.
    
    Arguments:
        img: [2D ndarray] image as numpy array
        region: [int] averaging neighbourhood, should be an odd number (3, 5, 7, 9, etc.)
    
    Return:
        img_avg: [2D ndarray] averaged image
    """

    cdef int reg_r = region//2

    # Output image
    cdef np.ndarray[FLOAT_TYPE_t, ndim=2] img_avg = np.zeros_like(img)

    cdef int x_size = img.shape[0]
    cdef int y_size = img.shape[1]

    cdef double s = 0
    cdef int i, j, m, n, x, y

    # Average pixels in the 3x3 region
    for i in range(x_size):
        for j in range(y_size):

            s = 0
            for x in range(-reg_r, reg_r + 1):
                for y in range(-reg_r, reg_r + 1):

                    m = i + x
                    n = j + y

                    # Wrap the borders
                    if m >= x_size:
                        m = m%x_size

                    if n >= y_size:
                        n = n%y_size


                    s += img[m, n]


            img_avg[i, j] = s/(region**2)


    return img_avg



# Import the square root function from a C library
from libc.math cimport sqrt

# cpdef means that the function will be accessible both inside this module and to external Python modules.
# If we were to write "cdef", wihtout the "p", then the function would be only available inside this module.
cpdef double cyEuclidDist(double x1, double y1, double x2, double y2):
    """ Calculate the Euclidian distance of two points in 2D. """
    
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)