import os
import shutil
import random


data_dir = 'data'

prefix = 'Cluster'
data_files = ['original', 'modeled', 'fitted', 'final']


# Remove old data dir if it exists
if os.path.isdir(data_dir):
	shutil.rmtree(data_dir)

# Make a new data dir
os.mkdir(data_dir)

for i in range(50):

	for file_type in data_files:

		start = random.randint(0, 359)
		end = random.randint(start+1, 360)

		file_name = "_".join(map(str, [prefix, i+1, 'sol', start, end, file_type])) + '.txt'

		with open(os.path.join(data_dir, file_name), 'w') as f:
			for j in range(5):
				f.write(str(random.gauss(i, j))+'\n')

