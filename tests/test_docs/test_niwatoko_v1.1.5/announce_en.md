Natural language programming with niwatoko
Now supports GPT-4o! 🎉

You can start using it right away by specifying the model as follows:

niwatoko graph.md -o output.py -m openai-gpt4o

Installation method
pip install niwatoko


The available models are:
- openai-gpt-turbo
- openai-gpt4o 
- claude-haiku
- claude-sonnet
- claude-opu

The file can import other files using the following syntax:
- `variable_name` = [file_path]

For example:
- `zoltraak` = [./zoltraak2.csv]
- `niwatoko` = [./niwatoko2.csv]
- `def_graph` = [./def_graph.md]
