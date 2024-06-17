インストール方法
============================================

niwatoko 言語は、以下の方法でインストールできます。

ローカルにインストールする
--------------------------

Macの場合
~~~~~~~~~

1. Homebrewを使用して、最新バージョンのPythonをインストールします。以下の手順に従ってください。

   a. ターミナルを開き、以下のコマンドを実行してHomebrewがインストールされているか確認します。

      .. code-block:: shell

         brew --version

      Homebrewがインストールされていない場合は、以下のコマンドを実行してインストールします。

      .. code-block:: shell

         /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

   b. 以下のコマンドを実行して、Homebrewを使用してPython 3.11をインストールします。

      .. code-block:: shell

         brew install python@3.11

   c. 以下のコマンドを実行して、PythonのPATHを設定します。

      .. code-block:: shell

         echo 'export PATH="/usr/local/opt/python@3.11/bin:$PATH"' >> ~/.zshrc

   d. 新しいターミナルウィンドウを開くか、以下のコマンドを実行して設定を反映します。

      .. code-block:: shell

         source ~/.zshrc

2. ターミナルで以下のコマンドを実行して、Pythonのバージョンを確認します。

   .. code-block:: shell

      python --version

   Python 3.11がインストールされていることを確認してください。

3. pipは通常、Pythonのインストールに含まれています。以下のコマンドを実行して、pipのバージョンを確認します。

   .. code-block:: shell
   
      pip --version

4. 以下のコマンドを実行して、niwatoko言語をインストールします。

   .. code-block:: shell

      pip install niwatoko

   これにより、最新バージョンのniwatoko言語がインストールされます。

.. note::
   
   - Homebrewを使用することで、最新バージョンのPythonを簡単にインストールできます。
   - pythonコマンドとpipコマンドを使用して、インストールしたPython 3.11を明示的に指定します。
   - Python 3.11は、niwatoko言語との互換性が確認されているバージョンです。

Windowsの場合
~~~~~~~~~~~~~

1. Pythonの公式サイト（ https://www.python.org/downloads/ ）から、Python 3.6以上のインストーラをダウンロードします。

2. ダウンロードしたインストーラを実行し、Pythonをインストールします。インストール時に「Add Python to PATH」オプションを選択することを推奨します。

3. コマンドプロンプトを管理者権限で開きます。

4. 以下のコマンドを実行して、Pythonのバージョンを確認します。

   .. code-block:: shell

      python --version

   Python 3.6以上がインストールされていることを確認してください。

5. 以下のコマンドを実行して、pipのバージョンを確認します。

   .. code-block:: shell

      pip --version

   pipがインストールされていない場合は、以下のコマンドを実行してインストールします。

   .. code-block:: shell

      curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
      python get-pip.py

6. 以下のコマンドを実行して、niwatoko言語をインストールします。

   .. code-block:: shell

      pip install niwatoko

仮想環境にインストールする
--------------------------

1. 仮想環境を作成します。

   .. code-block:: shell

      python -m venv myenv

2. 仮想環境をアクティベートします。

   Macの場合:

   .. code-block:: shell

      source myenv/bin/activate

   Windowsの場合:

   .. code-block:: shell

      myenv\Scripts\activate

3. 仮想環境内で、niwatoko言語をインストールします。

   .. code-block:: shell

      pip install niwatoko

Dockerを使用する
----------------

1. Dockerがインストールされていることを確認します。

2. 以下のDockerfileを作成します。

   .. code-block:: dockerfile

      FROM python:3.10
      
      RUN pip install niwatoko
      
      WORKDIR /app

3. Dockerイメージをビルドします。

   .. code-block:: shell

      docker build -t niwatoko .

4. Dockerコンテナを起動します。

   .. code-block:: shell

      docker run -it --rm -v $(pwd):/app niwatoko

これで、niwatoko言語を使用する準備が整いました。
インストール方法に応じて、適切な環境でniwatoko言語を実行できます。
