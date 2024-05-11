def multiply(a, b):
    """
    Function to multiply two numbers

    Parameters:
    a (int or float): First number
    b (int or float): Second number

    Returns:
    int or float: Product of a and b
    """
    return a * b

def multiply_list(numbers):
    """
    Function to calculate the product of a list of numbers

    Parameters:
    numbers (list): List of numbers

    Returns:
    int or float: Product of numbers
    """
    total = 1
    for num in numbers:
        total = multiply(total, num)
    return total


def multiply_multiple(*args):
    """
    Function to multiply multiple numbers

    Parameters:
    *args: Variable-length arguments. Accepts any number of numeric values

    Returns:
    int or float: Product of the passed arguments
    """
    return multiply_list(args)