from modules.constants import GRAVITY


def calculate_mud_density(pore_pressure, tvd):
    # mud density to balance formation pressure
    return pore_pressure / (GRAVITY * tvd)


def calculate_hydrostatic_pressure(mud_density, tvd):
    # hydrostatic pressure from mud column
    return mud_density * GRAVITY * tvd


def safe_window(pore_pressure, fracture_pressure, tvd):
    # calculate min and max safe mud density
    minimum_density = pore_pressure / (GRAVITY * tvd)
    maximum_density = fracture_pressure / (GRAVITY * tvd)
    return minimum_density, maximum_density


def check_safe_density(density, minimum_density, maximum_density):
    # check if mud density is within safe window
    if density < minimum_density:
        return "TOO LOW"
    if density > maximum_density:
        return "TOO HIGH"
    return "SAFE"


def validate_inputs(pore_pressure, fracture_pressure, tvd):

    if pore_pressure <= 0:
        return False, "Pore pressure must be greater than zero."

    if fracture_pressure <= 0:
        return False, "Fracture pressure must be greater than zero."

    if fracture_pressure <= pore_pressure:
        return False, "Fracture pressure must be greater than pore pressure."

    if tvd <= 0:
        return False, "True Vertical Depth must be greater than zero."

    return True, ""
