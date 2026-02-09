"""
states.py

Defines all legal discrete states used by the
UQLT Full-System Proof Engine.

States are strictly enforced.
No undefined or intermediate states are permitted.
"""

from enum import Enum


class State(Enum):
    VOID = 0
    STATIC = 1
    RADIO = 2
    RADIANT = 3
    PLASMA = 4
    HELIUM = 5
    CORE = 6


def validate_state(state):
    """
    Enforce legal state existence.
    """
    if not isinstance(state, State):
        raise ValueError(f"Illegal state: {state}")
