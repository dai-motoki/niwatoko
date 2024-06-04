# niwatoko - 自然言語プログラミング言語のPythonパッケージのsetup.pyファイルです。
# このファイルはパッケージのインストールや配布に必要な情報を含んでいます。

from setuptools import setup, find_packages

setup(
    name='niwatoko',
    version='1.2.10',
    description='自然言語でプログラミングを行うことができる新しいプログラミング言語',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='dai-motoki',
    author_email='dai.motoki1123@gmail.com',
    url='https://niwatoko2.vercel.app/',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'streamlit',
        'gradio',
        'openai',
        'anthropic',
        'opencv-python',
        'moviepy',
        'google-cloud-aiplatform'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: Japanese',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'niwatoko=niwatoko.cli:main',
        ],
    },
    package_data={
        '': ['*.txt', '*.md', '*.json', '*.csv', '*.yaml', '*.yml'],
        'niwatoko': ['foundation_model/interpretation/llm/*', 
                     'grammar/*'],
    },
)
