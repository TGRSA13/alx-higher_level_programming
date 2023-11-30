#!/usr/bin/python3

def add(a, b):
    """My addition function
    Args:
        a: first integer
        b: second integer
    Returns:
        The return value. a + b
    """
    return a + b

def sub(a, b):
    """My subtraction function
    Args:
        a: first integer
        b: second integer
    Returns:
        The return value. a - b
    """
    return a - b

def mul(a, b):
    """My multiplication function
    Args:
        a: first integer
        b: second integer
    Returns:
        The return value. a * b
    """
    return a * b

def div(a, b):
    """My division function
    Args:
        a: numerator
        b: denominator
    Returns:
        The return value. a / b
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

if __name__ == "__main__":
    # You can test your functions here if needed
    pass
