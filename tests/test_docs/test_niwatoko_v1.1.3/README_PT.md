Tradução para o português:

# niwatoko v1.1.3

Nós reproduzimos a funcionalidade de variáveis de documento da Anthropic como o segundo projeto de código aberto do mundo* e fornecemos a funcionalidade de importação de módulos (primeira do mundo*).

## Atualizações

### Adição da funcionalidade de importação (citação)
- Agora é possível citar o conteúdo de outros arquivos dentro de arquivos Markdown.
- Isso melhora a reutilização de código e facilita o gerenciamento de documentos.

- O método de citação é o seguinte:
   ```markdown
   - `nome_da_variável` = extensão [./caminho_do_arquivo(sem_extensão)]
   - `nome_da_variável` = [./caminho_do_arquivo]
   ```
- Exemplo:
   ```markdown
    `hello.py` = py [./hello]
    `hello.py` = [./hello.py]
   ```
- Esta funcionalidade é a primeira do mundo.
- Observe que a extensão do arquivo (.py) deve estar entre colchetes [].

### Adição da funcionalidade de variáveis de documento
- Agora é possível definir variáveis em arquivos Markdown e referenciá-las em outros locais.
- Isso melhora a legibilidade e a manutenibilidade dos documentos.
- Esta funcionalidade é a segunda implementação do mundo, após a Anthropic.

## Instalação

Para obter mais detalhes, consulte o seguinte URL:
[https://niwatoko2.vercel.app/installation.html](https://niwatoko2.vercel.app/installation.html)


1. Se você já tiver o Python e as chaves da Anthropic configurados, poderá usar o seguinte comando:

   ```
   pip install niwatoko
   ```

   Ou, para atualizar para a versão mais recente, execute o seguinte comando:
   
   ```
   pip install --upgrade niwatoko
   ```


## Exercício

Siga as etapas abaixo:
- Preparação
1. Clone o branch principal deste repositório.

   ```
   git clone -b main https://github.com/dai-motoki/niwatoko.git
   ```

2. Navegue até o diretório clonado.

   ```
   cd niwatoko/tests/test_docs/test_niwatoko_v1.1.3
   ```

- Execução

1. Prepare o arquivo `test_input.md`. Este arquivo contém o conteúdo de entrada a ser testado.

```test_input.md
## Citação
- `addition_py` = py [./test_import_module_add]
```py
def add(a, b):
    """
    Função para adicionar dois números

    Parâmetros:
    a (int ou float): Primeiro número
    b (int ou float): Segundo número

    Retorna:
    int ou float: Soma de a e b
    """
    return a + b

def add_list(numbers):
    """
    Função para calcular a soma de uma lista de números

    Parâmetros:
    numbers (list): Lista de números

    Retorna:
    int ou float: Soma dos números
    """
    total = 0
    for num in numbers:
        total = add(total, num)
    return total

def add_multiple(*args):
    """
    Função para adicionar vários números

    Parâmetros:
    *args: Argumentos de comprimento variável. Aceita qualquer número de valores numéricos

    Retorna:
    int ou float: Soma dos argumentos passados
    """
    return add_list(args)
```
- `multiplication_py` = py [./test_import_module_multiple]  
```py
def multiply(a, b):
    """
    Função para multiplicar dois números

    Parâmetros:
    a (int ou float): Primeiro número
    b (int ou float): Segundo número

    Retorna:
    int ou float: Produto de a e b
    """
    return a * b

def multiply_list(numbers):
    """
    Função para calcular o produto de uma lista de números

    Parâmetros:
    numbers (list): Lista de números

    Retorna:
    int ou float: Produto dos números
    """
    total = 1
    for num in numbers:
        total = multiply(total, num)
    return total


def multiply_multiple(*args):
    """
    Função para multiplicar vários números

    Parâmetros:
    *args: Argumentos de comprimento variável. Aceita qualquer número de valores numéricos

    Retorna:
    int ou float: Produto dos argumentos passados
    """
    return multiply_list(args)```

## TODO
Converta `addition_py` e `multiplication_py` em um documento de especificação de requisitos apenas em japonês.
Além disso, descreva os testes necessários.
```

2. Execute o seguinte comando para converter o conteúdo de `test_input.md` e gerar o arquivo `output.md`:

   ```
   niwatoko test_input.md -o output.md
   ```

3. Execute o seguinte comando para converter o conteúdo de `output.md` em código Python e gerar o arquivo `output.py`:

   ```
   niwatoko output.md -o output.py
   ```

4. Verifique o conteúdo dos arquivos `output.md` e `output.py` gerados e certifique-se de que a saída está de acordo com o esperado.

5. Repita as etapas até obter a saída esperada.