"""
grid.py

Defines the discrete grid used by the UQLT proof engine.
Each cell has a state and an energy value.
"""

import math
import numpy as np

from engine.states import State, validate_state


class Grid:
    def __init__(self, size):
        if size % 2 == 0:
            raise RuntimeError("Grid size must be odd")

        self.size = size
        self.center = size // 2

        self.state = np.full((size, size), State.VOID, dtype=object)
        self.energy = np.zeros((size, size), dtype=float)

    def iter_cells(self):
        for i in range(self.size):
            for j in range(self.size):
                yield i, j

    def get_state(self, i, j):
        return self.state[i, j]

    def set_state(self, i, j, state):
        validate_state(state)
        self.state[i, j] = state
        if state == State.VOID:
            self.energy[i, j] = 0.0

    def get_energy(self, i, j):
        return self.energy[i, j]

    def add_energy(self, i, j, amount):
        self.energy[i, j] += amount
        if self.energy[i, j] < 0:
            raise RuntimeError("Negative energy not allowed")

    def distance_from_center(self, i, j):
        return math.sqrt((i - self.center) ** 2 + (j - self.center) ** 2)
