# niwatoko v1.1.3

We have reproduced Anthropic's document variable feature as the second open-source implementation in the world*, and provided a module import feature (world's first*).

## Update Contents

### Addition of Import (Citation) Feature
- You can now quote the contents of other files within a Markdown file.
- This improves the reusability of code and makes document management easier.

- The citation method is as follows:
   ```markdown
   - `variable_name` = extension [./file_path(without extension)]
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


1. For those who have already set up Python and Anthropic keys, you can use the following command:

   ```
   pip install niwatoko
   ```

   Or, to upgrade to the latest version, run the following command:
   
   ```
   pip install --upgrade niwatoko
   ```


## Practice Problems

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
- `multiplication_py` = py [./test_import_module_multiple]  

## TODO
Please convert `addition_py` and `multiplication_py` to a Japanese-only requirements specification document.
Also, please describe the necessary tests.
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