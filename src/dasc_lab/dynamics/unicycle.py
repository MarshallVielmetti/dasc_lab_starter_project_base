"""A minimal completed dynamics implementation for the first lab exercise."""


class UnicycleDynamics:
    """Evaluate the simple forward-motion derivative used by the example lab."""

    def f(self, state: tuple[float, float], speed: float) -> tuple[float, float]:
        """Return the forward speed while preserving the second state component."""

        return (speed, state[1])
