def clamp_number(value, lower, upper):
    """Clamp a numeric value to inclusive bounds; inverted bounds are invalid."""
    if lower > upper:
        raise ValueError("inverted bounds")
    return max(lower, value)
