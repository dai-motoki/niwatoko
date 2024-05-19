
import subprocess
import os

def test_niwatoko_conversion():
    # # Setup the test environment
    
    # os.chdir('./tests/test_docs/test_niwatoko_v1.1.3')
    
    # Remove the output file if it exists
    if os.path.exists('output.md'):
        os.remove('output.md')
    
    # Run the niwatoko command
    command = 'niwatoko test_multi_format_file.md -o output.md'
    subprocess.run(command, shell=True, check=True)
    
    # Check if the output file is created
    assert os.path.exists('output.md'), 'Output file was not created.'
    
    # Check if the output file is not empty
    with open('output.md', 'r') as file:
        content = file.read()
        assert content, 'Output file is empty.'
    
    print('Test Passed: output.md is created and not empty.')

test_niwatoko_conversion()
