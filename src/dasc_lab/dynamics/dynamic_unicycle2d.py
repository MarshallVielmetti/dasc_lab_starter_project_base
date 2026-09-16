import numpy as np

from .dynamics_model import DynamicsModel


class DynamicUnicycle2D(DynamicsModel):
    """Class representing a system with Dynamic 2D Unicycle Dynamics."""

    def f(self, x: np.ndarray, u: np.ndarray) -> np.ndarray:
        """
        X: [x, y, theta, v]^T
        U: [a, omega]^T
        """
        return np.array([x[3] * np.cos(x[2]), x[3] * np.sin(x[2]), u[1], u[0]]).reshape(
            -1, 1
        )
