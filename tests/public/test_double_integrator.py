import numpy as np

from dasc_lab.dynamics import DoubleIntegrator


def test_double_integrator_dynamics() -> None:
    model = DoubleIntegrator(2)
    state = np.array([[1.0], [-2.0], [0.5], [-1.0]])
    control = np.array([[3.0], [-4.0]])

    np.testing.assert_array_equal(
        model.A,
        np.array(
            [
                [0.0, 0.0, 1.0, 0.0],
                [0.0, 0.0, 0.0, 1.0],
                [0.0, 0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0, 0.0],
            ]
        ),
    )
    np.testing.assert_array_equal(
        model.B,
        np.array(
            [
                [0.0, 0.0],
                [0.0, 0.0],
                [1.0, 0.0],
                [0.0, 1.0],
            ]
        ),
    )
    np.testing.assert_allclose(
        model.f(state, control),
        np.array([[0.5], [-1.0], [3.0], [-4.0]]),
    )
