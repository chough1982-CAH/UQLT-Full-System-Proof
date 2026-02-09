"""
transitions.py

Defines legal state transitions for the UQLT Full-System Proof Engine.

This module does not "decide outcomes" by tuning.
It enforces the stage-chain ordering and the legal transitions when
energy saturation thresholds are met.

If a state reaches saturation and no legal transition exists, the system halts.
"""

from engine.states import State
from config.constants import MAX_UNIT_ENERGY


# =========================
# Stage Chain Transitions
# =========================

STAGE_NEXT = {
    State.VOID: State.STATIC,
    State.STATIC: State.RADIO,
    State.RADIO: State.RADIANT,
    State.RADIANT: State.PLASMA,
    State.PLASMA: State.HELIUM,  # plasma closure forms He-4 class
}

# =========================
# Helium-family Transitions
# =========================

def helium_split(state: State, energy: float) -> State:
    """
    Helium splitting / diversification.

    In this engine, HELIUM_FRAGMENT covers:
    - He-3 / D / T class fragments (rare variants are handled probabilistically elsewhere)

    We keep splitting logic lawful: it occurs when HELIUM is saturated.
    """
    if state == State.HELIUM and energy >= MAX_UNIT_ENERGY["HELIUM"]:
        return State.HELIUM_FRAGMENT
    return state


def fragment_to_hydrogen(state: State, energy: float) -> State:
    """
    Terminal fragmentation into hydrogen.

    Hydrogen is treated as a low-constraint residue state.
    It forms when HELIUM_FRAGMENT cannot maintain stability.
    """
    if state == State.HELIUM_FRAGMENT and energy <= (MAX_UNIT_ENERGY["HYDROGEN"]):
        return State.HYDROGEN
    return state


def heavy_residue_form(state: State, energy: float) -> State:
    """
    Heavy residue formation from high-energy RADIANT/PLASMA intermediates.

    Heavy residue formation is permitted as an intermediate state:
    - it is not primordial
    - it is not a fuel
    - it is a constrained residue outcome of radiant processing
    """
    if state in (State.RADIANT, State.PLASMA) and energy >= (0.90 * MAX_UNIT_ENERGY["PLASMA"]):
        return State.HEAVY
    return state


# =========================
# Saturation Escalation
# =========================

def escalate_stage_chain(state: State, energy: float) -> State:
    """
    Enforce ordered stage-chain escalation when saturated.

    If a stage-chain state reaches its maximum admissible energy,
    it must transition to the next stage.
    """
    max_e = MAX_UNIT_ENERGY[state.name]

    if state in STAGE_NEXT and energy >= max_e:
        return STAGE_NEXT[state]

    return state


# =========================
# Master Transition Function
# =========================

def apply_transitions(state: State, energy: float) -> State:
    """
    Apply all legal transitions in a lawful order.

    Order matters:
    1) Heavy residue formation (mid-process)
    2) Stage-chain escalation
    3) Helium splitting
    4) Terminal fragmentation to hydrogen
    """
    # heavy residue can occur before stage-chain escalation completes
    state = heavy_residue_form(state, energy)

    # enforce ordered stage chain
    state = escalate_stage_chain(state, energy)

    # helium splits when saturated
    state = helium_split(state, energy)

    # fragments can decay into hydrogen residue
    state = fragment_to_hydrogen(state, energy)

    return state
