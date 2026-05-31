# Class Template

```python
"""
hazen_williams.py

Contains the HazenWilliams class used to calculate
friction losses in pressurized pipe systems using the
Hazen-Williams equation.

References
----------
Pumping Station Design, Third Edition
Hydraulic Institute Standards
AWWA Manuals
"""


class HazenWilliams:
    """
    Calculates hydraulic characteristics for a pipe system
    using the Hazen-Williams equation.

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

    Notes
    -----
    Hazen-Williams is commonly used for water and wastewater
    systems under normal operating temperatures.

    The equation is empirical and should not be applied to
    fluids other than water without proper justification.
    """

    def __init__(
        self,
        flow_rate: float,
        diameter: float,
        length: float,
        c_factor: float
    ) -> None:
        """
        Initialize Hazen-Williams calculator.

        Parameters
        ----------
        flow_rate : float
            Flow rate (gpm).

        diameter : float
            Pipe diameter (in).

        length : float
            Pipe length (ft).

        c_factor : float
            Hazen-Williams roughness coefficient.
        """
        self.flow_rate = flow_rate
        self.diameter = diameter
        self.length = length
        self.c_factor = c_factor

    def calculate_velocity(self) -> float:
        """
        Calculate flow velocity within the pipe.

        Returns
        -------
        float
            Velocity (ft/s).

        Raises
        ------
        ValueError
            If diameter is less than or equal to zero.

        Notes
        -----
        Uses continuity relationships and unit conversions
        appropriate for gpm and inches.
        """
        pass

    def calculate_headloss(self) -> float:
        """
        Calculate friction headloss using the
        Hazen-Williams equation.

        Returns
        -------
        float
            Friction headloss (ft).

        Raises
        ------
        ValueError
            If input values are invalid.

        Notes
        -----
        Calculates total friction loss over the
        specified pipe length.
        """
        pass

    def calculate_headloss_per_1000ft(self) -> float:
        """
        Calculate normalized headloss.

        Returns
        -------
        float
            Headloss per 1,000 ft of pipe.
        """
        pass

    def summary(self) -> dict:
        """
        Generate a summary of hydraulic results.

        Returns
        -------
        dict
            Dictionary containing calculated values.

        Example
        -------
        {
            "velocity": 4.12,
            "headloss": 15.23,
            "headloss_per_1000ft": 1.52
        }
        """
        pass
```
