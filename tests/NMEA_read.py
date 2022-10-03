from tqdm import tqdm
import datetime
import pyproj
import numpy as np
import pandas as pd

sample_file_name = "NMEA_sample.txt"
data_counter = 0

with open(sample_file_name, 'r') as f:
    str_nmea_log = f.readlines()
    
file_name_split = sample_file_name.split('-')

    # read NMEA log and extract $GPGGA
for log_line in tqdm(str_nmea_log):
    if log_line.find('GPGGA') != -1:
        data_counter += 1
        log_line_split = log_line.split(',')
        if data_counter == 1:
            date_time_str = file_name_split[0]+'-'+file_name_split[1]+'-'+file_name_split[2]+\
                            '-'+log_line_split[1]
            init_date_time = datetime.datetime.strptime(date_time_str, '%Y-%m-%d-%H%M%S')
            date_time_array = np.append(date_time_array, np.array([init_date_time]), axis=0)
            gpgga_array = np.append(gpgga_array, np.array([log_line_split]), axis=0)
            prev_date_time = init_date_time
        else:
            date_time = prev_date_time + datetime.timedelta(seconds=2)
            date_time_array = np.append(date_time_array, np.array([date_time]), axis=0)
            gpgga_array = np.append(gpgga_array, np.array([log_line_split]), axis=0)
            prev_date_time = date_time
print()
 # create DataFrame of GPGGA
gpgga_format = ['Data Type','UTC Time','Latitude','North/South','Longitude',
                    'East/West','Quality','Satellites Num','HDOP','Altitude','Alit Unit',
                    'Geoid Height','Geo Unit','Comm Time','Check Sum']
gpgga_data_frame = pd.DataFrame(data=gpgga_array, index=date_time_array, columns=gpgga_format)