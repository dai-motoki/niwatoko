def add(a, b):
    """
    2つの数値を足し算する関数

    Parameters:
    a (int or float): 1つ目の数値
    b (int or float): 2つ目の数値

    Returns:
    int or float: aとbの和
    """
    return a + b

def add_list(numbers):
    """
    数値のリストの合計を計算する関数

    Parameters:
    numbers (list): 数値のリスト

    Returns:
    int or float: numbersの合計値
    """
    total = 0
    for num in numbers:
        total = add(total, num)
    return total

def add_multiple(*args):
    """
    複数の数値を足し算する関数

    Parameters:
    *args: 可変長引数。任意の数の数値を受け取る

    Returns:
    int or float: 引数として渡された数値の合計
    """
    return add_list(args)
