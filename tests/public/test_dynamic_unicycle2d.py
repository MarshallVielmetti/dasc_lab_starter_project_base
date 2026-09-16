import numpy as np

from dasc_lab.dynamics import DynamicUnicycle2D


def test_dynamic_unicycle2d_dynamics() -> None:
    state = np.array([1.0, -2.0, np.pi / 2, 3.0])
    control = np.array([0.5, -0.25])

    np.testing.assert_allclose(
        DynamicUnicycle2D().f(state, control),
        np.array([[0.0], [3.0], [-0.25], [0.5]]),
        atol=1e-12,
    )
