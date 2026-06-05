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

    pipe_material : string
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

        Raises
        ------
        ValueError
            If diameter is less than or equal to zero.
            If flow_rate is less than or equal to zero.
            If length is less than or equal to zero.
        """
        self._validate_data(
            flow_rate,
            diameter,
            length,
        )
        self.flow_rate = flow_rate
        self.diameter = diameter
        self.length = length
        self.pipe_material = pipe_material

    def __str__(self) -> str:
        """
        Return a human-readable description of the Pipe object.

        Returns
        -------
        str
            Formatted description of the pipe characteristics.

        Notes
        -----
        Intended for display to users and general reporting
        purposes.
        """
        return (
            f"Pipe: {self.pipe_material} "
            f"with diameter {self.diameter} inches "
            f"and length {self.length} feet"
        )

    def __repr__(self) -> str:
        """
        Return an unambiguous string representation of the Pipe object.

        Returns
        -------
        str
            String representation of the Pipe instance suitable
            for debugging and development purposes.

        Notes
        -----
        The representation includes the primary pipe attributes
        used to define the pipe object.
        """
        return (
            f"Pipe(flow_rate={self.flow_rate}, "
            f"diameter={self.diameter}, "
            f"length={self.length}, "
            f"pipe_material='{self.pipe_material}')"
        )

    def _validate_data(self, flow_rate, diameter, length, pipe_material) -> None:
        """Validate the engineering data passed."""
        if diameter <= 0:
            raise ValueError("Diameter must be greater than zero.")
        if flow_rate <= 0:
            raise ValueError("Flow rate must be greater than zero.")
        if length <= 0:
            raise ValueError("Length must be greater than zero.")
        if not pipe_material.strip():
            raise ValueError("Pipe material cannot be empty")

