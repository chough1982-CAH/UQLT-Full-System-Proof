"""
transitions.py

Defines all legal state-to-state transitions.
No spontaneous jumps. No skips. No reversals.
"""

from engine.states import State


LEGAL_TRANSITIONS = {
    State.VOID: [State.STATIC],
    State.STATIC: [State.RADIO],
    State.RADIO: [State.RADIANT],
    State.RADIANT: [State.PLASMA],
    State.PLASMA: [State.HELIUM],
    State.HELIUM: [State.CORE],
    State.CORE: []
}


def is_transition_allowed(current_state, next_state):
    return next_state in LEGAL_TRANSITIONS[current_state]
