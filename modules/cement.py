import math


def calculate_annular_volume(
    hole_diameter,
    casing_od,
    interval_length,
    excess_percent
):
    """
    Calculate annular cement volume.

    Inputs
    ------
    hole_diameter : inches
    casing_od : inches
    interval_length : metres
    excess_percent : %

    Returns
    -------
    Volume (m³)
    """

    hole = hole_diameter * 0.0254
    casing = casing_od * 0.0254

    area = math.pi / 4 * (hole**2 - casing**2)

    excess = 1 + (excess_percent / 100)

    return area * interval_length * excess


def calculate_cement_sacks(volume, yield_per_sack):
    """
    Calculate required cement sacks.
    """

    return volume / yield_per_sack


def validate_inputs(
    hole_diameter,
    casing_od,
    interval_length,
    excess_percent,
    yield_per_sack
):

    if hole_diameter <= 0:
        return False, "Hole diameter must be greater than zero."

    if casing_od <= 0:
        return False, "Casing diameter must be greater than zero."

    if casing_od >= hole_diameter:
        return False, "Casing diameter must be smaller than the hole diameter."

    if interval_length <= 0:
        return False, "Interval length must be greater than zero."

    if excess_percent < 0:
        return False, "Excess cannot be negative."

    if yield_per_sack <= 0:
        return False, "Yield per sack must be greater than zero."

    return True, ""