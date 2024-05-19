以下は、要件定義書に基づいて作成したpythonプログラムとpytestテストコードです。

```python
def add(a, b):
    """
    2つの数値を足し算する関数
    
    Args:
        a (int or float): 1つ目の数値
        b (int or float): 2つ目の数値
    
    Returns:
        int or float: aとbの和
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("引数は数値でなければなりません")
    return a + b

def add_list(numbers):
    """
    数値のリストの合計を計算する関数
    
    Args:
        numbers (list): 数値のリスト
    
    Returns:
        int or float: numbersの合計値
    """
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("リストの要素は数値でなければなりません")
    return sum(numbers)

def add_multiple(*args):
    """
    複数の数値を足し算する関数
    
    Args:
        *args: 可変長引数。任意の数の数値を受け取る
    
    Returns:
        int or float: 引数として渡された数値の合計
    """
    if not all(isinstance(x, (int, float)) for x in args):
        raise TypeError("引数は数値でなければなりません")
    return sum(args)

def multiply(a, b):
    """
    2つの数値を掛け算する関数
    
    Args:
        a (int or float): 1つ目の数値
        b (int or float): 2つ目の数値
    
    Returns:
        int or float: aとbの積
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("引数は数値でなければなりません")
    return a * b

def multiply_list(numbers):
    """
    数値のリストの積を計算する関数
    
    Args:
        numbers (list): 数値のリスト
    
    Returns:
        int or float: numbersの積
    """
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("リストの要素は数値でなければなりません")
    return prod(numbers)

def multiply_multiple(*args):
    """
    複数の数値を掛け算する関数
    
    Args:
        *args: 可変長引数。任意の数の数値を受け取る
    
    Returns:
        int or float: 引数として渡された数値の積
    """
    if not all(isinstance(x, (int, float)) for x in args):
        raise TypeError("引数は数値でなければなりません")
    return prod(args)

def prod(iterable):
    """
    iterable内の要素の積を計算する関数
    """
    result = 1
    for x in iterable:
        result *= x
    return result
```

```python
import pytest

def test_add():
    # 正常系
    assert add(2, 3) == 5
    assert add(2.5, 3.7) == 6.2
    assert add(2, 3.7) == 5.7
    
    # 異常系
    with pytest.raises(TypeError):
        add("2", 3)

def test_add_list():
    # 正常系
    assert add_list([1, 2, 3]) == 6
    assert add_list([2.5, 3.7, 4.8]) == 11.0
    assert add_list([1, 2.5, 3.7]) == 7.2
    
    # 異常系
    with pytest.raises(TypeError):
        add_list([1, 2, "3"])

def test_add_multiple():
    # 正常系
    assert add_multiple(1, 2, 3) == 6
    assert add_multiple(2.5, 3.7, 4.8) == 11.0
    assert add_multiple(1, 2.5, 3.7) == 7.2
    
    # 異常系
    with pytest.raises(TypeError):
        add_multiple(1, 2, "3")

def test_multiply():
    # 正常系
    assert multiply(2, 3) == 6
    assert multiply(2.5, 3.7) == 9.25
    assert multiply(2, 3.7) == 7.4
    
    # 異常系
    with pytest.raises(TypeError):
        multiply("2", 3)

def test_multiply_list():
    # 正常系
    assert multiply_list([1, 2, 3]) == 6
    assert multiply_list([2.5, 3.7, 4.8]) == 44.28
    assert multiply_list([1, 2.5, 3.7]) == 9.25
    
    # 異常系
    with pytest.raises(TypeError):
        multiply_list([1, 2, "3"])

def test_multiply_multiple():
    # 正常系
    assert multiply_multiple(1, 2, 3) == 6
    assert multiply_multiple(2.5, 3.7, 4.8) == 44.28
    assert multiply_multiple(1, 2.5, 3.7) == 9.25
    
    # 異常系
    with pytest.raises(TypeError):
        multiply_multiple(1, 2, "3")
```