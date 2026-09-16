import numpy as np

from .dynamics_model import DynamicsModel


class PlanarQuadrotor(DynamicsModel):
    """Class representing a 2D planar quadrotor."""

    g = 9.81

    def __init__(self, L: np.float32, M: np.float32, I: np.float32):
        self.L = L
        self.M = M
        self.I = I

    def f(self, x: np.ndarray, u: np.ndarray) -> np.ndarray:
        """
        X: [x, z, theta, x_dot, z_dot, theta_dot]^T
        U: [F_a, F_b]^T
        """

        x_ddot = -1 / self.M * np.sin(x[2]) * (u[0] + u[1])
        z_ddot = -self.g + 1 / self.M * np.cos(x[2]) * (u[0] + u[1])
        theta_ddot = self.L / self.I * (u[1] - u[0])

        return np.array([x[3], x[4], x[5], x_ddot, z_ddot, theta_ddot]).reshape(-1, 1)
