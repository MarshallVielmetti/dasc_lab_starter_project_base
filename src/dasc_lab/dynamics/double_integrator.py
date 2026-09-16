import numpy as np

from .linear import LinearDynamics


class DoubleIntegrator(LinearDynamics):
    """Class representing a generic double integrator."""

    def __init__(self, n: int):
        """Define the system matrices for an n-dimensional double integrator, and pass them to the constructor for the LinearSystem superclass."""
        Z = np.zeros((n, n))
        I = np.eye(n)

        A = np.block([[Z, I], [Z, Z]])
        B = np.block([[Z], [I]])

        super().__init__(A, B)
