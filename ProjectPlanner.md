# EMSC4033 project plan template

## Quantifying spatial relationships of ore deposits and lithospheric depths

## Executive summary

Recent studies have revealed that several mineral systems show general spatial associations with plate and craton margins. However, the quantitative assessment of these relationships are not well established. In this project, I plan to write a Jupyter notebook that performs geodesic distance calculations and the relevant quantitative tests and upload the results to GitHub as:
1) raw data 
2) a sample notebook displaying output 
3) python scripts with documented functions
4) tests

**Example:** _(this is based on the seismic monitoring dashboard that Louis showed). Seismic stations can be used to monitor human noise over the course of the day. Some seismometers stream data live to a server and so this processing can be done in near-real time. In this project I plan to build an online dashboard which processes the data once a day and uploads the results to github as 1) raw data, 2) an image that can be embedded in websites, 3) an updating csv table in github. I also plan to use the github "actions" engine to provide all the necessary processing power._

## Goals

- Draw contours which represent the surface projection of a pre-defined lithospheric depth (based on various seismic tomography models).
- Calculate the geodesic distance between each deposit point and the nearest contour and present as cumulative distribution functions (CDFs).
- Perform two-sample kolmogorov-Smirnov (K-S) tests to assess spatial correlations. Results displayed graphically
- Compare between results of both models
- Present well-documented functions that are easy to use. 

(Write things that you can assess whether they have been accomplished. For example, a goal like “improve visualisation of ocean output” is vague... But a goal that reads “implement functionality to plot streamlines of horizontal velocities in various slices from 3D ocean output” is specific enough.)

## Background and Innovation  

Initial ground selection is arguably the most crucial aspect of mineral exploration, as failure to initially identify fertile regions results in waste of all future financial input (McCuaig, Beresford and Hronsky, 2010). Recent exploration methods have endeavoured to resolve this challenge by considering a more holistic perspective to identify prospective regions and draw relationships between mineralisation and its underlying tectonic and plate-scale processes (Huston et al., 2016). This approach is guided by the understanding that ore deposits are small-scale expressions of a variety of Earth processes that operate on different spatial and temporal scales (McCuaig, Beresford and Hronsky, 2010). Mineral systems that are active and geologically young are generally associated with plate and craton margins, both spatially and genetically (Huston et al., 2016). Even deposits from the geological past commonly occur at sites that host former crustal boundaries (Huston et al., 2016). By establishing the first-order geological controls that govern the spatiotemporal distribution of these mineral systems, the predictive power for identifying fertile regions can be increased substantially.

The process of identifying depth contours, calculating geodesic distances an performing statistical tests can also be completed using basic functions in Python. However, the main limitation of this approach is its considerably lengthy runtime. Therefore, my code will generalise the use of specialised packages so that people can input their own data of choice without necessarily the need to understand fully the underlying workings of the code.

_Give more details on the scientific problem that you are working on and how this project will advance the discipline or help with your own research.
(Where applicable, describe how people have been achieving this goal up to now, talk about existing packages, their limitations, whether you can generalise something to help other people use your code)._

## Resources & Timeline

- Several seismic tomography models will be used and compared against one another. These are SL2013sv, LITHO1.0, A2006 and Afonso2019.
- The project will be written in Python code on Jupyter.
- Contours and geodesic distances will be calculated using the Python interface of Generic Mapping Tools (GMT) - PyGMT.
- Statistical tests will be conducted using the existing Scipy package.

This project has been a work in progress for the last few weeks and is on track to be completed in the time available. It will be important for future personal use, so I intend to continually update the repository to reflect more efficient and presentable improvements.


_What do you have at your disposal already that will help the project along. Did you convince somebody else to help you ? Are there already some packages you can build upon. What makes it possible to do this project in the time available. Do you intend to continue this project in the future ?_

(For example:
  - I’ll be using data of X from satellite and then also data from baby blue seals…
  - I’ll step on existing package Y and build extra functionality on top of class W.
  - I’ll use textbook Z that describes algorithms a, b, c
  - …
)

## Testing, validation, documentation

**Note:** You need to think about how you will know your code is correct and achieves the goals that are set out above (specific tests that can be implemented automatically using, for example, the `assert` statement in python.)  It can be really helpful if those tests are also part of the documentation so that when you tell people how to do something with the code, the example you give is specifically targetted by some test code.

_Provide some specific tests with values that you can imagine `assert`ing_

## References 

Huston, D. L. et al. (2016) ‘Tectono-metallogenic systems — The place of mineral systems within tectonic evolution, with an emphasis on Australian examples’, Ore Geology Reviews, 76(September 2015), pp. 168–210. doi: 10.1016/j.oregeorev.2015.09.005.

McCuaig, T. C., Beresford, S. and Hronsky, J. (2010) ‘Translating the mineral systems approach into an effective exploration targeting system’, Ore Geology Reviews, 38(3), pp. 128–138. doi: 10.1016/j.oregeorev.2010.05.008.
