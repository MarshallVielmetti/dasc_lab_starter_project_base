import numpy as np

from dasc_lab.dynamics import Unicycle2D


def test_forward_motion_accepts_negative_speed() -> None:
    assert Unicycle2D().f(
        np.array([3.0, -0.25]).reshape(-1, 1), np.array([-1.5]).reshape(-1, 1)
    ) == np.array([-1.5, -0.25]).reshape(-1, 1)
