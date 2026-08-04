import math

from modules.constants import GRAVITY, INCH_TO_M


def calculate_plug_volume(hole_diameter, plug_length):
    # cement plug volume in m3
    hole = hole_diameter * INCH_TO_M
    area = math.pi / 4 * hole**2
    return area * plug_length


def calculate_squeeze_volume(hole_diameter, interval_length, squeeze_efficiency=0.8):
    # squeeze cement volume
    hole = hole_diameter * INCH_TO_M
    area = math.pi / 4 * hole**2
    volume = area * interval_length * squeeze_efficiency
    return volume


def calculate_balanced_plug(top, bottom, mud_weight, cement_density):
    # calculate balanced plug parameters
    length = bottom - top
    # pressure at plug bottom
    pressure = cement_density * GRAVITY * length
    return length, pressure


def calculate_abandonment_sacks(volume, yield_per_sack):
    # number of sacks needed
    return volume / yield_per_sack


def validate_inputs(hole_diameter, plug_length, yield_per_sack):
    if hole_diameter <= 0:
        return False, "Hole diameter must be greater than zero."
    if plug_length <= 0:
        return False, "Plug length must be greater than zero."
    if yield_per_sack <= 0:
        return False, "Yield must be greater than zero."
    return True, ""
