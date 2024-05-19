Tradução para o português:

# niwatoko v1.1.5
# niwatoko v1.1.5

A linguagem de programação Niwatoko agora oferece o recurso de importação de módulos (primeira do mundo*).
A linguagem de programação Niwatoko agora oferece o recurso de importação de módulos (primeira do mundo*).
Agora é possível processar arquivos Markdown com variáveis gerados pelo gerador de prompts da Anthropic no Niwatoko.
Agora é possível processar arquivos Markdown com variáveis gerados pelo gerador de prompts da Anthropic no Niwatoko.

## Conteúdo da atualização

### Adição da funcionalidade de importação (citação)
- Agora é possível citar o conteúdo de outros arquivos dentro de um arquivo Markdown.
- Isso melhora a reutilização de código e facilita o gerenciamento de documentos.

- O método de citação é o seguinte:
   ```markdown
   - `variável` = extensão [./caminho_do_arquivo(sem_extensão)]
   - `variável` = [./caminho_do_arquivo]
   ```
- Exemplo:
   ```markdown
    `hello.py` = py [./hello]
    `hello.py` = [./hello.py]
   ```
- Este é um recurso pioneiro no mundo.
- Observe que a extensão do arquivo (.py) deve estar entre colchetes [].

### Adição da funcionalidade de variáveis de documento
- Agora é possível definir variáveis `{{variável}}` em um arquivo Markdown e referenciá-las em outros lugares.
  - Por exemplo, `{{variável}}` carregará o arquivo `variável.md` no mesmo diretório.
- Isso melhora a legibilidade e a manutenibilidade da documentação.

## Instalação

Veja mais detalhes no seguinte URL:
[https://niwatoko2.vercel.app/installation.html]

1. Para usuários que já têm o Python e a chave da Anthropic configurados, você pode usar o seguinte comando:

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

1. Prepare o arquivo `test_input.md`. Esse arquivo contém o conteúdo de entrada a ser testado.

```test_input.md
## Citação
- `addition_py` = py [./test_import_module_add]
```py
```
- `multiplication_py` = py [./test_import_module_multiple]  
```py
```

## TODO
`addition_py` e `multiplication_py` devem ser convertidos em um documento de especificação de requisitos em japonês.
Também descreva os testes necessários.
```

2. Execute o seguinte comando para converter o conteúdo de `test_input.md` e gerar o arquivo `output.md`:

   ```
   niwatoko test_input.md -o output.md
   ```

3. Execute o seguinte comando para converter o conteúdo de `output.md` em código Python e gerar o arquivo `output.py`:

   ```
   niwatoko output.md -o output.py
   ```

4. Verifique o conteúdo dos arquivos `output.md` e `output.py` gerados e confirme se a saída está de acordo com o esperado.

5. Repita a execução até obter a saída esperada.