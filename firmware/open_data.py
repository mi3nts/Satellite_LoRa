
import numpy as np
import pygrib
import xarray as xr


data = '/home/prabu/Desktop/Satellite Data/download1.grib'
gr = pygrib.open(data)
grb = gr.select()[0]
data1 = grb.values
print(data1[1])
print(len(data1[1]))
print(len(data1))

print(gr.read())

# Install ECCODES C-LIBRARRY "sudo apt-get install libeccodes0" 
# Install cfgrib
ds = xr.open_dataset("download4.grib", engine="cfgrib")    

print(ds)


