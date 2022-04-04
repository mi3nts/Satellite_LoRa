import cdsapi
c = cdsapi.Client()
c.retrieve("reanalysis-era5-pressure-levels",
{
"variable": "temperature",
"pressure_level": "500",
"product_type": "reanalysis",
"year": "2008",
"month": "01",
"day": "01",
"time": "12:00",
"format": "grib",
'area': [30, -80, 25, -65,],
#'grid': [0.1, 0.1]
}, "/home/prabu/Desktop/Satellite Data/download1.grib")