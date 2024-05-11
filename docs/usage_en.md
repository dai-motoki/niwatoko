Here is the English translation of the provided text:

niwatoko Language Usage
==============================

The niwatoko language is a Python-based natural language programming language. It can be used as follows:

1. Install the niwatoko language.

   .. code-block:: shell

      pip install niwatoko

2. niwatoko is a natural language programming language that can be used in the shell. There are two ways to use it:

   - Interpreter mode: There are two ways to use it.
     1. Running the `niwatoko` command alone will display the interpreter screen, similar to Python. You can enter natural language commands here and execute them interactively.

        .. code-block:: shell

           $ niwatoko
           niwatoko> Please display "Hello, World!"
           Hello, World!
           niwatoko>

     2. You can also pass the prompt as a command-line argument, like `niwatoko "Please display 'Hello, World!'"`, and the response will be directly output.

        .. code-block:: shell

           $ niwatoko "Please display 'Hello, World!'"
           Hello, World!

        This will convert the natural language command to Python code and execute it immediately. The result is displayed on the standard output.

   - Compiler mode: You can use the `niwatoko` command to directly execute natural language source code.

     .. code-block:: shell

        $ niwatoko example.md

     The natural language source code written in the `example.md` file will be executed directly, without generating compiled Python code. This is convenient as it allows you to run niwatoko programs without the need for compilation.

3. niwatoko is a natural language programming language that can be used as an alternative to Python. It provides the same functionality as Python, but allows you to write more intuitive and readable code. Here are some examples of niwatoko programs, ranging from simple to more complex:

   .. code-block:: md

      Display "Hello, World!"

   .. code-block:: md

      Ask the user for their name
      Assign the input name to the variable `name`
      Display "Hello, " + `name` + "!"

   .. code-block:: md

      Function Fibonacci(n):
          # If n is less than or equal to 0, return 0
          If `n` is less than or equal to 0:
              Return 0
          
          # If n is 1, return 1
          If `n` is 1:
              Return 1
          
          # Otherwise, recursively calculate the Fibonacci number
          Else:
              Return Fibonacci(`n` - 1) + Fibonacci(`n` - 2)

      # Display the Fibonacci numbers from 1 to 10
      For `i` from 1 to 10:
          Display `i` + "-th Fibonacci number is " + Fibonacci(`i`)

   .. code-block:: md

      Function is_prime(n):
          If `n` is less than 2:
              Return False
          For `i` from 2 to `n`-1:
              If `n` is divisible by `i`:
                  Return False
          Return True

      Assign the input number to `num`
      If is_prime(`num`):
          Display `num` + " is a prime number"
      Else:
          Display `num` + " is not a prime number"

   The above examples, written in Markdown, cover a range of programming concepts from Hello World to prime number detection. By using Markdown, the basic programming concepts can be expressed in natural language, making the code more understandable for beginners.

   When you execute these Markdown programs, you will get the following results:

   .. code-block:: shell

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

4. Advanced Usage

The following is a Grimoire generation formula:

   .. code-block:: md

      ## Input Information:
      - `Author` = Daisuke Motoki
      - The prompt or ritual to be explained is as follows: `Ritual` =   
      ```
      Since I want to ~, please write a good issue on the gh command, make an implementation plan for it, get the #number, and create a branch that includes it. Then, automatically open the issue URL (lang ja)
      ```

      - Options
          - `Requirement` = [For creating a new Python package for the Zoltraak app, Grimoire]
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
          - Administration

      ### Skills
      #### Writing (`Ritual`)
      - Document the following
      - Propose a `Category` from the `Category Type` based on the `Ritual`
      ```
      『 (Write a concise title based on the `Ritual`, and write "Ritual") 』 Author: `Author`, Category: `Category`

      `Ritual`:
      Magic Effect: Briefly describe the magic effect details from the `Ritual`
      Special Effect: Briefly describe the special effect details from the `Ritual`
      Prerequisite: Describe the `Prerequisite` based on the `LLM Used` and the `Ritual`
      ```

      ## Work Procedure:
      1. Look at the `Input Information` and use the `Writing` skill of the `Grimoire Generation AI` to only describe the explanation
      2. Provide an example of executing the `Ritual`
          - If there are `Requirements`, base it on that
          - The `Ritual` is first used by the user.
          - Do not modify the content of the description
          - Describe the usage in a dialogue between the user and the AI
          - Use a formal and polite tone
      3. Propose an image generation prompt for expressing the `Ritual`
          - In English
          - In Japanese