import math

from modules.constants import (
    GRAVITY,
    INCH_TO_M,
    LPM_TO_M3_PER_MIN,
    LEAD_SLURRY_PERCENT,
    TAIL_SLURRY_PERCENT,
    TEMPERATURE_MARGIN_C,
)


def calculate_annular_volume(hole_diameter, casing_od, interval_length, excess_percent):
    # calculate annular volume in m3
    # hole and casing diameters are in inches, interval in metres

    hole = hole_diameter * INCH_TO_M
    casing = casing_od * INCH_TO_M

    area = math.pi / 4 * (hole**2 - casing**2)

    excess = 1 + (excess_percent / 100)

    return area * interval_length * excess


def calculate_cement_volume(slurry_volume, lead_percent=LEAD_SLURRY_PERCENT, tail_percent=TAIL_SLURRY_PERCENT):
    # split slurry volume into lead and tail sections
    lead_volume = slurry_volume * lead_percent / 100
    tail_volume = slurry_volume * tail_percent / 100
    return lead_volume, tail_volume


def calculate_spacer_volume(hole_diameter, casing_od, spacer_length):
    # spacer volume in annulus
    hole = hole_diameter * INCH_TO_M
    casing = casing_od * INCH_TO_M
    area = math.pi / 4 * (hole**2 - casing**2)
    return area * spacer_length


def calculate_flush_volume(hole_diameter, flush_length):
    # flush fluid volume inside the wellbore
    hole = hole_diameter * INCH_TO_M
    area = math.pi / 4 * hole**2
    return area * flush_length


def calculate_pump_time(slurry_volume, pump_rate_lpm):
    # pump time in minutes
    # slurry_volume in m3, pump_rate in l/min
    if pump_rate_lpm <= 0:
        return 0.0  # no pumping -> no pump time (avoid division by zero)
    pump_rate_m3 = pump_rate_lpm * LPM_TO_M3_PER_MIN
    return slurry_volume / pump_rate_m3


def calculate_plug_bumping_pressure(plug_length, mud_weight):
    # plug bumping pressure - hydrostatic pressure of the cement column
    pressure = mud_weight * GRAVITY * plug_length
    return pressure


def evaluate_temperature_rating(max_temperature_c, bottom_hole_temp):
    """Compare bottom-hole temperature against the cement class rating.

    Returns (rating, margin_c) where rating is:
      - "OK"      : bottom-hole temperature is within class rating
      - "LIMIT"   : within 15 °C of the rating (caution band)
      - "EXCEEDED": bottom-hole temperature exceeds the class rating
    """
    margin_c = max_temperature_c - bottom_hole_temp
    if bottom_hole_temp > max_temperature_c:
        return "EXCEEDED", margin_c
    if margin_c <= TEMPERATURE_MARGIN_C:
        return "LIMIT", margin_c
    return "OK", margin_c


def validate_inputs(hole_diameter, casing_od, interval_length, excess_percent, yield_per_sack):

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