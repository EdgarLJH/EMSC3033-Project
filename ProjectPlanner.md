# EMSC4033 project plan template

## Quantifying spatial relationships of ore deposits and lithospheric depths

## Executive summary

Recent studies have revealed that several mineral systems show general spatial associations with plate and craton margins. However, the quantitative assessment of these relationships are not well established. In this project, I plan to write a Jupyter notebook that performs geodesic distance calculations and the relevant quantitative tests and upload the results to GitHub as:
1) raw data 
2) a sample notebook displaying output 
3) python scripts with documented functions and dependencies
4) tests

## Goals

- Generate contours which represent the surface projection of a pre-defined lithospheric depth (based on various models of the lithosphere-asthenosphere boundary, LAB).
- Calculate the geodesic distance between each deposit point and the nearest contour and present as cumulative distribution functions (CDFs).
- Perform two-sample kolmogorov-Smirnov (K-S) tests to assess spatial correlations. Results displayed graphically
- Compare results of the different LAB maps
- Generalise notebook for easy-use by the public. 

## Background and Innovation  

Initial ground selection is arguably the most crucial aspect of mineral exploration, as failure to initially identify fertile regions results in waste of all future financial input (McCuaig, Beresford and Hronsky, 2010). Recent exploration methods have endeavoured to resolve this challenge by considering a more holistic perspective to identify prospective regions and draw relationships between mineralisation and its underlying tectonic and plate-scale processes (Huston et al., 2016). This approach is guided by the understanding that ore deposits are small-scale expressions of a variety of Earth processes that operate on different spatial and temporal scales (McCuaig, Beresford and Hronsky, 2010). Mineral systems that are active and geologically young are generally associated with plate and craton margins, both spatially and genetically (Huston et al., 2016). Even deposits from the geological past commonly occur at sites that host former crustal boundaries (Huston et al., 2016). By establishing the first-order geological controls that govern the spatiotemporal distribution of these mineral systems, the predictive power for identifying fertile regions can be increased substantially.

The process of identifying depth contours, calculating geodesic distances an performing statistical tests can also be completed using basic functions in Python. However, the main limitation of this approach is its considerably lengthy runtime. Therefore, my code will use a specialised package, Generic Mapping Tools (GMT), which is able to perform most of these calculations in exceedingly short amount of time. However, documentations for its Python interface, PyGMT, has not been updated to reflect the use of the latest few versions, so my code will generalise the use of PyGMT and simplify considerably the approach for people to make use of its capabilities.

## Resources & Timeline

- Several LAB models will be used and compared against one another. These models are each derived from upper-mantle shear wave tomography (Schaeffer & Lebedev, 2013), surface wave tomography (Pasyanos et al., 2014), surface heat flow measurements (Artemieva, 2006) and  joint inversion of seismic, potential field and geochemical data (Afonso et al., 2019).
- The project will be written in Python code on Jupyter.
- Contours and geodesic distances will be calculated using the Python interface of Generic Mapping Tools (GMT) - PyGMT.
- Statistical tests will be conducted using the existing Scipy package and a combination of numpy functions.

This project has been a work in progress for the last few weeks and is on track to be completed in the time available. It will be important for upcoming research, so I intend to continually update the repository to reflect improvements in efficiency and presentation.

## Testing, validation, documentation

**Tests**
- The correct number of random locations are generated.
- Correct input file types for get_cdf and get_std functions. 
- The correct length of data is used as argument for the K-S test. 

## References 

Afonso, J. C., F. Salajegheh, W. Szwillus, J. Ebbing, & C. Gaina (2019). A global reference model of the lithosphere and upper mantle from joint inversion and analysis of multiple data sets. _Geophysical Journal International_, 217, 1602–1628.

Artemieva, I. M. (2006). Global 1 x 1 thermal model TC1 for the continental lithosphere: Implications for lithosphere secular evolution. _Tectonophysics_, 416, 245–277.

Huston, D. L., T. P. Mernagh, M. P. Doublier, M. Fiorentini, D. C. Champion, A. L. Jaques, K. Czarnota, R. Cayley, R. Skirrow & E. Bastrakov (2016). Tectono-metallogenic systems — The place of mineral systems within tectonic evolution, with an emphasis on Australian examples. _Ore Geology Reviews_, 76, 168-210. 

McCuaig, T. C., S. Beresford, & J. Hronsky (2010). Translating the mineral systems approach into an effective exploration targeting system. _Ore Geology Reviews_, 38(3), 128-138. 

Pasyanos, M. E., T. G. Masters, G. Laske, & Z. Ma (2014). LITHO1.0: An updated crust and lithospheric model of the Earth. _Journal of Geophysical Research: Solid Earth_, 119, 2153–2173.

Schaeffer, A. J. & S. Lebedev (2013). Global shear speed structure of the upper mantle and transition zone. _Geophysical Journal International_, 194, 417–449.
