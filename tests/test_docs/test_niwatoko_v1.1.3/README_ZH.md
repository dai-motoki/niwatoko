以下は中国語への翻訳です:

# niwatoko v1.1.3

我们复制了Anthropic的文档变量功能,作为世界第二个*开源实现,并提供了模块导入功能,这是世界首创*。

## 更新内容

### 添加导入(引用)功能
- 现在可以在Markdown文件中引用其他文件的内容。
- 这提高了代码的可重用性,并简化了文档管理。

- 引用方法如下:
   ```markdown
   - `变量名` = 扩展名 [./文件路径(删除扩展名)]
   - `变量名` = [./文件路径]
   ```
- 例如:
   ```markdown
    `hello.py` = py [./hello]
    `hello.py` = [./hello.py]
   ```
- 这是世界首创的功能。
- 请注意,文件扩展名(.py)必须包含在方括号[]中。

### 添加文档变量功能
- 现在可以在Markdown文件中定义变量,并在其他地方引用该变量。
- 这提高了文档的可读性和可维护性。
- 这个功能是继Anthropic之后世界第二个实现。

## 安装

有关详细信息,请参阅以下网址:
[https://niwatoko2.vercel.app/installation.html](https://niwatoko2.vercel.app/installation.html)


1. 对于已经设置好Python和Anthropic密钥的用户,可以使用以下命令使用:

   ```
   pip install niwatoko
   ```

   或者,要升级到最新版本,请运行以下命令:
   
   ```
   pip install --upgrade niwatoko
   ```


## 练习题

请按以下步骤操作:
- 准备
1. 克隆此存储库的main分支。

   ```
   git clone -b main https://github.com/dai-motoki/niwatoko.git
   ```

2. 切换到克隆的目录。

   ```
   cd niwatoko/tests/test_docs/test_niwatoko_v1.1.3
   ```

- 执行

1. 准备`test_input.md`文件。该文件包含要测试的输入内容。

```test_input.md
## 引用
- `addition_py` = py [./test_import_module_add]
```py
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
```
- `multiplication_py` = py [./test_import_module_multiple]  
```py
def multiply(a, b):
    """
    Function to multiply two numbers

    Parameters:
    a (int or float): First number
    b (int or float): Second number

    Returns:
    int or float: Product of a and b
    """
    return a * b

def multiply_list(numbers):
    """
    Function to calculate the product of a list of numbers

    Parameters:
    numbers (list): List of numbers

    Returns:
    int or float: Product of numbers
    """
    total = 1
    for num in numbers:
        total = multiply(total, num)
    return total


def multiply_multiple(*args):
    """
    Function to multiply multiple numbers

    Parameters:
    *args: Variable-length arguments. Accepts any number of numeric values

    Returns:
    int or float: Product of the passed arguments
    """
    return multiply_list(args)```

## TODO
请将 `addition_py` 和 `multiplication_py` 转换为仅包含日语的需求规格说明书。
同时,请编写必要的测试用例。
```

2. 运行以下命令,将`test_input.md`的内容转换并输出到`output.md`文件:

   ```
   niwatoko test_input.md -o output.md
   ```

3. 运行以下命令,将`output.md`的内容转换为Python代码并输出到`output.py`文件:

   ```
   niwatoko output.md -o output.py
   ```

4. 检查生成的`output.md`和`output.py`文件的内容,确保输出符合预期。

5. 如果输出不符合预期,请重复执行上述步骤,直到获得预期的输出。