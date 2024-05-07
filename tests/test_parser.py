# はい、ここでは `parser.py` モジュールのテストを書く方法について説明します。
# 
# `tests/test_parser.py` ファイルを作成し、以下のようなテストコードを書きます:
# 
import unittest
from niwatoko.parser import parse

class TestParser(unittest.TestCase):
    def test_simple_program(self):
        program = """
        Create a function that takes two numbers as input and returns their sum.
        """
        ast = parse(program)
        self.assertIsNotNone(ast)
        self.assertEqual(len(ast.body), 1)
        self.assertEqual(ast.body[0].name, "create_function")
        self.assertEqual(len(ast.body[0].arguments), 2)
        self.assertEqual(ast.body[0].return_type, "sum")

    def test_invalid_program(self):
        program = """
        This is not a valid program.
        """
        with self.assertRaises(ValueError):
            parse(program)

    def test_program_with_multiple_statements(self):
        program = """
        Create a function that takes two numbers as input and returns their sum.
        Create a function that takes two strings as input and returns their concatenation.
        """
        ast = parse(program)
        self.assertIsNotNone(ast)
        self.assertEqual(len(ast.body), 2)
        self.assertEqual(ast.body[0].name, "create_function")
        self.assertEqual(ast.body[1].name, "create_function")

if __name__ == '__main__':
    unittest.main()
# 
# このテストケースでは、以下のことをチェックしています:
# 
# 1. 簡単な自然言語プログラムを正しくパースできること
# 2. 無効な自然言語プログラムを渡した場合に、適切な例外が発生すること
# 3. 複数の文からなる自然言語プログラムを正しくパースできること
# 
# テストを実行するには、以下のコマンドを使用します:
# 
# python -m unittest tests.test_parser
# 
# これにより、`tests/test_parser.py` ファイルのテストが実行されます。
# 
# テストの実装に際しては、以下のようなポイントに注意しましょう:
# 
# - 各テストケースでは、1つの機能や動作を検証するようにする
# - 期待する結果と実際の結果を明確に比較する
# - 例外処理のテストも忘れずに行う
# - テストの命名規則は `test_` で始まるようにする
# - テストの実行は自動化し、継続的に行う
# 
# これらの方法でparserモジュールのテストを書いていきます。テストの作成と並行して、実際の実装も進めていきましょう。