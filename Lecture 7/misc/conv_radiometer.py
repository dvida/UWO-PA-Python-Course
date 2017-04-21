from datetime import datetime, timedelta

raw_data_file = '2016-03-19_04.09.03.794.csv'
filtered_data_file = 'radiometer_data.csv'


with open(raw_data_file) as f:

	with open(filtered_data_file, 'w') as f2:

		first_line = True
		for line in f:

			line = line.split(',')

			date = datetime.strptime(line[0], '%Y%m%d-%H%M%S.%f')

			if first_line:
				first_timestamp = date
				first_line = False


			relative_time = (date - first_timestamp).total_seconds()

			f2.write(','.join(["{:.6f}".format(relative_time), line[1]]))