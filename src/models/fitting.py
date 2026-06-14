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

    quantity : int
        user defined quantity of the pipe fittings used in the system.

    fitting_material : string
        user defined pipe material.

    Notes
    -----
    Fitting data is commonly obtained to be used for water and wastewater
    systems under normal operating temperatures used to calculate hydraulic losses.
    """

    def __init__(self,
                 diameter_in: float,
                 quantity: int,
                 fitting_material: str
                 ) -> None:
        """
        Initialize Fitting class

        Parameters
        ----------
        diameter_in : float
            Pipe diameter (in).

        quantity : int
            User defined quantity of fittings.

        fitting_material : str
            Identify fitting material

        Raises
        ------
        ValueError
            If diameter_in is less than or equal to zero.
            If quantity is less than or equal to zero.
        """
        if diameter_in <= 0:
            raise ValueError("diameter_in must be greater than zero.")
        if quantity <= 0:
            raise ValueError("quantity must be greater than zero.")
        self.diameter_in = diameter_in
        self.quantity = quantity
        self.fitting_material = fitting_material

    def __str__(self) -> str:
        """
        Return a human-readable description of the Fitting object.

        Returns
        -------
        str
            Formatted description of the fitting characteristics.

        Notes
        -----
        Intended for display to users and general reporting
        purposes.
        """
        return (
            f"Fitting: {self.fitting_material} "
            f"with diameter {self.diameter_in} inches, "
            f"quantity {self.quantity}"
        )

    def __repr__(self) -> str:
        """
        Return an unambiguous string representation of the Fitting object.

        Returns
        -------
        str
            String representation of the Fitting instance suitable
            for debugging and development purposes.

        Notes
        -----
        The representation includes the primary fitting attributes
        used to define the fitting object.
        """
        return (
            f"Fitting(diameter={self.diameter_in}, "
            f"quantity={self.quantity}, "
            f"fitting_material={self.fitting_material})"
        )
