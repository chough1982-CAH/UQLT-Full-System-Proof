"""
constants.py

Canonical constants and hard limits for the UQLT Full-System Proof Engine.

These values are not tuning parameters.
They represent fixed constraints derived from UQLT laws.

If a simulation only succeeds when these values are altered,
the simulation is invalid.
"""

# =========================
# Fundamental UQLT Constants
# =========================

# Chronocollapse constant
# Governs time emergence via collapse-induced delay
TAU_CHRONOCOLLAPSE = 1.0

# Valignity constant
# Governs radial density ordering strength
V_VALIGNITY = 1.0

# Layering constant
# Controls separation strength between stabilized shells
MU_LAYERING = 1.0

# Helium dominance threshold
# Fraction of helium-family states required to force collapse
H_HELIUM_DOMINANCE = 0.62

# Field-spin equilibrium constant
# Balances rotational coherence vs emission loss
SIGMA_FIELD_SPIN = 1.0

# Helium loop diffusion constant
# Governs outward decay and recycling of helium byproducts
DELTA_HELIUM_LOOP = 0.15

# c^2 — maximum energy-motion per unit constraint
# This is NOT a speed; it is the upper bound on admissible energy motion
C_SQUARED_MAX_MOTION = 1.0


# =========================
# Unit Capacity Limits
# =========================

# Maximum admissible energy per unit by state
MAX_UNIT_ENERGY = {
    "VOID": 0.0,
    "STATIC": 0.05,
    "RADIO": 0.15,
    "RADIANT": 0.40,
    "PLASMA": 0.75,
    "HELIUM": 1.00,
    "HELIUM_FRAGMENT": 0.60,
    "HYDROGEN": 0.25,
    "HEAVY": 0.90,
    "CORE": 3.00,
}

# =========================
# Intake / Emission Rates
# =========================

# Energy intake per step by state
ENERGY_INTAKE = {
    "STATIC": 0.002,
    "RADIO": 0.004,
    "RADIANT": 0.008,
    "PLASMA": 0.010,
    "HELIUM": 0.006,
    "HELIUM_FRAGMENT": 0.004,
    "HYDROGEN": 0.002,
    "HEAVY": 0.003,
    "CORE": 0.000,  # cores do not intake; they emit
}

# EMN emission rate from cores
CORE_EMISSION_RATE = 0.05


# =========================
# Collapse and Stability
# =========================

# Minimum local helium fraction to trigger collapse
COLLAPSE_HELIUM_THRESHOLD = H_HELIUM_DOMINANCE

# Minimum energy required to stabilize a shell
MIN_STABLE_SHELL_ENERGY = 0.45

# Energy below which structures fragment
FRAGMENTATION_THRESHOLD = 0.30


# =========================
# Enforcement Flags
# =========================

# Hard enforcement switches
HALT_ON_OVERFLOW = True
HALT_ON_ILLEGAL_STATE = True
HALT_ON_ILLEGAL_TRANSITION = True
