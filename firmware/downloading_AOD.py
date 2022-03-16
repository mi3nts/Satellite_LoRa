

############### 	Downloading AOD data 	#################################################################################
############### 	Assign Year, Month, Date and Hour at line 70	##########################################################



# Library to perform array operations
import numpy as np

# Module to interface with s3 (AWS)
import s3fs

# Module for manipulating dates and times
import datetime

# Module to access files in the directory
import os



# Find Julian day from given year/month/day
def julian(year, month, day):
    calendar = datetime.datetime(year, month, day)
    julian_day = calendar.strftime('%j')

    return julian_day



# Create array containing ABI data file names for given satellite/product and date/time period
def aws_list(year, month, day, start, end, satellite, product):

    # Access AWS using anonymous credentials
    aws = s3fs.S3FileSystem(anon=True)

    # Make a list of all data files encompassing given date and start/end hours
    julian_day = julian(year, month, day)
    start_time = str(start)[0:2]
    end_time = str(end)[0:2]
    hour_range = range(int(start_time), int(end_time) + 1)
    final_list = []
    for i in hour_range:
        hour_files = aws.ls('noaa-goes' + str(satellite) + '/' + product + '/' + str(year) + '/' + julian_day + '/' + str(i) + '/')
        final_list.extend(hour_files)
        all_hours = np.array(final_list)

    # Extract list of data files for specified period set by start/end times
    data = []
    # List file names
    for i in all_hours:
        if i[-42:-38] >= str(start) and i[-42:-38] <= str(end):
            data.append(i)
        else:
            continue

    return data






save = 'yes'  # Option to save data files: 'yes' (save to "save_path" directory) or 'no' (list file names only)
#save_path = os.getcwd() + '/'  # Directory where data files will be saved


# Satellite and product settings
satellite = 16  # GOES-East = 16, GOES-West = 17
product = 'ABI-L2-AODC'  # ABI product name abbreviation; see list at https://docs.opendata.aws/noaa-goes16/cics-readme.html

# Day and time settings
year = 2020    # 4-digit year (e.g., 2021)
month = 12    # 1- or 2-digit month (e.g., Feb = 2, Oct = 10)
day = 3    # 1- or 2- digit day (e.g., 1, 25)
start = 2000    # 4-digit observation start time in UTC, no colon (e.g. 20:00 UTC = 2000)
end = 2020    # 4-digit observation end time in UTC, no colon (e.g. 20:35 UTC = 2035)


hour = str(start)[0:2]



# Creating a path to save the data
Euro_path = '/home/pxh180012/Data/AOD'
path = Euro_path + '/' + str(year)  
path = Euro_path  + '/' + str(year) + '/' + str(month)
path = Euro_path  + '/' + str(year) + '/' + str(month) + '/' + str(day)
path = Euro_path  + '/' + str(year) + '/' + str(month) + '/' + str(day) + '/' + hour


#path = os.getcwd() + '/' + str(year)  
#path = os.getcwd() + '/' + str(year) + '/' + str(month)
#path = os.getcwd() + '/' + str(year) + '/' + str(month) + '/' + str(day)
#path = os.getcwd() + '/' + str(year) + '/' + str(month) + '/' + str(day) + '/' + hour

print('Path: ' + path)
save_path = path + '/'




if __name__ == "__main__":

    # Query AWS and list filenames matching entered settings
    data = aws_list(year, month, day, start, end, satellite, product)
    if len(data) > 0:
        for i in data:
            print(i.split('/')[-1])
    else:
        print('No files retrieved.  Check settings and try again.')

    # Downlad and save data files to specfied directory
    if save == 'yes':
        aws = s3fs.S3FileSystem(anon=True)
        for i in data:
            aws.get(i, save_path + i.split('/')[-1])
        print('Download complete!')
    else:
        pass

