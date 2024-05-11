Here is the English translation of the installation guide for the niwatoko language:

niwatoko Language Installation
============================================

The niwatoko language can be installed using the following methods.

Install Locally
--------------------------

On Mac
~~~~~~~~~

1. Use Homebrew to install the latest version of Python. Follow these steps:

   a. Open the terminal and run the following command to check if Homebrew is installed:

      .. code-block:: shell

         brew --version

      If Homebrew is not installed, run the following command to install it:

      .. code-block:: shell

         /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

   b. Run the following command to install Python 3.11 using Homebrew:

      .. code-block:: shell

         brew install python@3.11

   c. Run the following command to set the Python PATH:

      .. code-block:: shell

         echo 'export PATH="/usr/local/opt/python@3.11/bin:$PATH"' >> ~/.zshrc

   d. Open a new terminal window or run the following command to apply the changes:

      .. code-block:: shell

         source ~/.zshrc

2. In the terminal, run the following command to check the Python version:

   .. code-block:: shell

      python --version

   Ensure that Python 3.11 is installed.

3. Pip is usually included with the Python installation. Run the following command to check the Pip version:

   .. code-block:: shell

      pip --version

4. Run the following command to install the niwatoko language:

   .. code-block:: shell

      pip install niwatoko

   This will install the latest version of the niwatoko language.

.. note::
   
   - Using Homebrew makes it easy to install the latest version of Python.
   - Use the python and pip commands to explicitly specify the installed Python 3.11.
   - Python 3.11 is the version that has been verified to be compatible with the niwatoko language.

On Windows
~~~~~~~~~~~~~

1. Download the Python 3.6 or later installer from the official Python website (https://www.python.org/downloads/).

2. Run the downloaded installer to install Python. It is recommended to select the "Add Python to PATH" option during installation.

3. Open the Command Prompt with administrative privileges.

4. Run the following command to check the Python version:

   .. code-block:: shell

      python --version

   Ensure that Python 3.6 or later is installed.

5. Run the following command to check the Pip version:

   .. code-block:: shell

      pip --version

   If Pip is not installed, run the following commands to install it:

   .. code-block:: shell

      curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
      python get-pip.py

6. Run the following command to install the niwatoko language:

   .. code-block:: shell

      pip install niwatoko

Install in a Virtual Environment
--------------------------

1. Create a virtual environment:

   .. code-block:: shell

      python -m venv myenv

2. Activate the virtual environment:

   On Mac:

   .. code-block:: shell

      source myenv/bin/activate

   On Windows:

   .. code-block:: shell

      myenv\Scripts\activate

3. Install the niwatoko language in the virtual environment:

   .. code-block:: shell

      pip install niwatoko

Use Docker
----------------

1. Ensure that Docker is installed.

2. Create the following Dockerfile:

   .. code-block:: dockerfile

      FROM python:3.9
      
      RUN pip install niwatoko
      
      WORKDIR /app

3. Build the Docker image:

   .. code-block:: shell

      docker build -t niwatoko .

4. Run the Docker container:

   .. code-block:: shell

      docker run -it --rm -v $(pwd):/app niwatoko

You are now ready to use the niwatoko language. Choose the appropriate installation method based on your environment.