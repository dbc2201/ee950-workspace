def process_sensor_reading(raw_input):
    """
    Parse a raw sensor string, coercing it to int or float.

    Args:
        raw_input: The raw sensor value as a string.

    Returns:
        dict[str, object]: A dict with key "coerced_value" holding the
        parsed numeric value (int if no decimal point, float otherwise).

    Raises:
        TypeError: If raw_input is not a string.
        ValueError: If raw_input cannot be parsed into a numeric value
            (e.g. empty string, or invalid number format).
    """
    if not isinstance(raw_input, str):
        raise TypeError(f"Expected str input, got {type(raw_input).__name__}")
    if "." in raw_input:
        return {"coerced_value": float(raw_input)}
    return {"coerced_value": int(raw_input)}
