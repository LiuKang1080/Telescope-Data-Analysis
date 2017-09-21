# Telescope Data Analysis Demo
Calculate the Elevation and Azimuth of each object from a data set at the current time based on Right Acension and Declination. Also find the object with the highest Elevation from that data set.
## Prerequisites
* Python (3.5.X)
* FRBS Data Set (Data from telescope should be in .dat format)
## Installation 
Ensure that the data file (.dat) is within the same directory as the Telescope_Data_Analysis.py script.
## Running Scripts
```
$ Telescope_Data_Analysis.py 
```
Running from command line will ask for the name of a data file ( ex. FRBS.dat). Once executed a FRBS_Calculations.log file will be produced containing the Object's name, elevation, azimuth and the current date and time.
