file_name = 'data.txt'


with open(file_name) as f:

	with open('galaxies.csv', 'w') as f2:

		first_line = True
		
		for line in f:

			if first_line:
				f2.write(line)
				first_line = False
				continue

			name, dist, vr = line.split(',')

			if vr.replace('\n', '') == 'NA':
				continue

			dist = 10**(1+float(dist)/5)/1e6

			### Take galaxies which are in the linear zone

			# Skip all galaxies which are further away than 400 MPc
			if dist > 400:
				continue

			# Skip all galaxies which are further away than 400 MPc
			if dist < 20:
				continue
			###

			# Skip velocities larger than 40k km/s
			if int(vr.replace('\n', '')) > 40000:
				continue

			f2.write(','.join([name, str(dist), vr]))

