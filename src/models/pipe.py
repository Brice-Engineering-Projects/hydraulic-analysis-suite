"""
Contains the Pipe class used to obtain and store
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

        Raises
        ------
        ValueError
            If diameter is less than or equal to zero.
            If flow_rate is less than or equal to zero.
            If length is less than or equal to zero.
            If c_factor is less than or equal to zero.

        """
        self._validate_data(
            flow_rate,
            diameter,
            length,
            c_factor
        )
        self.flow_rate = flow_rate
        self.diameter = diameter
        self.length = length
        self.c_factor = c_factor
        self.pipe_material = pipe_material

    def _validate_data(self, flow_rate, diameter, length, c_factor):
        """Validate the engineering data passed."""
        if diameter <= 0:
            raise ValueError("Diameter must be greater than zero.")
        if flow_rate <= 0:
            raise ValueError("Flow rate must be greater than zero.")
        if length <= 0:
            raise ValueError("Length must be greater than zero.")
        if c_factor <= 0:
            raise ValueError("C Factor must be greater than zero.")
