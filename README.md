# EMSC4033-Project
The repository provides a notebook to perform quantitative analyses on geodesic distances between lithospheric thickness and the data of the user's choice. The data will be plotted on various lithosphere-asthenosphere boundary (LAB) maps, and statistical histograms and violinplots will be produced.

This markdown file includes a guide to navigate the repository and explains the workflow of the *Quantitative_analysis.ipynb* notebook.

## Navigating the Repository
### Quantitative_analysis.ipynb
This is the main product of the repository - a notebook which displays the workflow and presents the final figures that are interpretable to the user. The user chooses a datafile to upload (ASCII format) and defines a lithospheric depth (km) of interest. Users may also customise maps and figures, which will be saved in the format of the user's choice. 

_This notebook is essentially a sample input that analyses teh relationship between magmatic nickel sulphide deposits and a lithospheric depth of 170 km. Final figures are saved as JPEG files_

### src
The *src* (source) folder contains all the "inner-workings" of the *Quantitative_analysis.ipynb* notebook. It contains a *data* folder that holds NetCDF files of the four LAB maps used in the notebook, as well as a CSV file containing data of global magmatic nickel occurrences for the sample input, whose sources are as follows: 

#### Lab maps:
- SL2013sv - Upper-mantle shear wave tomography (Schaeffer & Lebedev, 2013)
- LITHO1.0 - Surface wave tomography (Pasyanos et al., 2014)
- A2006 - Surface heat flow measurements (Artemieva, 2006)
- LithoRef18 - Joint inversion of seismic, potential field and geochemical data (Afonso et al., 2019)


#### Deposit data:
- Global magmatic nickel deposits (Hoggard et al., 2020)

*dependencies.py* imports all the packages required to run the notebook. This file is called at the beginning of the notebook.

*functions.py* contains various functions that conducts the workflow of the notebook. Lengthy or repeatedly-used code are written as functions to minimise the length of the main notebook. This file is called at the beginning of the notebook.

### Tests

## Quantitative_analysis Notebook Guide

## References

Afonso, J. C., F. Salajegheh, W. Szwillus, J. Ebbing & C. Gaina (2019). A global reference model of the lithosphere and upper mantle from joint inversion and analysis of multiple data sets. _Geophysical Journal International_, 217, 1602–1628.

Artemieva, I. M. (2006). Global 1 x 1 thermal model TC1 for the continental lithosphere: Implications for lithosphere secular evolution. _Tectonophysics_, 416, 245–277.

Hoggard, M. J., K. Czarnota, F. D. Richards, D. L. Huston, A. L. Jaques & S. Ghelichkhan (2020). Global distribution of sediment-hosted metals controlled by craton edge stability. _Nature Geoscience_, 13, 504-510. 

Pasyanos, M. E., T. G. Masters, G. Laske & Z. Ma (2014). LITHO1.0: An updated crust and lithospheric model of the Earth. _Journal of Geophysical Research: Solid Earth_, 119, 2153–2173.

Schaeffer, A. J. & S. Lebedev (2013). Global shear speed structure of the upper mantle and transition zone. _Geophysical Journal International_, 194, 417–449.


