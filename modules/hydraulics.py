import math


def calculate_annular_velocity(flow_rate_lpm, hole_diameter, pipe_od):
    """
    Calculate annular velocity.

    Parameters:
        flow_rate_lpm : Pump rate (L/min)
        hole_diameter : Hole diameter (inches)
        pipe_od       : Drill pipe OD (inches)

    Returns:
        Annular velocity (m/s)
    """

    # Convert litres/min to m³/s
    flow_rate = flow_rate_lpm / 1000 / 60

    # Convert inches to metres
    hole = hole_diameter * 0.0254
    pipe = pipe_od * 0.0254

    area = math.pi / 4 * (hole**2 - pipe**2)

    velocity = flow_rate / area

    return velocity


def evaluate_hole_cleaning(velocity):

    if velocity < 0.5:
        return "POOR"

    elif velocity < 1.0:
        return "FAIR"

    return "GOOD"


def validate_inputs(flow_rate, hole_diameter, pipe_od):

    if flow_rate <= 0:
        return False, "Pump rate must be greater than zero."

    if hole_diameter <= 0:
        return False, "Hole diameter must be greater than zero."

    if pipe_od <= 0:
        return False, "Pipe diameter must be greater than zero."

    if pipe_od >= hole_diameter:
        return False, "Pipe diameter must be smaller than hole diameter."

    return True, ""