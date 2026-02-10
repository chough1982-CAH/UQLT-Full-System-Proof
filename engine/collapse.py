"""
collapse.py

Implements helium-dominance collapse logic.
When local conditions exceed collapse thresholds,
structure transitions toward a core state.
"""

from engine.states import State
from engine.grid import Grid


def apply_collapse(grid: Grid, helium_threshold):
    """
    Enforce collapse where helium dominates.
    """
    for i, j in grid.iter_cells():
        state = grid.get_state(i, j)
        energy = grid.get_energy(i, j)

        if state == State.HELIUM and energy >= helium_threshold:
            grid.set_state(i, j, State.CORE)
