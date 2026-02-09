"""
emn_emission.py

Implements EMN (Electro-Magno-Nucleic) energy emission from cores
and its outward propagation through containment.

Key enforced properties:
- Emission originates ONLY from cores
- Propagation is outward-only
- Energy weakens monotonically with distance
- No inward flow, no amplification
"""

import numpy as np

from engine.states import State, is_core
from config.constants import CORE_EMISSION_RATE, C_SQUARED_MAX_MOTION
from config.parameters import GRID_SIZE


def emit_from_cores(grid):
    """
    Emit EMN energy from all core cells.

    Cores do not intake energy.
    They emit outward EMN energy into neighboring cells.
    """
    emissions = []

    for i, j in grid.iter_cells():
        if is_core(grid.get_state(i, j)):
            emissions.append((i, j))

    for ci, cj in emissions:
        _emit_single_core(grid, ci, cj)


def _emit_single_core(grid, ci, cj):
    """
    Emit EMN energy from a single core radially.
    """
    for i, j in grid.iter_cells():
        if (i, j) == (ci, cj):
            continue

        r = grid.distance_from_center(i, j)
        if r == 0:
            continue

        # Inverse radial weakening (monotonic)
        emission = CORE_EMISSION_RATE / r

        # Enforce max admissible energy motion
        emission = min(emission, C_SQUARED_MAX_MOTION)

        grid.add_energy(i, j, emission)


def compute_radial_energy_profile(grid):
    """
    Compute mean energy as a function of radial distance from center.
    """
    radial_bins = {}

    for i, j in grid.iter_cells():
        r = int(round(grid.distance_from_center(i, j)))
        radial_bins.setdefault(r, []).append(grid.get_energy(i, j))

    return {
        r: float(np.mean(values))
        for r, values in radial_bins.items()
    }
