"""
UQLT Collapse Engine Runner

Executes the collapse-only engine under strict constraint rules.
Used to validate inevitability of collapse without scripting.
"""

from engine.grid import Grid
from engine.collapse import enforce_collapse


def run():
    grid = Grid()

    while True:
        collapsed = enforce_collapse(grid)

        if collapsed:
            break

        if grid.is_illegal():
            raise RuntimeError("Illegal state detected during collapse")

    return grid


if __name__ == "__main__":
    run()
