import numpy as np

from .dynamics_model import DynamicsModel


class Unicycle2D(DynamicsModel):
    """Class representing a system with 2D Unicycle Dynamics."""

    def f(self, x: np.ndarray, u: np.ndarray) -> np.ndarray:
        """
        X: [x, y, theta]^T
        U: [v, omega]^T
        """
        return np.array([u[0] * np.cos(x[2]), u[0] * np.sin(x[2]), u[1]]).reshape(-1, 1)
