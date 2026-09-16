from abc import ABC, abstractmethod

import numpy as np


class DynamicsModel(ABC):
    @abstractmethod
    def f(self, x: np.ndarray, u: np.ndarray) -> np.ndarray:
        """Implement the System Dynamics"""
        pass
