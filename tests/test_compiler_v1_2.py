# Usage: niwatoko [OPTIONS] [FILE_PATH]

#   自然言語のソースコードを読み込んで実行するコマンドラインインターフェース。

#   Args:     file_path (str): 自然言語のソースコードが書かれたファイルのパス。     model (str):
#   使用するモデル（OpenAIまたはClaude）。     output (str): 生成されたコードの出力先ファイルのパス。     version
#   (bool): バージョン情報を表示するかどうか。

# Options:
#   -m, --model [openai|claude]  使用するモデルを選択します。
#   -o, --output PATH            生成されたコードの出力先ファイルを指定します。
#   -v, --version                バージョン情報を表示します。
#   --help                       Show this message and exit.



import subprocess
import os
from click.testing import CliRunner
from niwatoko.cli import main

class TestBase:
    """
    テストの共通処理を行うベースクラス
    """
    def setup_method(self):
        self.runner = CliRunner()

class TestVersion(TestBase):
    """
    バージョン情報が正しく表示されることを確認するテストケース
    """
    def test_version(self):
        result = self.runner.invoke(main, ['--version'])
        assert result.exit_code == 0
        assert 'niwatoko version:' in result.output

class TestNoFilePath(TestBase):
    """
    ファイルパスが指定されていない場合のエラーメッセージを確認するテストケース
    """
    def test_no_file_path(self):
        result = self.runner.invoke(main, [])
        assert result.exit_code == 0
        assert 'ファイルパスが指定されていません。' in result.output

class TestInvalidModel(TestBase):
    """
    無効なモデルが指定された場合のエラーを確認するテストケース
    """
    def test_invalid_model(self):
        result = self.runner.invoke(main, ['sample.md', '--model', 'invalid'])
        assert result.exit_code == 2
        assert 'Error: Invalid value for' in result.output

class TestGenerateResponse(TestBase):
    """
    自然言語コードから生成されたコードを確認するテストケースの基底クラス
    """
    def setup_method(self):
        super().setup_method()
        self.sample_file = None
        self.output_file = None

    def generate_response(self, model):
        result = self.runner.invoke(main, [str(self.sample_file), '--model', model, '--output', str(self.output_file)], input='n\n')
        assert '生成されたコードを' in result.output
        assert f'{str(self.output_file)} に書き出しました。実行しますか？(y/n)' in result.output
        assert result.exit_code == 0
        assert os.path.exists(self.output_file)
        assert 'に書き出しました。' in result.output

class TestGenerateResponseClaude(TestGenerateResponse):
    """
    Claudeモデルを使用して自然言語コードから生成されたコードを確認するテストケース
    """
    def test_generate_response_claude(self, tmp_path):
        self.sample_file = tmp_path / 'sample.md'
        self.sample_file.write_text('自然言語のコードサンプル')
        self.output_file = tmp_path / 'output.py'
        self.generate_response('claude')

class TestGenerateResponseOpenAI(TestGenerateResponse):
    """
    OpenAIモデルを使用して自然言語コードから生成されたコードを確認するテストケース
    """
    def test_generate_response_openai(self, tmp_path):
        self.sample_file = tmp_path / 'sample.md'
        self.sample_file.write_text('自然言語のコードサンプル')
        self.output_file = tmp_path / 'output.py'
        self.generate_response('openai')

# 上記をもとにリードミーを作成してください。特にオブジェクト思考のASCII図を描いてください。