"""
valignity.py

Implements Valignity ordering.
Determines vertical / radial equilibrium and neutral (hover) bands.
"""

from engine.states import State


def apply_valignity(grid):
    """
    Apply Valignity ordering across the grid.
    Higher-density states sink toward the core,
    lower-density states stabilize outward.
    """
    center = grid.center

    for i, j in grid.iter_cells():
        state = grid.get_state(i, j)

        if state in (State.VOID, State.STATIC):
            continue

        r = grid.distance_from_center(i, j)

        # Simple ordering rule (non-force, constraint-based)
        if r < center and state == State.PLASMA:
            grid.set_state(i, j, State.HELIUM)
