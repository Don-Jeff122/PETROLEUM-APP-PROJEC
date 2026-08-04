import math

from modules.constants import INCH_TO_M


def calculate_plug_volume(hole_diameter, plug_length):
    # plug volume in m3, hole_diameter in inches, plug_length in metres
    hole = hole_diameter * INCH_TO_M  # convert to metres

    area = math.pi / 4 * (hole ** 2)

    volume = area * plug_length

    return volume


def validate_inputs(hole_diameter, plug_length, yield_per_sack):

    if hole_diameter <= 0:
        return False, "Hole diameter must be greater than zero."

    if plug_length <= 0:
        return False, "Plug length must be greater than zero."

    if yield_per_sack <= 0:
        return False, "Yield must be greater than zero."

    return True, ""