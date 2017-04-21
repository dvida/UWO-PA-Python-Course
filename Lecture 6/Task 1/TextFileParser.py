from __future__ import print_function

def parseTextFile(file_name, delimiter=",", header=0):
	""" Parse a text file to a list. The file contents are delimited and have a header. """

	with open(file_name) as f:

		# Skip the header
		for i in range(header):
			next(f)


		data = []

		# Parse file contents
		for line in f:

			# Remove the newline char
			line = line.replace('\n', '').replace('\r', '')

			# Split the line by the delimiter
			line = line.split(delimiter)

			# Strip whitespaces from individual entries in the line
			for i, entry in enumerate(line):
				line[i] = entry.strip()

			# Add the contents of the line to the data list
			data.append(line)

		return data



if __name__ == "__main__":

	file_name = 'data.txt'

	print(parseTextFile(file_name, header=1))