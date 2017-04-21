from __future__ import print_function


# FUNCTIONS

def addNums(a, b):
    """ Adds two numbers and returns the result. """

    c = a + b

    return c

# Calling a function
print(addNums(5, 8))


# Input for the decimalHour function: 05:29:45

def decimalHour(time_string):
    """ Converts time from the 24hrs hh:mm:ss format to HH.hhh format. """

    hh, mm, ss = time_string.split(':')

    hh, mm, ss = map(float, (hh, mm, ss))

    result = ((ss/60) + mm)/60 + hh

    return result


# Call the function
print(decimalHour('05:29:45'))

# Call a function without the arguments
print(decimalHour)


def UTCdecimal(time_string, timezone=0):
    """ Converts time from the 24hrs hh:mm:ss to decimal hours, with respect to the timezone. """

    # Get the decimal time
    result = decimalHour(time_string) + timezone

    # Return the time (handle midnight wraparound)
    return result % 24


# Calling without parameters (time of the Trinity test on July 16, 1945)
print(UTCdecimal('05:29:45'))

# Calling with the timezone parameter (time in London, UK at the time of the Trinity test)
print(UTCdecimal('05:29:45', timezone=-7))


### Local and global variables

# Global vs local variables

def test(var):
    print('Input:', var)

    # This change will not influence the value of 'var' outside the function!
    var = 20

    print('Changed:', var)

    return 0

var = 10

test(var)

print('Global:', var)


### Unpacking function arguments from a list

def isTriangle(a, b, c):
    """ Checks if the given triangle sides can form a triangle. """

    if c > (a+b):
        return False

    elif b > (a+c):
        return False

    elif a > (b+c):
        return False

    return True

triangle_sides = [2, 3, 4]

# Unpacking list as function arguments with * (star)
print('Is ', triangle_sides, 'a triangle:', isTriangle(*triangle_sides))

###################################

### DISCUSSION BREAK

# Python philosophy
# PEP20: The Zen of Python
"""
>> import this
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""


# Style guide we are using: https://developer.lsst.io/coding/python_style_guide.html

# How to name things:
# - variable_name
# - functionName
# - ClassName
# - CONSTANTS


###################################

# NUMPY!

# Importing numpy
import numpy as np

# 2 points in 3D space
a = [[5, 1, 8], [3, 4, 6]]

print(a)

# Converting the list to a numpy array
a = np.array(a)

print(a)

# Atrubutes of a numpy array
print('Shape:', a.shape)
print('Dimensions:', a.ndim)
print('Type:', a.dtype)
print('Total number of elements:', a.size)

# Creating an array of zeros
b = np.zeros((3, 3))

print(b)
print(b.dtype)

# Creating an array of ones, forcing the type to int
c = np.ones((3, 3), dtype=np.int32)

print(c)

# Identity matrix
idm = np.eye(3)
print(idm)

# Converting the string list to a float list
num_lst = ['1.20', '2.15', '3.78', '4.05']

num_lst = np.array(num_lst).astype(np.float64)

print(num_lst)


# Creating a range of numbers from 0 to 100 as an array, with step 0.5
arr = np.arange(0, 100, 0.5)

print (arr)

# Creating a range of numbers - another approach
arr2 = np.linspace(0, 2, 9)

print(arr2)

# Reshaping an array
arr2 = arr2.reshape((3, 3))

print(arr2)

###################################

### Operations between arrays/matrices

# Adding a scalar to an array
a = np.zeros((3, 3))
a = a + 5
print(a)

# Multiplying by a scalar
a = a*3
print(a)

# Raising to a power
a = a**2
print(a)


a = np.zeros((3, 3)) + 2
b = np.zeros_like(a) + 3

# Multiplying matrices, element-wise
print(a*b)

# Dot product (matrix product)
print(np.dot(a, b))

# Some unary operations
a = np.arange(1, 101)
print('Sum:', np.sum(a))
print('Min:', np.min(a))
print('Max:', np.max(a))
print('Mean:', np.mean(a))
print('Median:', np.median(a))
print('Stddev:', np.std(a))

###################################

arr = np.linspace(1, 5, 20)

### Mathematical functions

# Square root
print(np.sqrt(arr))

# Sine
print(np.sin(arr))

# Cosine
print(np.cos(arr))

# Exponential
print(np.exp(arr))

###################################

import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)

### Basic plotting

plt.plot(x, y)

# plt.show()

# Adding a 1 sigma above mean line
plt.plot(x, np.zeros_like(x)+np.mean(y)+np.std(y), linestyle='--', color='red')

# plt.show()

# Adding a title and labels
plt.title('My first plot')
plt.xlabel('X')
plt.ylabel('Y')

# plt.show()

# Adding a grid
plt.grid()

plt.show()

# Clearing a plot
plt.clf()
plt.close()