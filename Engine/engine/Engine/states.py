"""
states.py

Defines all legal discrete states for the UQLT Full-System Proof Engine.
States are immutable and exhaustive.
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
    if not isinstance(state, State):
        raise RuntimeError(f"Illegal state: {state}")
