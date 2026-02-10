"""
UQLT Stage Chain Runner

This script executes the full causal sequence defined by
Unified Quantum Life Theory (UQLT), enforcing constraint-only
evolution from VOID to STRUCTURE.

No forces.
No tuning.
No gravity.
Only forbidden states and lawful transitions.
"""

from engine.states import State
from engine.grid import Grid
from engine.transitions import advance_state
from engine.collapse import enforce_collapse
from engine.emn_emission import emit_emn
from engine.valignity import apply_valignity


def run():
    grid = Grid()

    history = []

    while True:
        state_snapshot = grid.snapshot()
        history.append(state_snapshot)

        advance_state(grid)

        if enforce_collapse(grid):
            emit_emn(grid)
            apply_valignity(grid)
            break

        if grid.is_illegal():
            raise RuntimeError("Illegal state reached — simulation halted")

    return history


if __name__ == "__main__":
    run()
