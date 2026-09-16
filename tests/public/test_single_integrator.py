import numpy as np

from dasc_lab.dynamics import SingleIntegrator


def test_single_integrator_dynamics() -> None:
    model = SingleIntegrator(2)
    state = np.array([[1.0], [-2.0]])
    control = np.array([[0.5], [3.0]])

    np.testing.assert_array_equal(model.A, np.zeros((2, 2)))
    np.testing.assert_array_equal(model.B, np.eye(2))
    np.testing.assert_allclose(
        model.f(state, control),
        control,
    )
