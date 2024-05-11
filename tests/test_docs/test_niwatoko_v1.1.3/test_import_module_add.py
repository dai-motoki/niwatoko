def add(a, b):
    """
    Function to add two numbers

    Parameters:
    a (int or float): First number
    b (int or float): Second number

    Returns:
    int or float: Sum of a and b
    """
    return a + b

def add_list(numbers):
    """
    Function to calculate the sum of a list of numbers

    Parameters:
    numbers (list): List of numbers

    Returns:
    int or float: Sum of numbers
    """
    total = 0
    for num in numbers:
        total = add(total, num)
    return total

def add_multiple(*args):
    """
    Function to add multiple numbers

    Parameters:
    *args: Variable-length arguments. Accepts any number of numeric values

    Returns:
    int or float: Sum of the passed arguments
    """
    return add_list(args)
