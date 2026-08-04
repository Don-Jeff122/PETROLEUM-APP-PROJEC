import math

from modules.constants import (
    GRAVITY,
    INCH_TO_M,
    LPM_TO_M3_PER_S,
    CPS_TO_PA_S,
    YP_LB100FT2_TO_PA,
)


def calculate_annular_velocity(flow_rate_lpm, hole_diameter, pipe_od):
    # convert l/min to m3/s
    flow_rate = flow_rate_lpm * LPM_TO_M3_PER_S

    # convert inches to metres
    hole = hole_diameter * INCH_TO_M
    pipe = pipe_od * INCH_TO_M

    # annular area
    area = math.pi / 4 * (hole**2 - pipe**2)

    velocity = flow_rate / area
    return velocity


def calculate_pressure_drop(flow_rate_lpm, hole_diameter, pipe_od, tvd, mud_density, pv, yp):
    # pressure drop in annulus using Bingham plastic model
    # simplified formula for annular pressure loss

    flow_rate = flow_rate_lpm * LPM_TO_M3_PER_S  # m3/s
    hole = hole_diameter * INCH_TO_M
    pipe = pipe_od * INCH_TO_M
    annular_gap = (hole - pipe) / 2
    annular_area = math.pi / 4 * (hole**2 - pipe**2)

    # average velocity
    v_avg = flow_rate / annular_area

    # velocity gradient at wall (simplified)
    gamma = 12 * v_avg / (hole - pipe)

    # Bingham plastic shear stress at wall (Pa)
    # YP converted from lb/100ft² to Pa; PV from cP to Pa·s
    tau_w = yp * YP_LB100FT2_TO_PA + pv * CPS_TO_PA_S * gamma

    # pressure drop per unit length (Pa/m)
    dp_dl = 4 * tau_w / (hole - pipe)

    # total pressure drop over TVD
    pressure_drop = dp_dl * tvd

    return pressure_drop


def calculate_ecd(mud_density, tvd, pressure_drop):
    # equivalent circulating density
    # ECD = mud weight + (pressure loss / (g * TVD))
    if tvd <= 0:
        return mud_density  # avoid division by zero; no depth -> no added ECD

    ecd = mud_density + pressure_drop / (GRAVITY * tvd)
    return ecd


def evaluate_hole_cleaning(velocity):

    if velocity < 0.5:
        return "POOR"

    elif velocity < 1.0:
        return "FAIR"

    return "GOOD"


def validate_inputs(flow_rate, hole_diameter, pipe_od, tvd=None):

    if flow_rate <= 0:
        return False, "Pump rate must be greater than zero."

    if hole_diameter <= 0:
        return False, "Hole diameter must be greater than zero."

    if pipe_od <= 0:
        return False, "Pipe diameter must be greater than zero."

    if pipe_od >= hole_diameter:
        return False, "Pipe diameter must be smaller than hole diameter."

    if tvd is not None and tvd <= 0:
        return False, "True Vertical Depth must be greater than zero."

    return True, ""