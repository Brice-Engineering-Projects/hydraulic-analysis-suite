"""
Contains the Fitting class used to obtain and store
pipe fitting information from user inputs to be used to calculate
hydraulic analysis.

References
----------
## Standards
* AWWA Manuals
  * M11 Steel Pipe
  * M23 PVC Pipe
  * M41 Ductile Iron Pipe
* Hydraulic Institute Standards
* WEF Design Manuals

## Textbooks and Industry References
* MWH Water Distribution Systems Handbook
* MWH Water Treatment Principles and Design
* Pumping Station Design (3rd Edition)
* Cameron Hydraulic Data
* Crane Technical Paper 410 (TP-410)
"""


class Fitting:
    """
    Contains characteristics for a pipe system to be used in
    other classes to be used in calculations for hydraulic analyses.

    Attributes
    ----------
    diameter_in : float
        Internal pipe diameter (in).

    quantity : float
        user defined quantity of the pipe fittings used in the system.

    fitting_material : string
        user defined pipe material.

    Notes
    -----
    Fitting data is commonly obtained to be used for water and wastewater
    systems under normal operating temperatures used to calculate hydraulic losses.
    """
    pass
