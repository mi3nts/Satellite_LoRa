

####################	AOD Data Download	#########################################################################



import s3fs   
import os
import datetime
from datetime import timedelta

# The top-level class S3FileSystem holds connection information and allows typical -
# -file-system style operations like cp, mv, ls, du, glob, etc., as well as put/get of local files to/from S3.
fs = s3fs.S3FileSystem(anon=True)       

year = 2020

month_start = 1
month_end = 1

day_start = 1
day_end = 3

hour = ["00", "01", "02", "03", "04"]

download_directory = "/home/prabu/Desktop/test1/ddd/"


# Find Julian day from given year/month/day
calendar_start = datetime.datetime(year, month_start, day_start)
julian_day_start = calendar_start.strftime('%j')

calendar_end = datetime.datetime(year, month_end, day_end)
julian_day_end = calendar_end.strftime('%j')

for x in range(int(julian_day_start), int(julian_day_end)):
  monthh = datetime.datetime.strptime(str(x), '%j').strftime("%m")
  dayy = datetime.datetime.strptime(str(x), '%j').strftime("%d")
  
  for i in hour:
  	download_path = download_directory + str(year) + '/'
  	download_path = download_directory + str(year) + '/' + str(monthh) + '/'
  	download_path = download_directory + str(year) + '/' + str(monthh) + '/' + str(dayy) + '/'
  	download_path = download_directory + str(year) + '/' + str(monthh) + '/' + str(dayy) + '/' + str(i) + '/'
  	
  	digit = len(str(x))
  	if digit == 1:
  		julian_day = '0' + '0' + str(x)
  	elif digit == 2:
  		julian_day = '0' + str(x)
  	else:
  		julian_day = str(x)
  	
  	
  	AWS_path = 'noaa-goes16/ABI-L2-AODC/' + str(year) + '/' + julian_day + '/' + str(i) + '/*'
  	files= fs.glob(AWS_path)
  	last_file = len(files) - 1
  	fs.get(files[last_file], download_path)
  	
print("Download complete")


