"""
UQLT EMN Quantification Runner

Runs the EMN emission phase after core formation.
Quantifies EMN output as a function of collapse resolution.
"""

from engine.grid import Grid
from engine.collapse import enforce_collapse
from engine.emn_emission import compute_emn_output


def run():
    grid = Grid()

    while True:
        collapsed = enforce_collapse(grid)

        if collapsed:
            break

        if grid.is_illegal():
            raise RuntimeError("Illegal state detected during collapse")

    emn_value = compute_emn_output(grid)
    return emn_value


if __name__ == "__main__":
    run()
