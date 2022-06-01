# EMSC4033 - Project Report 

The aim of this project was to produce a python notebook that calculates the geodesic distances between a set of coordinates and a pre-defined lithospheric thickness. The statistical significance of this spatial relationship will then be evaluated against random locations using a two-sample Kolmogorov-Smirnov (K-S) test.

## Instructions

The user would only have to define a lithospheric thickness, z, in km at the beginning of the notebook, as well as upload an ASCII file of data points to read in. Subsequent data processing and figure-making is done automatically by the notebook.

The maps and figures are produced and can be easily interpreted by the user: 
- Lithospheric thickness is projected on a Robinson projected map - thick in blue and thin in red. Data points are also plotted on the maps. Further information on the data (such as age in the sample input) are colored. Colorbars are also shown below
- CDF plots are produced to show the percentage of data and random locations that are an x distance away from the define dlithospheric thickness contour. The standard deviations for the random locations are also displayed.
- D-value histograms show the frequencies of D-values obtained from the two-sample K-S tests between data and each array of random locations. The mean and standard deviation are annotated on the top-right corner of the plot
- p-value violin plots show the range and density of p-values from the two-sample K-S tests. The x-axis is reversed to show that a small p-value corresponds with a large D-value, and the limits are standardised across all plots for the different lithosphere-asthenosphere boundary (LAB) maps for easy visual comparison between each violin plot.

## Dependencies

The following packages are used:
- os - to get working directories
- io - to read temporary files
- netCDF4 - to read netCDF files
- random - to generate random coordinates
- numpy - for various number processing
- pandas - to read files and create dataframes
- pygmt - to extract contour and perform geodesic distance calculations
- matplotlib - figures and graphs
- matplotlib.pyplot - figures and graphs
- global_land_mask - to distinguish between onshore and offshore random coordinates
- scipy - to perform K-S tests

## Testing

Four pytest tests are provided for the following functions:
1. random_points() - This function generates a defined number of random onshore coordinates. As much of the processing relies on the number of random onshore points being correct, the test will also ensure that the _global_land_mask_ function is working as intended to filter for continental coordinates by checking that the size of the array of coordinates equals a known number answer.
2. get_cdf() - This function generates a histogram from input data with user-defined bin intervals. If a bin interval is too large, the numpy.histogram function returns no CDF values. Therefore, the test will check that the length of CDF values is at least one. 
3. get_std() - This function calculates the standard deviation for each user-defined bin interval. The test emulates a standard deviation calculation for one bin by calculating the stdev for an array of numbers with a known answer.
4.  ks2() - This function performs two-sample K-S tests for the data points and an array of arrays of random locations, each the same size as the length of data points. Therefore, the test checks that the size of data points is a factor of the size of total number of random locations. 

## Workflow Process

- The LAB maps are provided as netCDF files as the PyGMT grdcontour function takes grid data as input and extracts contour lines. 
- I decided to sort data and random location columns are sorted as an array of arrays after learning how to do so and index them in class. This greatly reduced the number of variables I would otherwise hae to create if I assigned each column data individual variables. 
- I used PyGMT for extracting contours and calculating the closest approach for data to contour as the runtime is extremely quick. Previosuly, I had manually plotted the contour by checking if the defined contour depth is between two subsequent LAB depths, and the geodesic distance is calculated by recursion between the data points and each contour point coordinate. This method required several hours to run whereas by using PyGMT, the total notebook runtime is under five minutes.
- The _get_std_ function is a tidier method of calculating standard deviations for values in every histogram bin. 
- The _ks2_ function performs two-sample K-S tests between the data points and each same-sized array of random locations. I chose to write this process as a function since the code is long and I will be using it repeatedly. 


## Future Avenues for Improvement

- The main aspect I would like to improve in the future is to write functions for the GMT _mapproject_ function and for the map plotting code. The string bash code in the _mapproject_ function caused a few complications when trying to write arguments in functions. For the maps, I decided to not use functions as the position of _pygmt.colorbar_ for deposit age needs to be passed only once and in between code that would have otherwise been written as a function.
