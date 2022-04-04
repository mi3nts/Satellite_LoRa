
import xarray as xr
import matplotlib.pyplot as plt
from pyproj import Proj
import numpy as np
import cartopy

# s3Fs is a Pythonic file interface to S3 (Amazon Simple Storage Service (Amazon S3))
import s3fs   
import os

# The top-level class S3FileSystem holds connection information and allows typical -
# -file-system style operations like cp, mv, ls, du, glob, etc., as well as put/get of local files to/from S3.
fs = s3fs.S3FileSystem(anon=True)       
files= fs.glob('noaa-goes16/ABI-L2-AODC/2021/140/01/*')
# print(files)
fs.get(files[1], "/home/prabu/Desktop/Satellite Data/")
ds_GOES = xr.open_dataset("/home/prabu/Research/GOES_16_data/OR_ABI-L2-AODC-M6_G16_s20211400106152_e20211400108525_c20211400110132.nc")