import numpy as np

from .linear import LinearDynamics


class SingleIntegrator(LinearDynamics):
    """Class representing a generic single-integrator."""

    def __init__(self, n: int):
        """Define the system matrices for an n-dimensional single integrator, and pass them to the constructor for the LinearSystem superclass."""
        A = np.zeros((n, n))
        B = np.eye(n)

        super().__init__(A, B)
