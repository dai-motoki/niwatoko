Ecco la traduzione in italiano:

# niwatoko v1.1.4
# niwatoko v1.1.4

Il linguaggio di programmazione Niwatoko ha iniziato a fornire la funzionalità di importazione di moduli (prima al mondo*).
Il linguaggio di programmazione Niwatoko ha iniziato a fornire la funzionalità di importazione di moduli (prima al mondo*).
È ora possibile elaborare i file Markdown con variabili generati dal generatore di prompt di Anthropic in Niwatoko.
È ora possibile elaborare i file Markdown con variabili generati dal generatore di prompt di Anthropic in Niwatoko.


## Contenuti dell'aggiornamento
## Contenuti dell'aggiornamento

### Aggiunta della funzionalità di importazione (citazione)
### Aggiunta della funzionalità di importazione (citazione)
- È ora possibile citare il contenuto di altri file all'interno di un file Markdown.
- È ora possibile citare il contenuto di altri file all'interno di un file Markdown.
- Ciò migliora la riutilizzabilità del codice e semplifica la gestione della documentazione.
- Ciò migliora la riutilizzabilità del codice e semplifica la gestione della documentazione.

- Il metodo di citazione è il seguente:
- Il metodo di citazione è il seguente:
   ```markdown
   ```markdown
   - `nome_variabile` = estensione [./percorso_file(senza_estensione)]
   - `nome_variabile` = estensione [./percorso_file(senza_estensione)]
   - `nome_variabile` = [./percorso_file]
   - `nome_variabile` = [./percorso_file]
   ```
   ```
- Esempio:
- Esempio:
   ```markdown
   ```markdown
    `hello.py` = py [./hello]
    `hello.py` = py [./hello]
    `hello.py` = [./hello.py]
    `hello.py` = [./hello.py]
   ```
   ```
- Questa funzionalità è un'iniziativa pionieristica a livello mondiale.
- Questa funzionalità è un'iniziativa pionieristica a livello mondiale.
- Nota che l'estensione del file (.py) deve essere inclusa tra parentesi quadre [].
- Nota che l'estensione del file (.py) deve essere inclusa tra parentesi quadre [].

### Aggiunta della funzionalità di variabili di documentazione
### Aggiunta della funzionalità di variabili di documentazione
```
```
- È ora possibile definire variabili {{variabile}} all'interno dei file Markdown e farvi riferimento in altri punti.
```
```
- È ora possibile definire variabili {{variabile}} all'interno dei file Markdown e farvi riferimento in altri punti.
  - Ad esempio, scrivendo `{{nome_variabile}}`, verrà caricato il file `nome_variabile.md` nello stesso livello gerarchico.
```
```
  - Ad esempio, scrivendo `{{nome_variabile}}`, verrà caricato il file `nome_variabile.md` nello stesso livello gerarchico.
- Ciò migliora la leggibilità e la manutenibilità della documentazione.
- Ciò migliora la leggibilità e la manutenibilità della documentazione.

## Installazione
## Installazione
```
```

Per maggiori informazioni, consultare il seguente URL:
Per maggiori informazioni, consultare il seguente URL:
[https://niwatoko2.vercel.app/installation.html](https://niwatoko2.vercel.app/installation.html)

1. Per gli utenti che hanno già configurato Python e la chiave di Anthropic, è possibile utilizzare il seguente comando:
1. Per gli utenti che hanno già configurato Python e la chiave di Anthropic, è possibile utilizzare il seguente comando:

   ```
   ```
   pip install niwatoko
   pip install niwatoko
   ```
   ```

   In alternativa, per aggiornare all'ultima versione, eseguire il seguente comando:
   In alternativa, per aggiornare all'ultima versione, eseguire il seguente comando:

   ```
   ```
   pip install --upgrade niwatoko
   pip install --upgrade niwatoko
   ```
   ```

## Esercizio
## Esercizio

Seguire questa procedura:
Seguire questa procedura:
- Preparazione
- Preparazione
1. Clonare il ramo principale (main) di questo repository.
1. Clonare il ramo principale (main) di questo repository.

   ```
   ```
   git clone -b main https://github.com/dai-motoki/niwatoko.git
   git clone -b main https://github.com/dai-motoki/niwatoko.git
   ```
   ```

2. Spostarsi nella directory clonata.
2. Spostarsi nella directory clonata.

   ```
   ```
   cd niwatoko/tests/test_docs/test_niwatoko_v1.1.3
   cd niwatoko/tests/test_docs/test_niwatoko_v1.1.3
   ```
   ```

- Esecuzione
- Esecuzione

1. Preparare il file `test_input.md`. Questo file contiene il contenuto di input da testare.
1. Preparare il file `test_input.md`. Questo file contiene il contenuto di input da testare.

```test_input.md
```test_input.md
## Citazione
## Citazione
- `addition_py` = py [./test_import_module_add]
- `addition_py` = py [./test_import_module_add]
```py
```
- `multiplication_py` = py [./test_import_module_multiple]  
- `multiplication_py` = py [./test_import_module_multiple]  
```py
```

## TODO
## TODO
Convertire `addition_py` e `multiplication_py` in una specifica dei requisiti in sola lingua giapponese.
Convertire `addition_py` e `multiplication_py` in una specifica dei requisiti in sola lingua giapponese.
Descrivere anche i test necessari.
Descrivere anche i test necessari.
```
```

2. Eseguire il seguente comando per convertire il contenuto di `test_input.md` e salvarlo in `output.md`:
2. Eseguire il seguente comando per convertire il contenuto di `test_input.md` e salvarlo in `output.md`:

   ```
   ```
   niwatoko test_input.md -o output.md
   niwatoko test_input.md -o output.md
   ```
   ```

3. Eseguire il seguente comando per convertire il contenuto di `output.md` in codice Python e salvarlo in `output.py`:
3. Eseguire il seguente comando per convertire il contenuto di `output.md` in codice Python e salvarlo in `output.py`:

   ```
   ```
   niwatoko output.md -o output.py
   niwatoko output.md -o output.py
   ```
   ```

4. Verificare il contenuto dei file `output.md` e `output.py` generati e assicurarsi che l'output sia come previsto.
4. Verificare il contenuto dei file `output.md` e `output.py` generati e assicurarsi che l'output sia come previsto.

5. Ripetere l'esecuzione finché non si ottiene l'output desiderato.
5. Ripetere l'esecuzione finché non si ottiene l'output desiderato.