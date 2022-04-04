
#####################################################  Read AOD data in Fort Worth  #######################################################

# AOD historical data close to Fort Worth 
# Latitude = 32.759154
# Longitude = -97.342332

###########################################################################################################################################


from netCDF4 import Dataset
import numpy as np
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
# Try to install cartopy using "pip install cartopy"
# If that didn't work, use "pip install cartopy==0.19.0.post1"
# Proj, pykdtree, scipy may need to be installed

# Cartopy is a Python package designed for geospatial data processing in order to produce maps and other geospatial data analyses. Cartopy has the ability to transform points, lines, vectors, polygons and images between different projections, and it can be combined with Matplotlib to plot contours, images, vectors, lines or points in the transformed coordinates.

import os
from datetime import datetime
import pandas as pd



# main directory where AOD data is stored. 
path_1 = "/home/prabu/Desktop/test1/ddd"



# To find indexes of any location assign X_FW and Y_FW variables.
# Finding Lat and Lon index for Fort Worth - get the path of data file from for loop and read the data. 
def FW_index(path):	

    file_id = Dataset(path)
    
    # Finding Latitudes and Longitudes of AOD data
    proj_info = file_id.variables['goes_imager_projection']
    lon_origin = proj_info.longitude_of_projection_origin
    H = proj_info.perspective_point_height+proj_info.semi_major_axis
    r_eq = proj_info.semi_major_axis
    r_pol = proj_info.semi_minor_axis
    
    lat_rad_1d = file_id.variables['x'][:]
    lon_rad_1d = file_id.variables['y'][:]
    lat_rad,lon_rad = np.meshgrid(lat_rad_1d,lon_rad_1d)
    
    lambda_0 = (lon_origin*np.pi)/180.0
    
    a_var = np.power(np.sin(lat_rad),2.0) + (np.power(np.cos(lat_rad),2.0)*(np.power(np.cos(lon_rad),2.0)+(((r_eq*r_eq)/(r_pol*r_pol))*np.power(np.sin(lon_rad),2.0))))
    b_var = -2.0*H*np.cos(lat_rad)*np.cos(lon_rad)
    c_var = (H**2.0)-(r_eq**2.0)
    
    r_s = (-1.0*b_var - np.sqrt((b_var**2)-(4.0*a_var*c_var)))/(2.0*a_var)
    
    s_x = r_s*np.cos(lat_rad)*np.cos(lon_rad)
    s_y = - r_s*np.sin(lat_rad)
    s_z = r_s*np.cos(lat_rad)*np.sin(lon_rad)
    
    Lat = (180.0/np.pi)*(np.arctan(((r_eq*r_eq)/(r_pol*r_pol))*((s_z/np.sqrt(((H-s_x)*(H-s_x))+(s_y*s_y))))))
    Lon = (lambda_0 - np.arctan(s_y/(H-s_x)))*(180.0/np.pi)
    
    # Finding index of closest location to Fort Worth from 2D array of Latitudes and Longitudes 
    X_FW = -97.342332   # Fort Worth Longitude
    Y_FW = 32.759154    # Fort Worth Latitudes 
    
    x = Lon[:][:]
    y = Lat[:][:]
    
    delt_x = abs(X_FW - x)
    delt_y = abs(Y_FW - y)
    dis = (((delt_x)**(2))+((delt_y)**(2)))**(.5)    # Distance between Fort Worth and all the Latitudes and Longitudes
    index = np.where(dis == np.min(dis))  # index of minimum distance
    print(index)


# Fort Worth indexes were found from FW_index function (To find any other location uncomment the FW_index function)
# FW_Lon_index = 647
# FW_Lat_index = 835



#date_array = []
#AOD_array = []

rows = []

def read_AOD(date, path):

    date_format = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    
    file_id = Dataset(path)
    AOD_data = file_id.variables['AOD'][:,:]
    AOD_FW = AOD_data[647][835]    # AOD value near to Fort Worth 
    #print(AOD_FW)
    #print(date_format)
    rows.append([str(date_format), AOD_FW])






# taking date time and path of each data set and send them to data_read function	    							
for year in os.listdir(path_1):
    path_2 = path_1 + "/" + str(year)
    for month in os.listdir(path_2):
        path_3 = path_2 + "/" + str(month)
        for day in os.listdir(path_3):
            path_4 = path_3 + "/" + str(day)
            for hour in os.listdir(path_4):
                path_5 = path_4 + "/" + str(hour)
                for d in os.listdir(path_5):
                
                    date = str(year) + "-" + str(month) + "-" + str(day) + " " + str(hour) + ":00:00"             
                    path = path_5 + "/" + d
                    
                    #FW_index(path)		# uncomment this for find indexes of a location.
                    
                    read_AOD(date, path)
                    


df = pd.DataFrame(rows, columns=["Date", "AOD"])
df = df.sort_values(by='Date')
#print(df)
df.to_csv('/home/prabu/Desktop/test1/out2.csv')






