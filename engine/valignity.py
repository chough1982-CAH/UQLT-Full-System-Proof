"""
valignity.py

Implements Valignity mechanics for the UQLT Full-System Proof Engine.

Valignity governs:
- radial density ordering
- emergence of stable hover / neutral bands
- surface equilibrium as a balance condition

No gravity, attraction, or external forces are used.
"""

import numpy as np

from engine.states import (
    State,
    HELIUM_FAMILY,
    LIGHT_STATES,
    HEAVY_STATES,
    is_core,
)
from config.constants import (
    V_VALIGNITY,
    MIN_STABLE_SHELL_ENERGY,
    FRAGMENTATION_THRESHOLD,
)


# =========================
# Density Weights
# =========================

STATE_DENSITY_WEIGHT = {
    State.CORE: 5.0,
    State.HELIUM: 3.0,
    State.HELIUM_FRAGMENT: 2.0,
    State.HEAVY: 2.5,
    State.PLASMA: 1.5,
    State.RADIANT: 1.2,
    State.RADIO: 0.8,
    State.STATIC: 0.5,
    State.HYDROGEN: 0.2,
    State.VOID: 0.0,
}


# =========================
# Density Metrics
# =========================

def compute_radial_density(grid):
    """
    Compute effective density as a function of radius.

    Density is defined as:
    sum(state_weight * energy) / number_of_cells
    """
    radial_bins = {}

    for i, j in grid.iter_cells():
        r = int(round(grid.distance_from_center(i, j)))
        state = grid.get_state(i, j)
        energy = grid.get_energy(i, j)

        weight = STATE_DENSITY_WEIGHT[state]
        radial_bins.setdefault(r, []).append(weight * energy)

    return {
        r: float(np.mean(values))
        for r, values in radial_bins.items()
    }


# =========================
# Hover Band Detection
# =========================

def detect_hover_bands(grid, tolerance=0.05):
    """
    Detect stable radial hover / neutral bands.

    A band is stable if:
    - mean energy is above minimum shell energy
    - density gradient is approximately zero
    """
    density = compute_radial_density(grid)
    radii = sorted(density.keys())

    hover_bands = []

    for r in radii[1:-1]:
        d_prev = density[r] - density[r - 1]
        d_next = density[r + 1] - density[r]

        if (
            abs(d_prev) < tolerance
            and abs(d_next) < tolerance
            and density[r] >= MIN_STABLE_SHELL_ENERGY
        ):
            hover_bands.append(r)

    return hover_bands


# =========================
# Surface Equilibrium
# =========================

def detect_surface_radius(grid):
    """
    Detect the emergent surface radius.

    The surface is defined where:
    - inward EMN-supported density
    - outward fragmentation tendency

    reach equilibrium.
    """
    density = compute_radial_density(grid)

    for r, rho in sorted(density.items()):
        if rho <= FRAGMENTATION_THRESHOLD:
            return r

    return None


# =========================
# Valignity Enforcement Check
# =========================

def validate_valignity_ordering(grid):
    """
    Ensure radial density does not invert.

    Returns True if ordering is valid.
    Raises RuntimeError if inversion occurs.
    """
    density = compute_radial_density(grid)
    radii = sorted(density.keys())

    for r1, r2 in zip(radii[:-1], radii[1:]):
        if density[r2] > density[r1] * V_VALIGNITY:
            raise RuntimeError(
                f"Valignity violation: density inversion at radius {r1}->{r2}"
            )

    return True
