Ecco la traduzione in italiano:

# niwatoko v1.1.3

Abbiamo riprodotto la funzionalità di variabili di documento open source (seconda al mondo*) di Anthropic e fornito la funzionalità di importazione di moduli (prima al mondo*).

## Aggiornamenti

### Aggiunta della funzionalità di importazione (citazione)
- È ora possibile citare il contenuto di altri file all'interno di un file Markdown.
- Ciò migliora la riutilizzabilità del codice e semplifica la gestione della documentazione.

- Il metodo di citazione è il seguente:
   ```markdown
   - `nome_variabile` = estensione [./percorso_file(senza_estensione)]
   - `nome_variabile` = [./percorso_file]
   ```
- Esempio:
   ```markdown
    `hello.py` = py [./hello]
    `hello.py` = [./hello.py]
   ```
- Questa funzionalità è un'iniziativa pionieristica a livello mondiale.
- Nota che l'estensione del file (.py) deve essere inclusa tra parentesi quadre [].

### Aggiunta della funzionalità di variabili di documento
- È ora possibile definire variabili all'interno di un file Markdown e farvi riferimento in altri punti.
- Ciò migliora la leggibilità e la manutenibilità della documentazione.
- Questa funzionalità è la seconda implementazione al mondo dopo Anthropic.

## Installazione

Per maggiori dettagli, consultare il seguente URL:
[https://niwatoko2.vercel.app/installation.html](https://niwatoko2.vercel.app/installation.html)


1. Per gli utenti che hanno già configurato Python e le chiavi di Anthropic, è possibile utilizzare il seguente comando:

   ```
   pip install niwatoko
   ```

   Per aggiornare all'ultima versione, eseguire invece il seguente comando:
   
   ```
   pip install --upgrade niwatoko
   ```


## Esercizio

Seguire questa procedura:
- Preparazione
1. Clonare il ramo principale (main) di questo repository.

   ```
   git clone -b main https://github.com/dai-motoki/niwatoko.git
   ```

2. Spostarsi nella directory clonata.

   ```
   cd niwatoko/tests/test_docs/test_niwatoko_v1.1.3
   ```

- Esecuzione

1. Preparare il file `test_input.md`. Questo file contiene il contenuto di input da testare.

```test_input.md
## Citazioni
- `addition_py` = py [./test_import_module_add]
```py
def add(a, b):
    """
    Funzione per sommare due numeri

    Parametri:
    a (int o float): Primo numero
    b (int o float): Secondo numero

    Restituisce:
    int o float: Somma di a e b
    """
    return a + b

def add_list(numbers):
    """
    Funzione per calcolare la somma di una lista di numeri

    Parametri:
    numbers (list): Lista di numeri

    Restituisce:
    int o float: Somma dei numeri
    """
    total = 0
    for num in numbers:
        total = add(total, num)
    return total

def add_multiple(*args):
    """
    Funzione per sommare più numeri

    Parametri:
    *args: Argomenti a lunghezza variabile. Accetta qualsiasi numero di valori numerici

    Restituisce:
    int o float: Somma degli argomenti passati
    """
    return add_list(args)
```
- `multiplication_py` = py [./test_import_module_multiple]  
```py
def multiply(a, b):
    """
    Funzione per moltiplicare due numeri

    Parametri:
    a (int o float): Primo numero
    b (int o float): Secondo numero

    Restituisce:
    int o float: Prodotto di a e b
    """
    return a * b

def multiply_list(numbers):
    """
    Funzione per calcolare il prodotto di una lista di numeri

    Parametri:
    numbers (list): Lista di numeri

    Restituisce:
    int o float: Prodotto dei numeri
    """
    total = 1
    for num in numbers:
        total = multiply(total, num)
    return total


def multiply_multiple(*args):
    """
    Funzione per moltiplicare più numeri

    Parametri:
    *args: Argomenti a lunghezza variabile. Accetta qualsiasi numero di valori numerici

    Restituisce:
    int o float: Prodotto degli argomenti passati
    """
    return multiply_list(args)```

## TODO
Convertire `addition_py` e `multiplication_py` in specifiche funzionali in sola lingua italiana.
Inoltre, descrivere i test necessari.
```

2. Eseguire il seguente comando per convertire il contenuto di `test_input.md` e generare il file `output.md`:

   ```
   niwatoko test_input.md -o output.md
   ```

3. Eseguire il seguente comando per convertire il contenuto di `output.md` in codice Python e generare il file `output.py`:

   ```
   niwatoko output.md -o output.py
   ```

4. Verificare il contenuto dei file `output.md` e `output.py` per assicurarsi che l'output sia come previsto.

5. Ripetere i passaggi finché non si ottiene l'output desiderato.