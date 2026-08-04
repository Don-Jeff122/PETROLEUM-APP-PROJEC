def calculate_pv(reading_600, reading_300):
    # PV = R600 - R300 (Bingham plastic model)
    return reading_600 - reading_300


def calculate_yp(reading_300, pv):
    # YP = R300 - PV
    return reading_300 - pv


def validate_inputs(reading_600, reading_300):

    if reading_600 <= 0:
        return False, "600 RPM reading must be greater than zero."

    if reading_300 <= 0:
        return False, "300 RPM reading must be greater than zero."

    if reading_600 < reading_300:
        return False, "600 RPM reading cannot be less than the 300 RPM reading."

    return True, ""