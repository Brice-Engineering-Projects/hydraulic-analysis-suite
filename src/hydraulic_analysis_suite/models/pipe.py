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

from hydraulic_analysis_suite.data.pipe_materials import PIPE_MATERIALS
from hydraulic_analysis_suite.data import constants
import math


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
                 flow_rate_gpm: float,
                 diameter_in: float,
                 length_ft: float,
                 pipe_material: str
                 ) -> None:
        """
        Initialize Pipe class

        Parameters
        ----------
        flow_rate_gpm : float
            Flow rate (gpm).

        diameter_in : float
            Pipe diameter (in).

        length_ft : float
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
            flow_rate_gpm,
            diameter_in,
            length_ft,
            pipe_material,
        )
        self.flow_rate_gpm = flow_rate_gpm
        self.diameter_in = diameter_in
        self.length_ft = length_ft
        self.pipe_material = pipe_material
        self._lookup_pipe_material()

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
            f"with diameter {self.diameter_in} inches "
            f"and length {self.length_ft} feet"
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
            f"Pipe(flow_rate={self.flow_rate_gpm}, "
            f"diameter={self.diameter_in}, "
            f"length={self.length_ft}, "
            f"pipe_material='{self.pipe_material}')"
        )

    def _validate_data(
            self,
            flow_rate_gpm:float,
            diameter_in:float,
            length_ft:float,
            pipe_material:str
    ) -> None:
        """
        Validate the engineering data passed.

        Raises
        ------
        ValueError
            If pipe diameter is less than zero.
            If flow rate is less than zero.
            If length is less than zero.
            If pipe material is empty.
            If pipe material is not found in the pipe material database.
        """
        pipe_material = pipe_material.lower().strip()

        if diameter_in <= 0:
            raise ValueError("Diameter must be greater than zero.")
        if flow_rate_gpm <= 0:
            raise ValueError("Flow rate must be greater than zero.")
        if length_ft <= 0:
            raise ValueError("Length must be greater than zero.")
        if not pipe_material:
            raise ValueError("Pipe material cannot be empty")
        if pipe_material not in PIPE_MATERIALS:
            raise ValueError(
                f"Pipe material '{pipe_material}' not found."
            )

    def _lookup_pipe_material(self) -> None:
        """
        Retrieve hydraulic properties associated with
        the selected pipe material and store them on
        the Pipe object.
        """
        pipe_material_data = PIPE_MATERIALS[self.pipe_material]

        self.material_name = pipe_material_data["material_name"]
        self.application = pipe_material_data["application"]
        self.category = pipe_material_data["category"]
        self.c_factor = pipe_material_data["c_factor"]
        self.roughness_ft = pipe_material_data["roughness_ft"]
        self.manning_n = pipe_material_data["manning_n"]

    def summary(self) -> dict:
        """
        Generate a summary of the pipe's attributes and hydraulic properties.

        Returns
        -------
        dict
            A dictionary containing the pipe's attributes and hydraulic properties.
        """

        general_data ={
            'material_name': self.material_name,
            'application': self.application,
            'category': self.category,
        }

        physical_properties ={
            'flow_rate_gpm': self.flow_rate_gpm,
            'diameter_in': self.diameter_in,
            'length_ft': self.length_ft,
            'pipe_material': self.pipe_material,
        }
        hydraulic_properties = {
            'c_factor': self.c_factor,
            'roughness_ft': self.roughness_ft,
            'manning_n': self.manning_n
        }
        derived_properties = {
            'diameter_ft': self.diameter_ft,
            'length_miles': self.length_miles,
            'radius_in': self.radius_in,
            'area_sf': self.area_sf,
            'volume_cf': self.volume_cf,
            'flow_rate_cfs': self.flow_rate_cfs,
            'velocity_fps': self.velocity_fps,
        }
        summary_data = {
            'general_data': general_data,
            'physical_properties': physical_properties,
            'hydraulic_properties': hydraulic_properties,
            'derived_properties': derived_properties
        }
        return summary_data

    @property
    def radius_in(self) -> float:
        """Unit conversion of diameter in inches to radius in inches."""
        radius_in = self.diameter_in / 2
        return radius_in

    @property
    def diameter_ft(self) -> float:
        """unit conversion from inches to feet of the pipe diameter."""
        diameter_ft = self.diameter_in / constants.INCHES_PER_FOOT
        return diameter_ft

    @property
    def length_miles(self) -> float:
        """Unit conversion from the length in feet to miles."""
        length_miles = self.length_ft / constants.FEET_PER_MILE
        return length_miles

    @property
    def flow_rate_cfs(self) -> float:
        """Unit conversion for flow rate from gpm to cfs."""
        flow_cfs = self.flow_rate_gpm * constants.GPM_TO_CFS
        return flow_cfs

    @property
    def area_sf(self) -> float:
        """calculates the cross-sectional area of the pipe."""
        area = math.pi * self.diameter_ft**2 / 4
        return area

    @property
    def volume_cf(self) -> float:
        """Calculates the volume of the pipe."""
        volume = math.pi * self.length_ft * self.diameter_ft**2 / 4
        return volume

    @property
    def velocity_fps(self) -> float:
        """Calculates the velocity in fps."""
        velocity_fps = self.flow_rate_cfs / self.area_sf
        return velocity_fps
