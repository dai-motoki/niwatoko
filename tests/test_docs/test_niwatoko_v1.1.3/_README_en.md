# niwatoko v1.1.3

We have reproduced the Anthropic document variable feature as the second open-source implementation in the world*, and provided a module import feature (world's first*).

## Update Details

### Addition of Import (Citation) Feature
- You can now quote the contents of other files within a Markdown file.
- This improves the reusability of code and makes document management easier.

- The citation method is as follows:
   ```markdown
   - `variable_name` = extension [./file_path(without_extension)]
   - `variable_name` = [./file_path]
   ```
- Example:
   ```markdown
    `hello.py` = py [./hello]
    `hello.py` = [./hello.py]
   ```
- This feature is a world-first attempt.
- Note that the file extension (.py) must be included in the square brackets [].

### Addition of Document Variable Feature
- You can now define variables within a Markdown file and reference those variables in other places.
- This improves the readability and maintainability of the document.
- This feature is the second implementation in the world after Anthropic.

## Installation

Please refer to the following URL for details:
[https://niwatoko2.vercel.app/installation.html](https://niwatoko2.vercel.app/installation.html)


1. If you have already set up Python and Anthropic's key, you can use the following command:

   ```
   pip install niwatoko
   ```

   Or, to upgrade to the latest version, run the following command:
   
   ```
   pip install --upgrade niwatoko
   ```


## Practice Problem

Please use the following steps:
- Preparation
1. Clone the main branch of this repository.

   ```
   git clone -b main https://github.com/dai-motoki/niwatoko.git
   ```

2. Move to the cloned directory.

   ```
   cd niwatoko/tests/test_docs/test_niwatoko_v1.1.3
   ```

- Execution

1. Prepare the `test_input.md` file. This file contains the test input content.

```test_input.md
## Citation
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
Convert `addition_py` and `multiplication_py` to a Japanese-only functional specification document.
Also, describe the necessary tests.
```

2. Run the following command to convert the content of `test_input.md` and output it to the `output.md` file:

   ```
   niwatoko test_input.md -o output.md
   ```

3. Run the following command to convert the content of `output.md` to Python code and output it to the `output.py` file:

   ```
   niwatoko output.md -o output.py
   ```

4. Check the contents of the generated `output.md` and `output.py` files and verify that the output is as expected.

5. Repeat the execution until the expected output is obtained.