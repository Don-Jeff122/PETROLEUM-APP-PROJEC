import math


def calculate_plug_volume(hole_diameter, plug_length):
    """
    Calculate the volume of a cement plug.

    Inputs:
        hole_diameter : inches
        plug_length   : metres

    Returns:
        Volume (m³)
    """

    hole = hole_diameter * 0.0254

    area = math.pi / 4 * (hole ** 2)

    volume = area * plug_length

    return volume


def calculate_cement_sacks(volume, yield_per_sack):
    """
    Calculate required cement sacks.
    """

    return volume / yield_per_sack


def validate_inputs(hole_diameter, plug_length, yield_per_sack):

    if hole_diameter <= 0:
        return False, "Hole diameter must be greater than zero."

    if plug_length <= 0:
        return False, "Plug length must be greater than zero."

    if yield_per_sack <= 0:
        return False, "Yield must be greater than zero."

    return True, ""