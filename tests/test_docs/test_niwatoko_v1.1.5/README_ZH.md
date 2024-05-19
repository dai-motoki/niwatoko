以下は中国語への翻訳です:

# niwatoko v1.1.5
# niwatoko v1.1.5

Niwatoko编程语言开始提供模块导入功能(世界首创*)。
Niwatoko编程语言开始提供模块导入功能(世界首创*)。
Anthropic的提示生成器生成的带有变量的Markdown文件现在可以在Niwatoko中处理。
Anthropic的提示生成器生成的带有变量的Markdown文件现在可以在Niwatoko中处理。

## 更新内容
## 更新内容

### 添加导入(引用)功能
### 添加导入(引用)功能
- 现在可以在Markdown文件中引用其他文件的内容。
- 现在可以在Markdown文件中引用其他文件的内容。
- 这提高了代码的可重用性,并简化了文档管理。
- 这提高了代码的可重用性,并简化了文档管理。

- 引用方法如下:
- 引用方法如下:
   ```markdown
   ```markdown
   - `变量名` = 扩展名 [./文件路径(删除扩展名)]
   - `变量名` = 扩展名 [./文件路径(删除扩展名)]
   - `变量名` = [./文件路径]
   - `变量名` = [./文件路径]
   ```
   ```
- 例如:
- 例如:
   ```markdown
   ```markdown
    `hello.py` = py [./hello]
    `hello.py` = py [./hello]
    `hello.py` = [./hello.py]
    `hello.py` = [./hello.py]
   ```
   ```
- 这是一个世界首创的功能。
- 这是一个世界首创的功能。
- 请注意,文件扩展名(.py)必须包含在方括号[]中。
- 请注意,文件扩展名(.py)必须包含在方括号[]中。

### 添加文档变量功能
### 添加文档变量功能
```
```
- 现在可以在Markdown文件中定义 {{变量}} ,并在其他地方引用该 {{变量}} 。
```
```
- 现在可以在Markdown文件中定义 {{变量}} ,并在其他地方引用该 {{变量}} 。
  - 例如,写 `{{变量名}}` 会读取同一目录下的 `变量名.md` 文件。
```
```
  - 例如,写 `{{变量名}}` 会读取同一目录下的 `变量名.md` 文件。
- 这提高了文档的可读性和可维护性。
- 这提高了文档的可读性和可维护性。

## 安装
## 安装
```
```

有关详细信息,请参阅以下网址:
有关详细信息,请参阅以下网址:
[https://niwatoko2.vercel.app/installation.html](https://niwatoko2.vercel.app/installation.html)

1. 对于已经设置好Python和Anthropic密钥的用户,可以使用以下命令:
1. 对于已经设置好Python和Anthropic密钥的用户,可以使用以下命令:

   ```
   ```
   pip install niwatoko
   pip install niwatoko
   ```
   ```

   或者,要升级到最新版本,请运行以下命令:
   或者,要升级到最新版本,请运行以下命令:

   ```
   ```
   pip install --upgrade niwatoko
   pip install --upgrade niwatoko
   ```
   ```

## 练习问题
## 练习问题

请按照以下步骤操作:
请按照以下步骤操作:
- 准备
- 准备
1. 克隆此存储库的main分支。
1. 克隆此存储库的main分支。

   ```
   ```
   git clone -b main https://github.com/dai-motoki/niwatoko.git
   git clone -b main https://github.com/dai-motoki/niwatoko.git
   ```
   ```

2. 进入克隆的目录。
2. 进入克隆的目录。

   ```
   ```
   cd niwatoko/tests/test_docs/test_niwatoko_v1.1.3
   cd niwatoko/tests/test_docs/test_niwatoko_v1.1.3
   ```
   ```

- 执行
- 执行

1. 准备 `test_input.md` 文件。该文件包含要测试的输入内容。
1. 准备 `test_input.md` 文件。该文件包含要测试的输入内容。

```test_input.md
```test_input.md
## 引用
## 引用
- `addition_py` = py [./test_import_module_add]
- `addition_py` = py [./test_import_module_add]
```py
```
- `multiplication_py` = py [./test_import_module_multiple]  
- `multiplication_py` = py [./test_import_module_multiple]  
```py
```

## TODO
## TODO
请将 `addition_py` 和 `multiplication_py` 转换为日语需求规格书,并编写必要的测试。
请将 `addition_py` 和 `multiplication_py` 转换为日语需求规格书,并编写必要的测试。
```
```

2. 运行以下命令,将 `test_input.md` 的内容转换并输出到 `output.md` 文件:
2. 运行以下命令,将 `test_input.md` 的内容转换并输出到 `output.md` 文件:

   ```
   ```
   niwatoko test_input.md -o output.md
   niwatoko test_input.md -o output.md
   ```
   ```

3. 运行以下命令,将 `output.md` 的内容转换为Python代码并输出到 `output.py` 文件:
3. 运行以下命令,将 `output.md` 的内容转换为Python代码并输出到 `output.py` 文件:

   ```
   ```
   niwatoko output.md -o output.py
   niwatoko output.md -o output.py
   ```
   ```

4. 检查生成的 `output.md` 和 `output.py` 文件的内容,确保输出符合预期。
4. 检查生成的 `output.md` 和 `output.py` 文件的内容,确保输出符合预期。

5. 如果输出不符合预期,请重复执行步骤。
5. 如果输出不符合预期,请重复执行步骤。