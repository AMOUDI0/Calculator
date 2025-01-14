import math

def sqrt(number):
    """
    Calculate the square root of a number.

    Args:
        number (float): The input number.
    Returns:
        float: The square root of the input number.
    """
    if number < 0:
        return "Error: Cannot calculate the square root of a negative number."
    return math.sqrt(number)
