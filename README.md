# EMSC4033-Project
The repository provides a notebook to perform quantitative analyses on geodesic distances between lithospheric thickness and the data of the user's choice. The data will be plotted on various lithosphere-asthenosphere boundary (LAB) maps, and statistical histograms and violinplots will be produced.

This markdown file includes a guide to navigate the repository and explains the workflow of the *Quantitative_analysis.ipynb* notebook.

## Navigating the Repository
#### Quantitative_analysis.ipynb
This is the main product of the repository - a notebook which displays the workflow and presents the final figures that are interpretable to the user. The user chooses a datafile to upload (ASCII format) and defines a lithospheric depth (km) of interest. Users may also customise maps and figures, which will be saved in the format of the user's choice. 

_This notebook is essentially a sample input that analyses the relationship between magmatic nickel sulphide deposits and a lithospheric depth of 170 km. Final figures are saved as JPEG files_

#### src
The *src* (source) folder contains all the "inner-workings" of the *Quantitative_analysis.ipynb* notebook. It contains a *data* folder that holds NetCDF files of the four LAB maps used in the notebook, as well as a CSV file containing data of global magmatic nickel occurrences for the sample input, whose sources are as follows: 

###### Lab maps:
- SL2013sv - Upper-mantle shear wave tomography (Schaeffer & Lebedev, 2013)
- LITHO1.0 - Surface wave tomography (Pasyanos et al., 2014)
- A2006 - Surface heat flow measurements (Artemieva, 2006)
- LithoRef18 - Joint inversion of seismic, potential field and geochemical data (Afonso et al., 2019)


###### Deposit data:
- Global magmatic nickel deposits (Hoggard et al., 2020)

*dependencies.py* imports all the packages required to run the notebook. This file is called at the beginning of the notebook.

*functions.py* contains various functions that conducts the workflow of the notebook. Lengthy or repeatedly-used code are written as functions to minimise the length of the main notebook. This file is called at the beginning of the notebook.

#### Tests
Test functions and Pytest are used to ensure that the functions operate as intended. Four test functions are provided for:
1. random_points(): Ensure taht the correct number of random locations are generated
2. get_cdf(): Appropriate bin intervals are used 
3. get_std(): Appropriate bin intervals are used
4. ks2(): size of data1 is a factor n of the size of data2

#### .ll files
Longitudes and latitudes calculated by PyGMT functions are dumped into these various ASCII files.

#### LAB_maps.jpg & CDFs.jpg
The final product of the _Quantitative_analysis.ipynb_ notebook (maps and statistical figures) are saved as JPEG files. The file type can be easily changed by the user.

## Quantitative_analysis Notebook Guide

#### User Input
The user need only to specify a lithospheric depth, z, in km and provide an ASCII data file as the main input of the notebook. 

#### Workflow
After the user has provided a lithospheric depth, z, and input data file, the notebook proceeds to:

1. Import netCDF LAB maps
2. Sort the data into a plottable array
3. Generate 100 CDFs of random onshore locations - random_points()
4. Project a contour line over lithospheric thickness z and dump coordinates into an ASCII file - pygmt.Figure().grdcontour
5. Determine the closest approach for each data point to a contour line and dump as an ASCII file - gmt mapproject
6. For each LAB map, generate CDFs for data and random locations - get_cdf()
7. Calculate standard deviations for the random locations for every LAB map - get_std()
8. Calculate D and p-values for each LAB map - ks2()
9. Project data points on each LAB map
10. For every LAB map, produce cumulative frequency graphs, D-value histograms and p-value violin plots

#### Final Map and Figures
Robinson projection LAB maps are produced using grid data processed by PyGMT (thinnest lithosphere in red and thickest in blue). The  arrays of data points produced earlier (step 2) are used to plot the locations of the data on these maps. 

The cumulative frequencies for distances to contours from data and random locations are displayed as a graph. A vertical line denoting the user-defined contour depth is illustrated as a dot-dash line. The standard deviations of random locations are also shown on the graph along with the mean and the raw number of data points. These graphs ultimately tells us the percentage of data points that can be found within a certain distance from the LAB contour. 

Histograms are used to display D-value sets calculated from the two-sample K-S tests. Means and standard deviations are annotated on the top-right corner of each figure. 

Corresponding p-values are as violin plots. The x-limits are standard across all plots for easy comparison by the user. A small p-value suggests that the two CDFs are selected from populations of different distributions and the spatial relationship between the data and the particular lithospheric thickness is significant. 

## References

Afonso, J. C., F. Salajegheh, W. Szwillus, J. Ebbing & C. Gaina (2019). A global reference model of the lithosphere and upper mantle from joint inversion and analysis of multiple data sets. _Geophysical Journal International_, 217, 1602–1628.

Artemieva, I. M. (2006). Global 1 x 1 thermal model TC1 for the continental lithosphere: Implications for lithosphere secular evolution. _Tectonophysics_, 416, 245–277.

Hoggard, M. J., K. Czarnota, F. D. Richards, D. L. Huston, A. L. Jaques & S. Ghelichkhan (2020). Global distribution of sediment-hosted metals controlled by craton edge stability. _Nature Geoscience_, 13, 504-510. 

Pasyanos, M. E., T. G. Masters, G. Laske & Z. Ma (2014). LITHO1.0: An updated crust and lithospheric model of the Earth. _Journal of Geophysical Research: Solid Earth_, 119, 2153–2173.

Schaeffer, A. J. & S. Lebedev (2013). Global shear speed structure of the upper mantle and transition zone. _Geophysical Journal International_, 194, 417–449.


