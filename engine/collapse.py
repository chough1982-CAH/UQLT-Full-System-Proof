"""
collapse.py

Implements helium-dominance-driven collapse for the
UQLT Full-System Proof Engine.

Collapse is NOT probabilistic.
Collapse is NOT optional.
Collapse occurs when helium-family dominance exceeds the admissible threshold.

Failure to collapse when triggered halts the system.
"""

import numpy as np

from engine.states import State, is_helium_family, is_core
from config.constants import (
    COLLAPSE_HELIUM_THRESHOLD,
    MAX_UNIT_ENERGY
)


def compute_local_helium_fraction(grid, i, j, radius=1):
    """
    Compute local helium-family fraction within a neighborhood radius.
    """
    size = grid.size
    helium_count = 0
    total_count = 0

    for di in range(-radius, radius + 1):
        for dj in range(-radius, radius + 1):
            ni, nj = i + di, j + dj
            if 0 <= ni < size and 0 <= nj < size:
                state = grid.get_state(ni, nj)
                if state != State.VOID:
                    total_count += 1
                    if is_helium_family(state):
                        helium_count += 1

    if total_count == 0:
        return 0.0

    return helium_count / total_count


def collapse_cell(grid, i, j):
    """
    Force collapse of a cell into a CORE.
    """
    grid.set_state(i, j, State.CORE)
    grid.set_energy(i, j, MAX_UNIT_ENERGY["CORE"])


def enforce_collapse(grid, radius=1):
    """
    Enforce helium-dominance collapse across the grid.

    For each non-core cell:
    - Compute local helium-family dominance
    - If dominance exceeds threshold, collapse MUST occur
    """
    collapse_events = []

    for i, j in grid.iter_cells():
        state = grid.get_state(i, j)

        # Skip voids and existing cores
        if state == State.VOID or is_core(state):
            continue

        helium_fraction = compute_local_helium_fraction(grid, i, j, radius)

        if helium_fraction >= COLLAPSE_HELIUM_THRESHOLD:
            collapse_events.append((i, j))

    # Execute collapse events
    for i, j in collapse_events:
        collapse_cell(grid, i, j)

    return len(collapse_events)
