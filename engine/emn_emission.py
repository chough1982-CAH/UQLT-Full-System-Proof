"""
emn_emission.py

Handles outward-only EMN energy emission from CORE states.
No inward flow, no amplification.
"""

from engine.states import State


def emit_emn(grid, i, j):
    """
    Emit EMN energy from a CORE cell to surrounding cells.
    """
    if grid.get_state(i, j) != State.CORE:
        return

    for ni, nj in grid.neighbors(i, j):
        if grid.get_state(ni, nj) != State.CORE:
            grid.add_energy(ni, nj, 0.1)
