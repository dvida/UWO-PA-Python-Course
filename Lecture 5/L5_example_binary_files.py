from __future__ import print_function

import numpy as np

def readBinary(file_name):
    """ Read a binary file. """

    with open(file_name, 'rb') as fid:

        # Read the header
        header_size = int(np.fromfile(fid, dtype=np.uint32, count=1))
        station_latitude = np.fromfile(fid, dtype=np.float64, count=1)
        station_longitude = np.fromfile(fid, dtype=np.float64, count=1)
        elevation = np.fromfile(fid, dtype=np.float64, count=1)
        station_name = (b''.join(np.fromfile(fid, dtype='c', count=100))).decode("utf-8")
        year = np.fromfile(fid, dtype=np.uint32, count=1)
        data_size = int(np.fromfile(fid, dtype=np.uint32, count=1))

        # Skip to the end of the header
        fid.seek(header_size)

        # Read the tabular data
        table = np.fromfile(fid, dtype=np.float64, count=2*data_size)
        table = np.reshape(table, (data_size, 2))


    # Print header data
    print(header_size)
    print(station_latitude)
    print(station_longitude)
    print(elevation)
    print(station_name)
    print(year)
    print(data_size)

    # Print the tabular data
    print(table)



def writeBinary(file_name, header, data):
    """ Write a binary file. """

    # Open a file for binary writing
    with open(file_name, 'wb') as fid:

        # Write the header
        for data_type, entry in header:

            # Make sure each entry is written in the proper file format
            np.array(entry).astype(data_type).tofile(fid)

        # Write tabular data
        data.tofile(fid)



if __name__ == '__main__':

    ### READING AND WRITING BINARY FILES

    """
    Binary files are files which are written in a way that is easily understandable to computers - in pure 
    machine code. This of course makes them difficult for humans to read, but they do have advantages - they
    are usually very small in size and can be read by a computer extremely fast.

    To read a binary file, you alsolutely NEED to know its format. That means that you know what type are the 
    data inside the file, and what is their order and size.

    Let me illustrate. Let's say we have a binary file which contains yearly temperature measurements from one 
    weather station. Such binary file would have 2 parts:
        1) The header - Header size in bytes, station's geographical coordinates, station name, 
                        year when the data was taken, number of temperature measurements in the table.
        2) Data table - Table which contains the temperature data. The table has two columns: measurement time
                        and temperature value
    
    HEADER:
        - header_size: [uint32] header size in bytes
        - station_latitude: [float64] station's latitude in degrees
        - station_longitude: [float64] station's longitude in degrees
        - elevation: [float64] elevation in meters
        - station_name: [100 characters] name of the weather station
        - year: [uint32] year when the data was collected
        - data_size: [uint32] number of measurements in the table

    DATA TABLE:
        Contains data_size number of measurements. Each measurement has this format:
        - jd_time: [float64] julian date when the measurement was taken
        - temperature: [float64] temperature value in deg. of Celsius


    IMPORTANT:
    What is important is that each entry has a specified data type. Also, an extermely good idea is that the 
    first entry is the header size. Imagine that one day we add some entries to the header, because we need to
    expand out data format as we wanted include some more info. If the header size is not present, then the 
    new format will not work will any old code we have. By using the header size, we can keep track of the 
    number of bytes we have read in, and just skip all unread bytes until our tabular data begines.

    So, how do we calculate the header size? We take a look at individual size and number of data types, and
    sum them all together to get the number of bits. Then, we divide that number by 8 to get the size in
    bytes. In our case, we have: (32 + 64 + 64 + 64 + 100*8 + 32 + 32)/8 = 136 bytes in the header. Thus, 136
    is our header size.

    """

    ### WRITING BINARY FILES

    # We will create fake temperature measurement data
    temp_measure = []

    for jd in np.arange(2431456.5, 2431821.5, 1.0/6):
        temp_measure.append([jd, np.random.normal(13, 19)])

    temp_measure = np.array(temp_measure)

    # We will define a header as a list of (data type, value) pairs, in the proper order.
    header = [[np.uint32, 136],
              [np.float64, 33.676971],
              [np.float64, -106.475330],
              [np.float64, 1500],
              [np.str_, '{:100s}'.format('Trinity Site')],
              [np.uint32, 1945],
              [np.uint32, temp_measure.shape[0]]]

    # Name of our data file
    file_name = 'Trinity_site_1945_temps.bin'

    # Writing the binary file
    writeBinary(file_name, header, temp_measure)

    """
    If you were to open this file, you would see just a bunch of jiberish. To retrieve the file contents,
    we need to read it by knowing its format.
    """

    # Read the binary file
    readBinary(file_name)