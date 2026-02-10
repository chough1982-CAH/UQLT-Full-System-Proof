"""
states.py

Defines the allowed discrete states for the UQLT system.
States are labels only — no behavior is encoded here.
"""

from enum import Enum, auto


class State(Enum):
    VOID = auto()
    STATIC = auto()
    RADIO = auto()
    RADIANT = auto()
    PLASMA = auto()
    HELIUM = auto()
    COLLAPSE = auto()
    CORE = auto()
