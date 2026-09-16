import numpy as np

from dasc_lab.dynamics import Unicycle2D


def test_forward_motion() -> None:
    state = np.array([0.0, 0.5, np.pi / 2])
    control = np.array([2.0, 0.25])

    np.testing.assert_allclose(
        Unicycle2D().f(state, control),
        np.array([[0.0], [2.0], [0.25]]),
        atol=1e-12,
    )
