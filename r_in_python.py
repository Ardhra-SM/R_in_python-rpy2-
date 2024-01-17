# On Windows, from a command prompt use the following command to set the R_HOME permanently as a user environment variable, replacing C:\rpath\bin with your R install location:
# setx R_HOME "C:\rpath\bin" [This can be typed into any command prompt and then the code that follows below can be written before any R package is called in python.]

import os
os.environ["R_HOME"] = r"C:/Program Files/R/R-4.3.2"
os.environ["PATH"]   = r"C:/Program Files/R/R-4.3.2/bin/x64" + ";" + os.environ["PATH"] # This the fix for pointing the R_HOME file after it has been created.

# Import necessary packages:
import rpy2.robjects as robjects
# from rpy2.robjects.packages import importr
# from rpy2.robjects import pandas2ri

# Must be activated:
# pandas2ri.activate()


# time_series= robjects.r('ts')
# forecast_package= importr('forecast')



