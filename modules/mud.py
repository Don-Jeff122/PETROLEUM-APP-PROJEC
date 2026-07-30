GRAVITY = 9.81


def calculate_mud_density(pore_pressure, tvd):
    """
    Calculate the mud density required to balance formation pressure.

    Parameters:
        pore_pressure (Pa)
        tvd (m)

    Returns:
        Mud density (kg/m³)
    """

    return pore_pressure / (GRAVITY * tvd)


def calculate_hydrostatic_pressure(mud_density, tvd):
    """
    Calculate hydrostatic pressure.

    Parameters:
        mud_density (kg/m³)
        tvd (m)

    Returns:
        Pressure (Pa)
    """

    return mud_density * GRAVITY * tvd


def safe_window(pore_pressure, fracture_pressure, tvd):
    """
    Calculate the minimum and maximum safe mud density.
    """

    minimum_density = pore_pressure / (GRAVITY * tvd)
    maximum_density = fracture_pressure / (GRAVITY * tvd)

    return minimum_density, maximum_density


def check_safe_density(density, minimum_density, maximum_density):
    """
    Check whether the mud density is safe.
    """

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


def pa_to_mpa(value):
    return value / 1_000_000