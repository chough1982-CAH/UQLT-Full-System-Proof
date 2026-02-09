"""
parameters.py

Runtime parameters for the UQLT Full-System Proof Engine.

These parameters control execution scale, determinism, and output handling.
They DO NOT modify physical laws, constants, or mechanisms.

Changing values here must not alter qualitative outcomes.
If outcomes change qualitatively, the engine is invalid.
"""

import os
from datetime import datetime

# =========================
# Determinism
# =========================

# Fixed random seed for reproducibility
RANDOM_SEED = 42

# =========================
# Grid / Lattice Parameters
# =========================

# Square grid dimensions (NxN)
GRID_SIZE = 61  # must be odd to define a center cell

# =========================
# Simulation Timing
# =========================

# Maximum number of steps for each simulation phase
STEPS_STAGE_CHAIN = 300
STEPS_COLLAPSE = 600
STEPS_EMN_ANALYSIS = 400
STEPS_VALIGNITY_ANALYSIS = 400

# =========================
# Neighborhood Definition
# =========================

# Neighborhood radius for local interactions
NEIGHBOR_RADIUS = 1  # Moore neighborhood

# =========================
# Output Paths
# =========================

BASE_OUTPUT_DIR = "outputs"

DATA_OUTPUT_DIR = os.path.join(BASE_OUTPUT_DIR, "data")
PLOT_OUTPUT_DIR = os.path.join(BASE_OUTPUT_DIR, "plots")

# Ensure output directories exist
os.makedirs(DATA_OUTPUT_DIR, exist_ok=True)
os.makedirs(PLOT_OUTPUT_DIR, exist_ok=True)

# =========================
# Run Metadata
# =========================

# Timestamp runs for traceability
RUN_TIMESTAMP = datetime.utcnow().strftime("%Y%m%d_%H%M%S")

# Attach metadata to all outputs
INCLUDE_METADATA = True

# =========================
# Validation Controls
# =========================

# Minimum steps before allowing collapse validation
MIN_STEPS_BEFORE_COLLAPSE_CHECK = 50

# Minimum steps before allowing stability checks
MIN_STEPS_BEFORE_STABILITY_CHECK = 100

# =========================
# Safety Limits
# =========================

# Abort if simulation exceeds this many total state transitions
MAX_STATE_TRANSITIONS = 10_000_000
