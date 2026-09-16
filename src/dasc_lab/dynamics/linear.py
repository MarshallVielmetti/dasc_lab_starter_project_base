import numpy as np

from .dynamics_model import DynamicsModel


class LinearDynamics(DynamicsModel):
    """Class representing any system with linear dynamics."""

    def __init__(self, A: np.ndarray, B: np.ndarray):
        """Define the Linear System"""
        self.A = A
        self.B = B

    def f(self, x: np.ndarray, u: np.ndarray) -> np.ndarray:
        """Evaluate the System Matrices"""
        return self.A @ x + self.B @ u
