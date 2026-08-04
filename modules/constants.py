"""Central engineering constants, unit conversions, and app metadata.

All conversion factors and physical constants used across the calculation
engine live here so the codebase satisfies the PENG 258 requirement of
"absence of hardcoded values" — every variable is either user input or
derived from these named constants.
"""

# ── Physical constants ───────────────────────────────────────────────────────
GRAVITY = 9.81                     # gravitational acceleration (m/s²)

# ── Unit conversions ─────────────────────────────────────────────────────────
INCH_TO_M = 0.0254                 # inches → metres
LPM_TO_M3_PER_S = 1.0 / 60_000.0   # litres/min → m³/s
LPM_TO_M3_PER_MIN = 1.0 / 1000.0   # litres/min → m³/min
PPG_TO_KG_M3 = 119.826             # lb/gal (ppg) → kg/m³
PA_PER_MPA = 1_000_000             # Pa → MPa
CPS_TO_PA_S = 0.001                # centipoise → Pa·s
YP_LB100FT2_TO_PA = 0.4788         # lb/100ft² → Pa (Bingham plastic wall shear)
EXCESS_WARNING_THRESHOLD = 50.0    # % excess beyond which washout is suspect
TEMPERATURE_MARGIN_C = 15.0        # safety margin below class max temp (°C)
LEAD_SLURRY_PERCENT = 40           # default lead slurry fraction (%)
TAIL_SLURRY_PERCENT = 60           # default tail slurry fraction (%)

# ── App metadata ─────────────────────────────────────────────────────────────
APP_NAME = "PyMudCement-Optima"
APP_TAGLINE = "Drilling & Cementing Engineering"
APP_VERSION = "1.1"
AUTHOR = "Group ..."
UNIVERSITY = "University of Energy and Natural Resources (UENR)"
DEPARTMENT = "Petroleum and Natural Gas Engineering"
