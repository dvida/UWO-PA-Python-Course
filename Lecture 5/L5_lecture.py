from __future__ import print_function

import numpy as np
import matplotlib.pyplot as plt


### Plotting, level 2
x = np.linspace(0, 10, 100)

plt.plot(x, np.sin(x), color='red', linestyle='--', label='Sine')
plt.plot(x, np.sqrt(x), color='g', linewidth=10, label='Sqrt')
plt.plot(x, np.tan(x), color='#FFD700', linestyle='', marker='o', label='Tan')

# Adding a legend
plt.legend(loc='upper left')

# plt.show()

# Forcing plot limits
plt.xlim((0, 5))
plt.ylim((0, 2))

plt.show()

plt.clf()
plt.close()


### Plotting, level 3

x = np.linspace(1, 100, 1000)

plt.plot(x, np.log10(x)+np.sin(x))

# Setting a logarithmic scale
plt.xscale('log')

# Turn on grid (both major and minor grid lines)
plt.grid(which='both')

plt.show()

plt.clf()
plt.close()


### Plotting, level 4

# Making several subplots
fig, (ax1, ax2) = plt.subplots(nrows = 2) #, sharex=True)

x1 = np.linspace(0, 10, 100)
ax1.plot(x1, np.sin(x1), color='g')

x2 = np.linspace(5, 15, 100)
ax2.plot(x2, np.cos(x2), color='r')

ax1.grid()
ax2.grid()

# fig.subplots_adjust(hspace=0)

plt.show()

# Uncomment sharex and fig.subplots_adjust for sharing the X axis

plt.clf()
plt.close()


### Plotting, level 5

x = np.linspace(-np.pi, np.pi, 100)
plt.plot(x, np.sin(x), color='r', label='Sine')
plt.plot(x, np.cos(x), color='b', label='Cosine')

# Setting ticks in LaTeX style
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], ['$-\pi$', '$-\pi/2$', '$0$', '$\pi/2$', '$\pi$'])
plt.yticks([-1, 0, 1], ['$-1$', '$0$', '$1$'])

plt.xlim((-np.pi, np.pi))

plt.legend(loc='upper left', frameon=False)

# plt.show()

# Moving spines (JUST C/P, NO DETAILED EXPLANATOIN!)
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

plt.show()

plt.clf()
plt.close()


###################################

### Numpy continued

a = np.arange(100, 200)

# Indexing works the same as with lists
print(a[0])
print(a[-1])

print(a[5:20])

# Reshape to 2 columns
a = a.reshape((-1, 2))

print(a)

# Accessing 2D elements - NOTICE: slightly different than lists!
print(a[5,0])

# Array slicing

first_row = a[0,:]
print(first_row)

first_column = a[:,0]
print(first_column)

second_column = a[:,1]
print(second_column)

print(a.shape)

# Splitting arrays - by column
first_column, second_column = np.hsplit(a, 2)
print(first_column)
print(second_column)

# For splitting by row, use vsplit

###################################

# USING NUMPY DOCUMENTATION:
# Google: numpy sample uniform


# Sampling distributions

# Uniform distribution
uniform_sample = np.random.uniform(0, 1, 10)

print(uniform_sample)

# Normal distribution 1D
normal_sample = np.random.normal(0, 1.0, 200)

print(normal_sample)

# Taking samples from an existing array
samples = np.random.choice(normal_sample, 10)

print(samples)

# Conditional filtering - taking only positive numbers in the normal sample
print(normal_sample[normal_sample > 0])

# Conditionally modifying an array, overwriting zero values
uniform_sample[uniform_sample > 0.5] = 0

print(uniform_sample)

###################################

# Numpy - linear algebra:
# https://docs.scipy.org/doc/numpy/reference/routines.linalg.html

###################################
# FOR THOSE WHO WANT TO KNOW MORE

# Plotting a histogram of our normal sample
plt.hist(normal_sample, bins=10)#, cumulative=True)

plt.show()

plt.clf()
plt.close()

###################################

# IMPORTANT: Shallow vs deep copy
a = np.arange(10)

print(a)

# Assigning the array to another variable (not not copying it!)
b = a

# Modifying 'b' will also modify 'a'
b[0] = 100

print(a)

# The proper way of copying arrays
b = np.copy(a)

a[0] = 9

print('a:', a)
print('b:', b)

###################################

# Sorting arrays
a = np.random.uniform(0, 10, 10)

print(np.sort(a))

# Sorting by the second column
a = np.random.uniform(0, 10, (20, 2))
a = a[a[:,1].argsort()]

print(a)

###################################

# Showing images

a = np.linspace(0, 255, 200*200).reshape(200, 200)#.T

# Showing an image - IMPORTANT: DIFFERENT COLORMAPS
# Recommended colormaps: inferno, magma, viridis, gray
# Not recommended: jet
plt.imshow(a, cmap='inferno')

plt.show()

# Show the TRANSPOSING!

plt.clf()
plt.close()

###################################

# Plotting 3D data using scatter and color
x = np.random.rand(100)
y = np.random.rand(100)
z = np.arange(100)

plt.scatter(x, y, c=z, edgecolors='none')
plt.colorbar(label='my data')

plt.show()

plt.clf()
plt.close()


###################################
# FOR THOSE WHO WANT TO KNOW MORE

# Contour plots

import matplotlib.mlab as mlab

# Define the size of the plot (Xmin, Xmax, Ymin, Ymax)
extent = (-3, 3, -2, 2)

# 'Resolution' of the plot
delta = 0.025 

x = np.arange(extent[0], extent[1], delta)
y = np.arange(extent[2], extent[3], delta)

# Generate the background 'grid' for the data
X, Y = np.meshgrid(x, y)

# Generate 2 bivariate Gaussian distributions
Z1 = mlab.bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0)
Z2 = mlab.bivariate_normal(X, Y, 1.5, 0.5, 1, 1)

# Difference of Gaussians (so we can get some nice data for plotting)
Z = 10.0 * (Z2 - Z1)

# Define contour levels (from -1 to 1.5 with 0.25 step)
levels = np.arange(-1.0, 1.5, 0.25)

# Plot the image (set the extent to the data size, otherwise the image size would be dimension/delta)
plt.imshow(Z, extent=extent, cmap='inferno')

# Plot the contours with the given levels (omit the 'levels' for auto levels)
# NOTE: origin='upper' must be set, as images usually start in the upper left corner - if this was not set, 
# the contours would be upside down
CS = plt.contour(Z, levels=levels, origin='upper', extent=extent)

# Label the contours (inline=1 creates a break in countour lines for inserting the text)
plt.clabel(CS, inline=1, fontsize=10)

plt.show()