
#####################################################  Read ECMWF data in Fort Worth  #######################################################

# AOD historical data close to Fort Worth 
# Latitude = 32.759154
# Longitude = -97.342332

###########################################################################################################################################



import cdsapi
import os

c = cdsapi.Client()



###### variables #################################
year = ['2020']
month = ['11']
#day = ['17',]
day = ['17', '18']
time = ['22:00', '23:00']

# area = [36.9, -106.8, 25.74, -92.91,]	# North, West, South, East.          Default: global
# area = [50, -125, 25, -65,] 		# US
# area = [38, -107, 25, -91,]			# TX
# area = [43, -125, 32, -113,]		# CA

area = [33, -98, 32, -97]	# Fort Worth



# Output file. Adapt as you wish.
#download_path = '/home/prabu/Desktop/test1/Metro_data/era5_US_Land.grib'
#download_directory = '/home/prabu/Desktop/test1/Metro_data/'		# local computer path
download_directory = '/home/pxh180012/Data/metro/'				# Europa computer path


# Create target Directory
try: 
    os.mkdir(download_directory + str(year[0]))
except FileExistsError:
    print("already exists")
    

for m in month:
    download_path = download_directory + str(year[0]) + '/'
    try:
    	os.mkdir(download_path + str(m))
    except FileExistsError:
    	print("already exists")
    	
    for d in day:
    	download_path = download_directory + str(year[0]) + '/' + str(m) + '/'
    	try:
    	    os.mkdir(download_path + str(d))
    	except FileExistsError:
    	    print("already exists")
    	    
    	for t in time:
    	    download_path = download_directory + str(year[0]) + '/' + str(m) + '/' + str(d) + '/' + str(t) 
    	    
    	    # Downloading data
    	    data = c.retrieve('reanalysis-era5-land',
            {'product_type': 'reanalysis',
            'variable': [
            '2m_temperature',], 
            'year': year,
            'month': m,
            'day': d,
            'time': t,
            'format': 'grib',			# Supported format: grib and netcdf. Default: grib
            'area' : area, 
            'grid' : [0.1, 0.1],		# Latitude/longitude grid.  (one latitude devided into 10 parts)         Default: 0.25 x 0.25  
            }, download_path) 
    	    



