import s3fs
import os

fs = s3fs.S3FileSystem(anon=True)
files= fs.glob('noaa-goes16/ABI-L2-AODC/2021/140/01/*')

print(files)
fs.get(files[1], "/home/prabu/Desktop/Satellite Data/")