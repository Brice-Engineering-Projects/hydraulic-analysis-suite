


class UserInput:
    """Collects user input data"""

    def __init__(self, flow_rate: float, diameter: float, length: float, c_factor: float, pipe_material: str):
        """Initialization for the PipeValidation"""
        self.diameter = diameter
        self.flow_rate = flow_rate
        self.length = length
        self.pipe_material = pipe_material

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
        Uses pipe_material to fetch the c_factor from data stored in a data (dictionary).
        """
        pass
