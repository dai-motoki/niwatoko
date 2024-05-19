Here is the English translation of the `usage` section:

niwatoko Language Usage
======================

The niwatoko language is a Python-based natural language programming language. You can use it following these steps:

1. Install the niwatoko language.

   ```shell
   pip install niwatoko
   ```

2. niwatoko is a natural language programming language that can be used in the shell. There are two ways to use it:

   - Interpreter mode: There are two ways to use it in this mode.
     1. Running the `niwatoko` command alone will bring up an interpreter screen, similar to Python. You can enter natural language commands here and execute them interactively.

        ```shell
        $ niwatoko
        niwatoko> Please display "Hello, World!"
        Hello, World!
        niwatoko>
        ```

     2. You can also pass the natural language command as a command-line argument to `niwatoko "command"`. This will directly output the result of executing the command.

        ```shell
        $ niwatoko "Please display 'Hello, World!'"
        Hello, World!
        ```

   - Compiler mode: You can directly execute natural language source code files using the `niwatoko` command.

     ```shell
     $ niwatoko example.md
     ```

     The natural language source code in the `example.md` file will be executed directly, without generating compiled Python code.

3. niwatoko is a natural language programming language that can be used as an alternative to Python. It provides the same functionality as Python, but allows you to write more intuitive and readable code. Here are some examples of niwatoko programs written in pure natural language, ranging from simple to more complex:

   ```md
   Display "Hello, World!"
   ```

   ```md
   Ask the user for their name
   Assign the input name to the variable name
   Display "Hello, " + name + "!"
   ```

   ```md
   Define a function Fibonacci(n):
       # If n is less than or equal to 0, return 0
       If n is less than or equal to 0:
           Return 0
       # If n is 1, return 1
       If n is 1:
           Return 1
       # Otherwise, recursively calculate the Fibonacci number
       Else:
           Return Fibonacci(n - 1) + Fibonacci(n - 2)

   # Display the Fibonacci numbers from 1 to 10
   For i from 1 to 10:
       Display i + "-th Fibonacci number is " + Fibonacci(i)
   ```

   ```md
   Define a function is_prime(n):
       If n is less than 2:
           Return False
       For i from 2 to n-1:
           If n is divisible by i:
               Return False
       Return True

   Assign the input number to num
   If is_prime(num):
       Display num + " is a prime number"
   Else:
       Display num + " is not a prime number"
   ```

   The above examples, written in Markdown, demonstrate natural language programming concepts from Hello World to prime number checking. By using Markdown, you can express programming concepts in natural language, making the code more understandable, especially for beginners.

   When you execute these Markdown programs, you will get the following results:

   ```shell
   $ niwatoko hello_world.md
   Hello, World!

   $ niwatoko greeting.md
   Please enter your name: Yamada
   Hello, Yamada!

   $ niwatoko fibonacci.md
   1st Fibonacci number is 1
   2nd Fibonacci number is 1
   3rd Fibonacci number is 2
   4th Fibonacci number is 3
   5th Fibonacci number is 5
   6th Fibonacci number is 8
   7th Fibonacci number is 13
   8th Fibonacci number is 21
   9th Fibonacci number is 34
   10th Fibonacci number is 55

   $ niwatoko prime_number.md
   Please enter a number: 17
   17 is a prime number

   $ niwatoko prime_number.md
   Please enter a number: 24
   24 is not a prime number
   ```

4. Advanced Usage

Here is an example of a Grimoire generation script:

   ```md
   ## Input Information:
   - `Author` = Daisuke Motoki
   - The prompt or ritual to be explained is as follows: `Ritual` =
   ```
   ```
   I want to ~, so please write a good issue on the gh command, make an implementation plan for it, get the #number, and create a branch that includes it. Then, automatically open the issue URL (lang ja)
   ```

   - Options
       - `Requirement` = [Create a new python package for the Zoltraak app Grimoire]
       - `Requirement` = [Chatbot development using Dify]
       - `Prerequisite` = [Run on Open Interpreter]
       - `LLM Used` = GPT-4

   ## Grimoire Generation AI
   ### Knowledge
   - `Category Type` = 
       - Marketing
       - HR
       - Sales
       - Consulting
       - PM
       - Design
       - Development
       - Administrative

   ### Skills
   #### Writing (`Ritual`)
   - Document the following
   - Propose a `Category` from the `Category Type` based on the `Ritual`
   ```
   『 (Write a concise title based on the `Ritual`, and append "Ritual")』 Author: `Author`, Category: `Category`

   `Ritual`:
   Magic Effect: Briefly describe the magic effect details from the `Ritual`
   Special Effect: Briefly describe the special effect details from the `Ritual`
   Prerequisite: Describe the `Prerequisite` based on the `LLM Used` and the `Ritual`
   ```

   ## Workflow:
   1. Look at the `Input Information` and use the `Writing` skill from the `Grimoire Generation AI` to just write the explanation.
   2. Provide an example of executing the `Ritual`
       - If there are `Requirement` options, base it on those
       - The `Ritual` is first used by a person.
       - Do not modify the content of the description.
       - Describe the usage in a dialogue between a person and AI, in a formal tone.
   3. Propose an image generation prompt for expressing the `Ritual`
       - In English
       - In Japanese