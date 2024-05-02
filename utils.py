def validate_numeric(input_str: str) -> float:
    """Validate that the input string is a numeric value."""
    try:
        return float(input_str)
    except ValueError:
        raise ValueError("Input must be a numeric value.")
