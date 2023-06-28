#!/usr/bin/python3
def safe_print_integer(value):
    """Print an integer with "{:d}".format().

    Args:
        value (int): The integer to print.

    Returns:
        True if printing is successful, False otherwise.
    """
    if isinstance(value, int):
        print("{:d}".format(value))
        return True
    return False
