from __future__ import print_function


### READING FILES

file_name = 'data.txt'


# Reading in and parsing file contents
data_list = []
with open(file_name) as f:

    # SKip the header (the first line)
    next(f)

    for line in f:

        # Remove newline char
        line = line.replace('\n', '')

        # Split the line into a list by a comma
        line = line.split(',')
        
        # Parse the line
        num = line[0]
        name = line[1].strip()
        epoch = int(line[2])
        elements = list(map(float, line[3:9]))
        ref = line[9]

        # Add the line to the data list
        data_list.append([num, name, epoch, elements, ref])

        print(num, name, epoch, elements, ref)


###################################

print(data_list)

# Wile E. Coyote rewrites history...
for line in data_list:
    line[1] = 'Coyote'

print(data_list)

# But before we write the data back to disk...
###################################

### STRING FORMATTING

### Note for the lecture:
### C/P and explain how formatting works

# Converting floats to strings
x = 3.14159

print('{:4.2f}'.format(x))

# Signed formatting
print('{:+5.2f}'.format(x))

# Zero padding
print('{:06.2f}'.format(x))

# More decimals
print('{:7.5f}'.format(x))



# More decimal places than the number precision
y = 2.71
print('{:7.5f}'.format(y))

# Less decimal precision, but same size -> left padding
print('{:7.2f}'.format(y))



# Integers (same singed and zero padding rules)
z = 42
print('{:7d}'.format(z))

# Strings
print('{:10}'.format('wile e'))

# Align to the right
print('{:>10}'.format('wile e'))

# Named agruments
print("{a} {b} {c}".format(a=5, b=8, c=10))

###################################

### WRITING FILES

# Writing the data back to the list
new_file_name = 'true_data.txt'

# Open a file for writing (if a file with the same name exists, it will erase its content!)
with open(new_file_name, 'w') as f:

    # Write the header
    f.write('Num,Name,Epoch,q,e,i,w,Node,Tp,Ref\n')

    for line in data_list:

        # Composing a string
        str_line = ['{:>3}'.format(line[0]), line[1], '{:5d}'.format(line[2])]

        # Convert all elemets using the same format
        for element in line[3]:
            str_line.append('{:.3f}'.format(element))

        # Add the reference
        str_line.append(ref)

        print(str_line)

        # Convert the list to a comma delimited string
        final_line = ','.join(str_line)

        # Write the line
        f.write(final_line+'\n')

###################################

# Appending to a file
with open(new_file_name, 'a') as f:

    f.write('Wile E. was here')

###################################

### PYTHON MODULES

# Python standard library: https://docs.python.org/3/library/

import math

# Sqrt
print(math.sqrt(2))

# Sine
print(math.sin(math.pi))

# Log10
print(math.log10(100))

# Random module
import random

# Random integer in the 1 to 100 range
print(random.randint(1, 100))

# Random float in the 0 to 1 range
print(random.random())

# Shuffle a list
a = [1, 2, 3, 4, 5]
random.shuffle(a)
print(a)

# Sample 10 elements from a list
b = range(1, 100)
print(random.sample(b, 10))

# Sampling a gaussian distribution
for i in range(10):
    print(random.gauss(0, 2))


###################################
### Ways of importing modules
 
# Module alias
import math as m

print(m.sqrt(2))

# Importing individual functions - PREFERED!
from math import sqrt

print(sqrt(2))

# Importing all functions from a module - NOT RECOMMENDED!
from math import *

print(sqrt(2))
print(pi)


###################################
# FILE HANDLING - os library

import os

# Listing the contents of the current directory
print(os.listdir('.'))

# Printing the current directory
print(os.getcwd())

# Changing the current directory one up
os.chdir('..')
print(os.getcwd())

# Directory separator
# DO NOT USE / or \
print(os.sep)

### Making a new directory

# Construct a new path to the directory
new_dir_path = os.path.join(os.getcwd(), 'test')
print(new_dir_path)

# Make new dir if the dir does not exist
if not os.path.exists(new_dir_path):
    os.mkdir(new_dir_path)
else:
    print('The directory already exists!')

###

# Make an example file in the new directory
file_name = 'top_secret.txt'
file_path = os.path.join(new_dir_path, file_name)
with open(file_path, 'w') as f:
    pass

# Delete the file
if os.path.isfile(file_path):
    os.remove(file_path)
else:
    print('The file does not exist!')

###################################

# FILE HANDLING - shutil library

import shutil


# Make an example file
with open(file_path, 'w') as f:
    pass

# Copying files
copy_path = 'unclassified.txt'
shutil.copy2(file_path, copy_path)

# Moving/renaming files
new_name = 'public_release.txt'
shutil.move(copy_path, new_name)