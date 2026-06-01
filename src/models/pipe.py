"""
Contains the Pipes class used to obtain and store
pipe system information from user inputs to be used to calculate
hydraulic analysis.

References
----------
Pumping Station Design, Third Edition
Hydraulic Institute Standards
AWWA Manuals
"""

class Pipe:
    """
    Contains characteristics for a pipe system to be used in
    other classes to be used in calculations for hydraulic analyses.

    Attributes
    ----------
    flow_rate : float
        Flow rate through the pipe (gpm).

    diameter : float
        Internal pipe diameter (in).

    length : float
        Pipe length (ft).

    c_factor : float
        Hazen-Williams roughness coefficient.

    material : string
        user defined pipe material.

    Notes
    -----
    Pipe data is commonly obtained to be used for water and wastewater
    systems under normal operating temperatures.
    """

    def __init__(self,
                 flow_rate: float,
                 diameter: float,
                 length: float,
                 c_factor: float,
                 pipe_material: str
                 ) -> None:
        """
        Initialize Pipe class

        Parameters
        ----------
        flow_rate : float
            Flow rate (gpm).

        diameter : float
            Pipe diameter (in).

        length : float
            Pipe length (ft).

        pipe_material : str
            Identify pipe material

        c_factor : float
            Hazen-Williams roughness coefficient.
        """

    def collect_pipe_data(self, flow_rate, diameter, length, pipe_material):
        """
        Collect pipe data from user input.

        Returns
        -------
        float
            flow_rate (cfs).
            diameter (in).
            length (ft).

        str
            pipe_material (str).

        Raises
        ------
        ValueError
            If diameter is less than or equal to zero.
            If flow_rate is less than or equal to zero.
            If length is less than or equal to zero.

        Notes
        -----
        Uses pipe_material to fetch the c_factor from data stored in a db (dictionary).
        """