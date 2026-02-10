"""
transitions.py

Defines the strict allowed state transitions for the UQLT system.
No transition outside this map is permitted.
"""

from .states import State


# Canonical ordered transitions (no skips allowed)
ALLOWED_TRANSITIONS = {
    State.VOID: State.STATIC,
    State.STATIC: State.RADIO,
    State.RADIO: State.RADIANT,
    State.RADIANT: State.PLASMA,
    State.PLASMA: State.HELIUM,
    State.HELIUM: State.COLLAPSE,
    State.COLLAPSE: State.CORE,
}


def next_state(current_state: State) -> State | None:
    """
    Returns the next allowed state.
    If no transition exists, returns None.
    """
    return ALLOWED_TRANSITIONS.get(current_state)
