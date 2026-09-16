import numpy as np

from dasc_lab.dynamics import LinearDynamics


def test_linear_dynamics() -> None:
    system = LinearDynamics(
        np.array([[2.0, -1.0], [0.0, 3.0]]),
        np.array([[1.0, 0.0], [0.0, 2.0]]),
    )
    state = np.array([[1.0], [2.0]])
    control = np.array([[3.0], [-1.0]])

    np.testing.assert_allclose(
        system.f(state, control),
        np.array([[3.0], [4.0]]),
    )
