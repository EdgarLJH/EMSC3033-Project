# EMSC4033-Project
The repository provides a notebook to perform quantitative analyses on geodesic distances between lithospheric thickness and the data of the user's choice. The data will be plotted on various lithosphere-asthenosphere boundary (LAB) maps, and statistical histograms and violinplots will be produced.

This markdown file includes a guide to navigate the repository and explains the workflow of the *Quantitative_analysis.ipynb* notebook.

## Navigating the Repository
#### Quantitative_analysis.ipynb
This is the main product of the repository - a notebook which displays the workflow and presents the final figures that are interpretable to the user. The user chooses a datafile to upload (ASCII format) and defines a lithospheric depth (km) of interest. Users may also customise maps and figures, which will be saved in the format of the user's choice. 

_This notebook is essentially a sample input that analyses teh relationship between magmatic nickel sulphide deposits and a lithospheric depth of 170 km. Final figures are saved as JPEG files_

#### src
The *src* (source) folder contains all the "inner-workings" of the *Quantitative_analysis.ipynb* notebook. It contains a *data* folder that holds NetCDF files of the four LAB maps used in the notebook (SL2013sv, LITHO1.0, A2006, LithoRef18), as well as a CSV file containing data of global magmatic nickel occurrences for the sample input. 

*dependencies.py* imports all the packages required to run the notebook. This file is called at the beginning of the notebook.

*functions.py* contains various functions that conducts the workflow of the notebook. Lengthy or repeatedly-used code are written as functions to minimise the length of the main notebook. This file is called at the beginning of the notebook.

#### Tests

## Quantitative_analysis Notebook Guide

