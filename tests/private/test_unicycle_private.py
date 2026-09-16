import numpy as np

from dasc_lab.dynamics import Unicycle2D


def test_forward_motion_accepts_negative_speed() -> None:
    state = np.array([[3.0], [-0.25], [0.0]])
    control = np.array([[-1.5], [-0.25]])

    np.testing.assert_allclose(
        Unicycle2D().f(state, control),
        np.array([[-1.5], [0.0], [-0.25]]),
        atol=1e-12,
    )
