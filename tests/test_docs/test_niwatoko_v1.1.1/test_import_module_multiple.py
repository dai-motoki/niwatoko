def multiply(a, b):
    """
    2つの数値を掛け算する関数

    Parameters:
    a (int or float): 1つ目の数値
    b (int or float): 2つ目の数値

    Returns:
    int or float: aとbの積
    """
    return a * b

def multiply_list(numbers):
    """
    数値のリストの積を計算する関数

    Parameters:
    numbers (list): 数値のリスト

    Returns:
    int or float: numbersの積
    """
    total = 1
    for num in numbers:
        total = multiply(total, num)
    return total

def multiply_multiple(*args):
    """
    複数の数値を掛け算する関数

    Parameters:
    *args: 可変長引数。任意の数の数値を受け取る

    Returns:
    int or float: 引数として渡された数値の積
    """
    return multiply_list(args)
