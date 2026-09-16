import numpy as np

from dasc_lab.dynamics import KinematicBicycle2D


def test_kinematic_bicycle2d_dynamics() -> None:
    state = np.array([1.0, -2.0, np.pi / 2, np.pi / 4])
    control = np.array([3.0, 0.5])

    np.testing.assert_allclose(
        KinematicBicycle2D(2.0).f(state, control),
        np.array([[0.0], [3.0], [1.5], [0.5]]),
        atol=1e-12,
    )
