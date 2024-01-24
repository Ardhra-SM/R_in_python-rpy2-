# On Windows, from a command prompt use the following command to set the R_HOME permanently as a user environment variable, replacing C:\rpath\bin with your R install location:
# setx R_HOME "C:\rpath\bin" [This can be typed into any command prompt and then the code that follows below can be written before any R package is called in python.]

import os
os.environ["R_HOME"] = r"C:/Program Files/R/R-4.3.2"
os.environ["PATH"]   = r"C:/Program Files/R/R-4.3.2/bin/x64" + ";" + os.environ["PATH"] # This the fix for pointing the R_HOME file after it has been created.

# Choosing a CRAN mirror;
import rpy2.robjects.packages as rpackages
utils= rpackages.importr('utils')
utils.chooseCRANmirror(ind=1)

# Installing required packages:
from rpy2.robjects.vectors import StrVector
packages= ('extRemes','bnlearn')
utils.install_packages(StrVector(packages))


# Import packages:
from rpy2.robjects.packages import importr
extRemes, bnlearn= importr('extRemes'), importr('bnlearn')

# Import functions:
# print(extRemes.__dict__['_rpy2r'])  # Gives a list of all the functions that are availanle in the package.

data_path= "C:/Users/ArdhraSedhu/Documents/Physical climate risk/Data_PCR/Heat_wave/Historical/tasmax_historical_percentiles.nc"
data= nc.Dataset(data_path)
variables= data.variables.keys()
time= data.variables["tasmax"]
dimension_time= time.shape

time_data= time[:]

# lat, lon= data.variables['lat'], data.variables['lon']
# print(lat)
# print(lon)
# print(lat[:])

timedim= time.dimensions[0]
print('name of time dimension = %s' % timedim)

times= data.variables[timedim]
print('units =%s, \nvalues = %s' % (times.units, times[:]))

dates= num2date(times[:], times.units)
print([date.strftime('%Y-%m-%d %H:%M:%S') for date in dates[:10]])



