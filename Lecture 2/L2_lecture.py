from __future__ import print_function

# While loop

# Fibonacci series
a, b = 0, 1
while b < 50:
    print(b, end=',')
    a, b = b, a+b
print()

# Many new concepts in the code above!
# INDENTATION - Python's way of grouping statements
# - NO BRACKETS
# - NICELY FORMATTED CODE
# - 4 SPACES

# # INFINITE LOOP!
# while 1:
#   pass

###################################

# If statement

a = 10

print('a is an', end=' ')
if a%2 == 0:
    print('even number!')
else:
    print('odd number!')


print('a is', end=' ')
if a <= 10:
    print('less than or equal to 10')
else:
    print('greater than 10')

# Relational operators:
# == equal to
# != not equal to
# <  less than
# >  greater then
# <= 
# >=

# Bools
print(8 == 8) # True
print(1 == 2) # False
print(True == 1) # True
print(False == 0) # True

# None, same as NULL in C
var = None

if var is None:
    print('The variable is None!')


# Combining conditions - airplane edition
age = 8

if age < 2:
    print('Free fare!')

elif (age > 2) and (age < 12): # We can have elifs as much as we want
    print('50% off!')

else:
    print('Full fare!')

# Logical operators:
# not, and, or, ^ (xor)

# Testing strings

test_str = 'It is not safe to go alone. Take this!'

if 'safe' in test_str:
    print('Thanks!')

# The same thing works for lists (checking if 'y' is one of the elements of the list)

test_list = [1, 2, 3.14, 4]

if 3.14 in test_list:
    print(test_list)
    

# List as condition
test_list = []

if test_list:
    print('The list is not empty!')
else:
    print('The list is empty!')

###################################

# QUESTION 1
# What does this code print out?

x = 81

if (x%2 == 0) and (x > 100):
	print('Alpha')

elif ((x%3 == 0) and not (x%9 == 0)):
	print('Kilo')

elif ((x%5 == 0) or ((x-1)/10 < 10)):
	print('Delta')

else:
	print('Echo')

###################################

# Controlling the flow of a loop - finding the first number divisible by 2, 3 and 7; breaking the loop after

x = 1
while x < 100:

    if (x%2 == 0) and (x%3 == 0) and (x%7 == 0):
        print(x)

        # Break the loop
        break

    x += 1


# Controlling the flow of a loop - mark all leap years between 1990 and 2020 (continue statement)
# Leap years:
# - The year can be evenly divided by 4;
# - If the year can be evenly divided by 100, it is NOT a leap year, unless;
# - The year is also evenly divisible by 400. Then it is a leap year.

x = 1990
while x < 2020:

    x += 1

    if ((x%4 == 0) and (x%100 != 0)) or (x%400 == 0):
        print(x, 'leap')

        continue

    print(x)


###################################

# For loop

# First 50 numbers in the Fibonnaci series
a, b = 0, 1
for i in range(50):
    print(b, end=',')
    a, b = b, a+b


# Looping over a predefined list
cities = ['New York', 'Paris', 'Peckham']
for city in cities:
    print(city)


# Enumerating
for i, city in enumerate(cities):
    print(i, city)


# Zipping lists
countries = ['USA', 'France', 'UK']
for country, city in zip(countries, cities):
    print(country, city)


###################################

# QUESTION 2
# You are reading someone's spagetti code, and you see this little gem. What does it do?

data = [
	[65.90, 432.6],
	[12.40, 76.30],
	[12.45, 90.80],
	[57.40, 47.20]]

var = 0
for x, y in data:

	if x > y:
		var += x
	else:
		var += y

print(var/len(data))

###################################

### READING FILES

file_name = 'data.txt'

# Opening a file in reading mode
with open(file_name, 'r') as f:

    # Print the file object status
    print(f.closed)

    # Print out one line from the file
    print(f.readline())

# File is closed now
print(f.closed)

# The file will close outside the with block - reading it produces an error!
# print(f.readline())

# Reading the file line by line
with open(file_name) as f:

    for line in f:
        print(line)


# Manipulating strings - splitting a string by a delimiter
a = 'one,two,three,four'
print(a.split(','))

# Stripping whitespace
b = '     center     '
print(b.strip())


# Printing the file content as a list
with open(file_name) as f:

    for line in f:

        # Remove newline char
        line = line.replace('\n', '')

        # Split the line into a list by a comma
        line = line.split(',')
        
        print(line)