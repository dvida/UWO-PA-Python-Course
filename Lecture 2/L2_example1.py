from __future__ import print_function

"""
Converting decimal numbers to binary.
"""

# Our initial number
num = 9

# Init the binary number list
num_bin = []

while True:

	# Calculate the remainder
	rem = num%2

	# Add the remainder to the number list
	num_bin.append(str(rem))

	# Divide the number by 2 (integer division)
	num = int(num)//2

	# Break the loop if the number is 0
	if num == 0:
		break

# Reverse the list
num_bin = reversed(num_bin)

print(''.join(num_bin))