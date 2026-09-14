from dasc_lab.dynamics import UnicycleDynamics


def test_forward_motion_accepts_negative_speed() -> None:
    assert UnicycleDynamics().f((3.0, -0.25), -1.5) == (-1.5, -0.25)
