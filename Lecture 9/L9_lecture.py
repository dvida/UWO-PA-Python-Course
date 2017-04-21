from __future__ import print_function, division

### Multiprocessing and parallelization
# See file: PyDomanParallelizer.py

###


#########################################

### Exceptions  ###


# Let's cause some errors just for fun, and see what happens:

# # Zero division:
# print(5/0)

# # Accessing non-existent element in a list
# a = [1, 2, 3]
# print(a[10])

# # Type error
# print('a' + 2)

# You can see what types of errors are caused, and try to predict which error you want to catch.

import numpy as np

def invSqrt(x):
    """ Returnes the inverse square root of a number, and returns infinity is the given number is 0. """

    try:
        return 1/np.sqrt(x)

    except ZeroDivisionError:
        return np.inf



print(invSqrt(5))
print(invSqrt(0))

# # What if we give it some nonsense?
# print(invSqrt('a'))

# We can handle all other errors by a general 'except' block - be careful when using this, as you can let
# some unpredicted errors slip through!

try:
    # Printing nonexistent variable
    print(result)
except:
    print('There was an error!')


# Check the documentation for more information:
# https://docs.python.org/3/tutorial/errors.html


#########################################

### Decorators ###
# An extremely powerful Python feature


import time

# Decorator for timing function execution time

def timeItDeco(func):
    """ Decorator which times the given function. """

    def timing(*args, **kwargs):
        """ This function will replace the original function. """

        # Start the clock
        t1 = time.clock()

        # Run the original function and collect results
        result = func(*args, **kwargs)

        # Print out the execution time
        print('Execution time', time.clock() - t1)

        return result

    # Return the funtion that was modified
    return timing



# @timeItDeco
def calcPi(n):
    """ Calculating Pi using Monte Carlo Integration. 
        
        Quickly estimates the first 2 decimals, but it is terribly inefficient for estimating other decimals.

        Source: http://www.stealthcopter.com/blog/2009/09/python-calculating-pi-using-random-numbers/
    """

    inside = 0.0

    for i in range(n):
        x = np.random.random()
        y = np.random.random()

        # Calculate the length of hypotenuse given the sides x and y
        if np.hypot(x, y) <= 1:
            inside += 1

    return 4.0*inside/n

# Run the calcPi function without timing
print(calcPi(100000))


# Wrap it inside a decorator
calcPi = timeItDeco(calcPi)

# Run the decorated function
print(calcPi(100000))

# You can also do this by putting @timeItDeco above the function declaration!

###


def memoDeco(func):
    """ Decorator which stores results of previous function calls, and for all future function calls looks up
        the result in memory before calculating it. 

    """

    cache = {}

    def mem(*args, **kwargs):

        # Check if we alreasy have a solution stored
        if args in cache:
            return cache[args]

        # If not, calculate it and add to cache
        else:

            # Calculate the result
            result = func(*args, **kwargs)

            # Store the result to cache
            cache[args] = result

            return result

    return mem


# @memoDeco
def fib(n):
    """ Calculate the Nth Fibonacci number. This is an EXTREMELY inefficient function.
    """

    if n in (0, 1):
        return n

    return fib(n-1) + fib(n-2)


# This takes a while without memoization, but it is lightning fast with memoization

t1 = time.clock()

print(fib(35))

print('Fibonacci runtime:', time.clock() - t1)


#########################################

### Regular expressions ###

# "Some people, when confronted with a problem, think 'I know, I'll use regular expressions.' 
#    Now they have two problems." - Jamie Zawinski

# Regular expression is a sequence of characters that define a search pattern.


## Possible seach pattern elements:

# . (dot) - matches any character except a newline

# * (star) - matches 0 or more repetitions of the preceding RE, as many repetitions as are possible.
#       e.g. if our regular expression was: a*, it will match: '' (EMPTY), 'a', 'aa', 'aaa', etc.

# + (plus) - matches 1 or more repetitions of the preceding RE, as many repetitions as are possible.
#       e.g. if our regular expression was: a+, it will match: 'a', 'aa', 'aaa', etc.

# ? (question mark) - matches 0 or 1 repetion of the preceding RE:
#       e.g. if our regular expression was: a?, it will match: '' (EMPTY) and 'a'.

# The '*', '+', and '?' qualifiers are all greedy - they match as much text as possible.

# {m} - matches exactly m repetitions of the preceding RE.
#       e.g. if our regular expression was: a{5}, it will match 'aaaaa'

# {m, n} - matches m to n repetitions of the preceding RE.
#       e.g. if our regular expression was: a{2, 5}, it will match 'aa', 'aaa', 'aaaa', 'aaaaa'

# [] - used to indicate a set of characters. In a set:
#       - Characters can be listed individually, e.g. [amk] will match 'a', 'm', or 'k'.
#       - Ranges of characters can be indicated by giving two characters and separating them by a '-', for 
#            example [a-z] will match any lowercase ASCII letter, [0-5][0-9] will match all the two-digits 
#            numbers from 00 to 59.

# | - A|B, where A and B can be arbitrary REs, creates a regular expression that will match either A or B.
#       It is basically the 'or' logical operator.

# () - defines a group which will be consided a RE. 
#       E.g. if we want to match all occurences of the 'cat' in a string, we would write (cat)*

import re


# Let's match all repetitions of the letter 'a'
s = 'a aa aaa'

# Find all occurences and their indices of start and end
match = re.finditer('a+', s)

# Go through all matches
for group in match:
    
    start = group.start()
    end = group.end()
    
    print(start, end, s[start:end])



# Let's write a regular expression which will match phone numbers in this format:
tel_num = '031-212-555'

match = re.findall('[0-9]{3}-[0-9]{3}-[0-9]{3}', tel_num)

if match:
    print(tel_num, 'is a proper telephone number!')

else:
    print('Wrong format!')

# Now try to change the telephone number to be of another format!


# In a list of courses, let's find all astronomy courses about Mars
courses = [
    'ASTRO 101 - Intro',
    'ASTRO 206 - Earth',
    'ASTRO 287 - Intro to Mars',
    'ASTRO 457 - Marsian atmosphere'
    ]

for course in courses:
    match = re.findall('ASTRO [0-9]{3} - .*Mars.*', course)

    if match:
        print(match)