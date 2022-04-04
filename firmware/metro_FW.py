

import numpy as np
import pygrib
import xarray as xr
import os
from datetime import datetime
import pandas as pd


#main_path = "/home/prabu/Desktop/test1/Metro_data/"		# local computer path where data stored
main_path = '/home/pxh180012/Data/metro/'			# Europa computer path where data stored

#output_path = '/home/prabu/Desktop/test1/out_metro.csv'	# local computer path where file will be saved
output_path = '/home/pxh180012/dataFrame/metro.csv'	 	# local computer path where file will be saved


rows = []

def read_metro(date, path):
    
    date_format = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    
    gr = pygrib.open(data)
    temperature = gr.select()[0].values
    mean_temp = np.mean(temperature)
    
    rows.append([str(date_format), mean_temp])
 




for year in os.listdir(main_path):
    path = main_path + str(year) + "/"
    for month in os.listdir(path):
    	path_1 = path + str(month) + "/"
    	for day in os.listdir(path_1):
    	    path_2 = path_1 + str(day) + "/"
    	    for h in os.listdir(path_2):
    	    	
    	    	date = str(year) + "-" + str(month) + "-" + str(day) + " " + str(h) + ":00"  
    	    	data = path_2 + str(h)
    	    	
    	    	read_metro(date, path)

    
  
df = pd.DataFrame(rows, columns=["Date", "mean_temp"])
df = df.sort_values(by='Date')
#print(df)
df.to_csv(output_path) 
print("Done")
    

'''
data = "/home/prabu/Desktop/test1/Metro_data/era5_US_Land.grib"

gr = pygrib.open(data)
temperature = gr.select()[0].values
pressure = gr.select()[1].values
precipitation = gr.select()[2].values

#mean_temp = np.array(temperature[1])
mean_temp = np.mean(temperature)
print(mean_temp)
'''

