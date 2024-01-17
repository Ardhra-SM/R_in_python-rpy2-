import os
os.environ["R_HOME"] = r"C:/Program Files/R/R-4.3.2"
os.environ["PATH"]   = r"C:/Program Files/R/R-4.3.2/bin/x64" + ";" + os.environ["PATH"]

# Import necessary packages:
import rpy2.robjects as robjects
# from rpy2.robjects.packages import importr
# from rpy2.robjects import pandas2ri

# Must be activated:
# pandas2ri.activate()


# time_series= robjects.r('ts')
# forecast_package= importr('forecast')



