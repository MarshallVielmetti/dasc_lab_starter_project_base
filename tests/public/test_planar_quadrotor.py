import numpy as np

from dasc_lab.dynamics import PlanarQuadrotor


def test_planar_quadrotor_dynamics() -> None:
    model = PlanarQuadrotor(L=0.25, M=2.0, I=0.5)
    state = np.array([1.0, -2.0, np.pi / 6, 3.0, -4.0, 0.2])
    control = np.array([12.0, 8.0])

    np.testing.assert_allclose(
        model.f(state, control),
        np.array(
            [
                [3.0],
                [-4.0],
                [0.2],
                [-5.0],
                [-9.81 + 5.0 * np.sqrt(3.0)],
                [-2.0],
            ]
        ),
        atol=1e-12,
    )

    hover_control = np.array([model.M * model.g / 2, model.M * model.g / 2])
    np.testing.assert_allclose(
        model.f(np.zeros(6), hover_control),
        np.zeros((6, 1)),
        atol=1e-12,
    )
