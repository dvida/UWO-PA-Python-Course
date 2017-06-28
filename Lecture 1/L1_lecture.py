from __future__ import print_function

# This is a comment

print('Hello world!')

a = 15.9
b = 6

print('a =', a)
print('b =', b)

print('Addition:', a + b)
print('Subtraction:', a - b)
print('Multiplication:', a*b)
print('Division:', a/b)

print('Integer division:', a//b)
print('Modulo:', a%b)

print('a squared:', a**2)
print('a cubed:', a**3)
print('a^9:', a**9)

print('sqrt(2):', 2**(1.0/2))

c = round(1.1/3, 4)
print('Rounding floats:', c)

###################################

# Swapping variable values
print('Before: a = ', a, ', b =', b)

a, b = b, a

print('After: a = ', a, ', b =', b)


###################################

# Strings
# More on strings: https://www.tutorialspoint.com/python/python_strings.htm

name = 'Monty Python' # Apostropes
title = "Holy Grail" # Quotes

print(name)
print(title)

full_title = name + ' and the ' + title
print(full_title)

# First char
print(name[0])

# Last char
print(name[-1])

# Ranges of chars
print(name[0:5])
print(name[6:])
print(title[:4])

# Every other char
print(name[::2])
print(name[1::2])
print(name[1:8:2])

# Modifying strings, Holy Grain
print(title[:-1] + 'n')

# String length
print('Length:', len(name))

# New line escape char
print('First line\nSecond line')

# Repetition
print('Hello! '*10)

# Counting substrings
print("'n's in " + name + ':', name.count('n'))

# Replacing substrings
print(name.replace('o', 'a'))

###################################

# Type conversions
x = "3.14"
y = float(x)
z = int(y)

print(x, y, z)

###################################

# QUESTION 1
# What will this code print out:

a = 'rosemead'
b = 'new york'
print(a[2:5] + b[4:] + 'a')

# Semyorka was the world's first ICMB (developed in 1957), and it was used (in a modified form) to launch 
# Sputnik, the world's first artificial satellite.

###################################

# Lists - ultimate containters!
apollo_moon = [11, 12, 14, 15, 16, 17]

print(apollo_moon)

apollo_commanders = ['Armstrong', 'Conrad', 'Shephard', 'Scott', 'Young', 'Cernan']

print(apollo_commanders)

# Accessing elements - same as strings!
print('Post Apollo 13 commanders:', apollo_commanders[2:])

# List are MUTABLE - possible to change elements in-place
apollo_commanders[0] = 'Lovell'

print('If Neil got shingles before the flight:', apollo_commanders)

# Appending an entry
apollo_moon.append(18)
apollo_moon.append(19)

print('Added cancelled:', apollo_moon)

# Popping the last entry
cancelled = apollo_moon.pop()

print(cancelled)
print(apollo_moon)

# Insert the failed Apolo 13
apollo_moon.insert(2, 13)

print(apollo_moon)

# Remove by entry
apollo_moon.remove(13)

print(apollo_moon)

# Remove by index
apollo_moon.pop(-1)

# Find the index of the entry
print('Index of Apollo 11:', apollo_moon.index(11))

# Reversing a list (in place)
apollo_moon.reverse()
print('Reverse:', apollo_moon)

# Reversing a list without modifying it
print('Back to normal:', apollo_moon[::-1])

# Unpacking list elements to individual variables
apollo12_crew = ['Pete', 'Dick', 'Al']
commander, cm_pilot, lm_pilot = apollo12_crew

print(commander, cm_pilot, lm_pilot)

# 2D list
list2d = [[1, 2], [3, 4]]

print(list2d)

# Accessing elements of multidimensional lists
print(list2d[0][1])

# Weird lists
mission_details = [1969, 'Apollo 12', ['Conrad', 'Gordon', 'Bean'], 10.19194]

print(mission_details)

# QUESTION: Acessing Al Bean?
print(lm_pilot, mission_details[2][2])


ww2 = [1939, 1940, 1941, 1942, 1943, 1944, 1945]

# Appying a single function across a list
ww2 = list(map(str, ww2))
print(ww2)

# Joining list elements by a delimiter
print(', '.join(ww2))

###################################

# QUESTION 2
# What will this code print out:

a = [1, 2, 3, 4]
b = ['10', '11', '12', '13']
print(int("5" + b[-1]) + a[1])

# Answer: 515


###################################
# Other list operations

x = [1, 2, 20, 21, 22, 23, 1, 1]

# Summing elements inside list
print(sum(x))

# Max
print(max(x))

# Min
print(min(x))

# Counting occurences or an element in a list
print(x.count(1))

# Sorting a list (IN PLACE SORTING)
x.sort()
print(x)

# Reversing a list (IN PLACE)
x.reverse()
print(x)

###################################

# Lists: shallow copy VS deep copy

a = [1, 2, 3, 4]

# Now let's point 'b' to 'a'
b = a

# We can see that 'b' is the same as 'a'
print('a and b:', a, b)

# Now if we change 'a'
a[0] = 100
print('a and b:', a, b) # 'b' changes as well!

# This happens because 'b' was only pointing to 'a', the whole list was not copied
# To copy the list completely, we use this
b = list(a)

# Now if we change 'a' again
a[0] = 0

# 'b' stays the same
print('a and b:', a, b)


###################################

# FOR THOSE WHO WANT TO KNOW MORE

# Complex numbers

r = 1 + 1j
q = 5 - 3j

print('r =', r)
print('q =', q)
print('r+q =', r + q)
print('abs(r)', abs(r))

# Accessing complex number parts
print('Re(q) = ', q.real)
print('Im(q) =', q.imag)

print('q conjg = ', q.conjugate())
print('q**2 =', q**2)