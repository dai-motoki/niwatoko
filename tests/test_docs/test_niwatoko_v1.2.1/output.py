以下は、要件定義書に基づいて実装した足し算モジュールとテストコードです。

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
        raise TypeError("Arguments must be integers or floats")
    return a + b


def add_list(numbers):
    """
    数値のリストの合計を計算する関数

    Args:
        numbers (list): 数値のリスト

    Returns:
        int or float: numbersの合計値
    """
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("List elements must be integers or floats")
    return sum(numbers)


def add_multiple(*args):
    """
    複数の数値を足し算する関数

    Args:
        *args: 可変長引数。任意の数の数値を受け取る

    Returns:
        int or float: 引数として渡された数値の合計
    """
    if not all(isinstance(arg, (int, float)) for arg in args):
        raise TypeError("Arguments must be integers or floats")
    return sum(args)
```

テストコード:

```python
import unittest

class TestAddModule(unittest.TestCase):
    def test_add_normal(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(2.5, 3.7), 6.2)
        self.assertEqual(add(2, 3.7), 5.7)

    def test_add_abnormal(self):
        with self.assertRaises(TypeError):
            add("2", 3)

    def test_add_list_normal(self):
        self.assertEqual(add_list([1, 2, 3]), 6)
        self.assertEqual(add_list([2.5, 3.7, 4.8]), 11.0)
        self.assertEqual(add_list([1, 2.5, 3.7]), 7.2)

    def test_add_list_abnormal(self):
        with self.assertRaises(TypeError):
            add_list([1, 2, "3"])

    def test_add_multiple_normal(self):
        self.assertEqual(add_multiple(1, 2, 3), 6)
        self.assertEqual(add_multiple(2.5, 3.7, 4.8), 11.0)
        self.assertEqual(add_multiple(1, 2.5, 3.7), 7.2)

    def test_add_multiple_abnormal(self):
        with self.assertRaises(TypeError):
            add_multiple(1, 2, "3")

if __name__ == '__main__':
    unittest.main()
```