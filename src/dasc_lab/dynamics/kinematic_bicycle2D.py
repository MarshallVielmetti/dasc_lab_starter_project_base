import numpy as np

from .dynamics_model import DynamicsModel


class KinematicBicycle2D(DynamicsModel):
    """Class representing a system with Kinematic 2D Bicycle."""

    def __init__(self, L: np.float32):
        """
        L: Bicycle Length
        """
        self.L = L

    def f(self, x: np.ndarray, u: np.ndarray) -> np.ndarray:
        """
        X: [x, y, theta, delta]^T -- theta is heading angle, delta is steering angle
        U: [v, phi]^T -- velocity and steering rate
        """

        theta_dot = u[0] * np.tan(x[3]) / self.L

        return np.array(
            [x[0] * np.cos(x[2]), x[1] * np.sin(x[2]), theta_dot, u[1]]
        ).reshape(-1, 1)
