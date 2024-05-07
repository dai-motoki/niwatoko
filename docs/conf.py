# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'niwatoko'
copyright = '2023, Your Name'
author = 'Your Name'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # 'sphinxcontrib.vercelwebapp',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',  # todoディレクティブを有効にする
    'sphinx.ext.mathjax',  # 数式のレンダリングを有効にする
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'  # alabasterテーマを使用
html_static_path = ['_static']

# -- Options for autodoc extension -------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#configuration

autodoc_member_order = 'bysource'
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'private-members': True,
    'special-members': '__init__',
    'inherited-members': True,
    'show-inheritance': True,
}

# -- Options for napoleon extension ------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html#configuration

napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = True
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True  # examplesをアドモニションとして表示
napoleon_use_admonition_for_notes = True  # notesをアドモニションとして表示
napoleon_use_admonition_for_references = True  # referencesをアドモニションとして表示
napoleon_use_ivar = True  # インスタンス変数の説明を表示
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = True
napoleon_type_aliases = None
napoleon_attr_annotations = True

# -- 日本語で説明を追加 -------------------------------------------------------

# このconf.pyファイルは、Sphinxドキュメントジェネレーターの設定ファイルです。
# プロジェクト情報、一般的な設定、拡張機能の設定、HTML出力のオプションなどを定義しています。

# プロジェクト情報セクションでは、プロジェクト名、著作権表示、作者名、リリースバージョンを指定します。

# 一般的な設定セクションでは、使用する拡張機能、テンプレートパス、除外パターンなどを設定します。
# ここでは、autodoc、viewcode、napoleon、todo、mathjaxという5つの拡張機能を有効にしています。

# HTML出力のオプションセクションでは、HTMLテーマとスタティックファイルのパスを指定します。
# ここでは、alabasterテーマを使用しています。

# autodoc拡張機能のオプションセクションでは、autodocの動作を制御するための設定を行います。
# メンバーの表示順序、デフォルトのオプションなどを指定しています。

# napoleon拡張機能のオプションセクションでは、napoleonの動作を制御するための設定を行います。
# Google形式とNumPy形式のdocstringをサポートし、各種の設定オプションを指定しています。
# examples、notes、referencesをアドモニションとして表示するように設定しています。

# これらの設定を適切に行うことで、Sphinxを使用してプロジェクトのドキュメントを生成することができます。
# Configuration file for the Sphinx documentation builder.
# ...

# Sphinxには他にも多くの機能や設定オプションがあるので、必要に応じて公式ドキュメントを参照してください。
# ドキュメントのソースファイル（.rstまたは.mdファイル）を編集し、再度ビルドコマンドを実行することで、
# ドキュメントを更新することができます。

# Sphinxには他にも多くの機能や設定オプションがあるので、必要に応じて公式ドキュメントを参照してください。

# -- ドキュメントの構成 --------------------------------------------------------

# index.rst をルートドキュメントとして設定
master_doc = 'index'

# ドキュメントの章立てを定義
# ここでは、各rstファイルをtoctreeディレクティブで指定しています
# ファイル名（拡張子なし）を指定することで、そのファイルの内容が組み込まれます
toctree = [
    'requirements',
    'installation',
    'usage',
    'modules',
    'contributing',
    'authors',
    'history',
]

# toctreeディレクティブのオプションを設定
# maxdepth: 目次の最大の深さ
# caption: 目次のキャプション
# glob: ワイルドカードを使用してファイルを指定可能にする
# hidden: 目次自体は表示しないが、内容は組み込む
toctree_options = {
    'maxdepth': 2,
    'caption': 'Contents:',
    'glob': True,
    'hidden': True,
}

# 以上の設定により、以下のようなドキュメントの構成になります:
# 
# index.rst
# ├── requirements.rst
# ├── installation.rst
# ├── usage.rst
# ├── modules.rst
# ├── contributing.rst
# ├── authors.rst
# └── history.rst
# 
# index.rstがルートドキュメントとなり、その下に各rstファイルの内容が組み込まれます。
# toctreeディレクティブにより、目次が自動生成されます。
# 
# これで、ドキュメントの基本的な構成が完成しました。
# 各rstファイルに適切な内容を記述することで、プロジェクトのドキュメントを整備していきましょう。

