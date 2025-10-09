def safe_divide(numerator, denominator):
    """
    Try to convert inputs to float and divide.
    Returns a string with the result or an appropriate error message.
    """
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        result = num / den
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    return f"The result of the division is {result}"
