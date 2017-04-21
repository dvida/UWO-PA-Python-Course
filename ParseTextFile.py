
import numpy as np


def parseData(file_name, delimiter=None, header_size=0, col_types=None, ret_array=False):
	""" Parse data form a text file

	Arguments:
		file_name: [str] Name of the input file.

	Keyword arguments:
		delimiter: [str] Data delimiter (often a comma of a semicolon). None by default, i.e. space/tab 
			delimited data
		header_size: [int] Number of lines in the header of the file. 0 by defualt.
		col_types: [type, or list of types] Define which columns are of which type. E.g. if all colums contain
			floating point data, then you can specify:
			col_types=float. 
			On the other hand, if the first colum
			contains integer values, and second column contains floating point values, you can specify:
			col_types=[int, float]
			This argument is None by default, meaning that values will be left as strings.
		ret_array: [bool] If True, the function returns a numpy array. If False, it returns a Pyhon list.
			Be aware that if col_types are specified, and one of the types is float, the whole array will be
			a float array. Furthermore, if some values in the read data are strings, the all values in the
			numpy array will be strings are well.

	Returns:
		data_list: Python list if ret_array is False, numpy array if ret_array is True

	"""

	with open(file_name) as f:

		# Skip header
		for i in range(header_size):
			next(f)

		data_list = []

		# Go through every line of the file
		for line in f:

			line = line.replace('\n', '').replace('\r', '')

			# Split the line by the given delimiter
			if delimiter is None:
				line = line.split()

			else:
				line = line.split(delimiter)


			# Convert the columns to given types
			if col_types is not None:

				if not isinstance(col_types, list):
					col_types = [col_types]*len(line)


				if len(line) == len(col_types):

					for i, (tp, entry) in enumerate(zip(col_types, line)):
						line[i] = tp(entry)
						

			data_list.append(line)

		# Convert the data to a numpy array
		if ret_array:
			data_list = np.array(data_list)


		return data_list



