# Deutsche Übersetzung:

# niwatoko v1.1.3

Wir haben die Dokumentvariablenfunktion von Anthropic als Open Source (weltweit die Zweite*) nachgebildet und eine Modulimportfunktion (weltweit die Erste*) bereitgestellt.

## Aktualisierungen

### Hinzufügen der Importfunktion (Zitieren)
- Sie können nun den Inhalt anderer Dateien in Markdown-Dateien zitieren.
- Dadurch wird die Wiederverwendbarkeit des Codes erhöht und die Verwaltung der Dokumentation erleichtert.

- Die Zitierweise ist wie folgt:
   ```markdown
   - `Variablenname` = Erweiterung [./Dateipfad(ohne Erweiterung)]
   - `Variablenname` = [./Dateipfad]
   ```
- Beispiel:
   ```markdown
    `hello.py` = py [./hello]
    `hello.py` = [./hello.py]
   ```
- Diese Funktion ist ein Weltpremiere.
- Bitte beachten Sie, dass die Dateiendung (.py) in eckige Klammern [] eingeschlossen werden muss.

### Hinzufügen der Dokumentvariablenfunktion
- Sie können Variablen in Markdown-Dateien definieren und an anderer Stelle referenzieren.
- Dadurch wird die Lesbarkeit und Wartbarkeit der Dokumentation verbessert.
- Diese Funktion ist nach Anthropic die zweite Implementierung weltweit.

## Installation

Weitere Details finden Sie unter folgendem Link:
[https://niwatoko2.vercel.app/installation.html](https://niwatoko2.vercel.app/installation.html)


1. Für Benutzer, die Python und Anthropic-Schlüssel bereits eingerichtet haben, können Sie wie folgt verwenden:

   ```
   pip install niwatoko
   ```

   Oder führen Sie den folgenden Befehl aus, um auf die neueste Version zu aktualisieren:
   
   ```
   pip install --upgrade niwatoko
   ```


## Übungsaufgabe

Bitte verwenden Sie die folgenden Schritte:
- Vorbereitung
1. Klonen Sie den Hauptzweig dieses Repositorys.

   ```
   git clone -b main https://github.com/dai-motoki/niwatoko.git
   ```

2. Wechseln Sie in das geklonte Verzeichnis.

   ```
   cd niwatoko/tests/test_docs/test_niwatoko_v1.1.3
   ```

- Ausführung

1. Bereiten Sie die Datei `test_input.md` vor. Diese Datei enthält den Testinhalt.

```test_input.md
## Zitate
- `addition_py` = py [./test_import_module_add]
```py
def add(a, b):
    """
    Funktion zum Addieren von zwei Zahlen

    Parameter:
    a (int oder float): Erste Zahl
    b (int oder float): Zweite Zahl

    Rückgabe:
    int oder float: Summe von a und b
    """
    return a + b

def add_list(numbers):
    """
    Funktion zum Berechnen der Summe einer Liste von Zahlen

    Parameter:
    numbers (Liste): Liste von Zahlen

    Rückgabe:
    int oder float: Summe der Zahlen
    """
    total = 0
    for num in numbers:
        total = add(total, num)
    return total

def add_multiple(*args):
    """
    Funktion zum Addieren mehrerer Zahlen

    Parameter:
    *args: Variabel-lange Argumente. Akzeptiert eine beliebige Anzahl numerischer Werte

    Rückgabe:
    int oder float: Summe der übergebenen Argumente
    """
    return add_list(args)
```
- `multiplication_py` = py [./test_import_module_multiple]  
```py
def multiply(a, b):
    """
    Funktion zum Multiplizieren von zwei Zahlen

    Parameter:
    a (int oder float): Erste Zahl
    b (int oder float): Zweite Zahl

    Rückgabe:
    int oder float: Produkt von a und b
    """
    return a * b

def multiply_list(numbers):
    """
    Funktion zum Berechnen des Produkts einer Liste von Zahlen

    Parameter:
    numbers (Liste): Liste von Zahlen

    Rückgabe:
    int oder float: Produkt der Zahlen
    """
    total = 1
    for num in numbers:
        total = multiply(total, num)
    return total


def multiply_multiple(*args):
    """
    Funktion zum Multiplizieren mehrerer Zahlen

    Parameter:
    *args: Variabel-lange Argumente. Akzeptiert eine beliebige Anzahl numerischer Werte

    Rückgabe:
    int oder float: Produkt der übergebenen Argumente
    """
    return multiply_list(args)```

## TODO
Konvertieren Sie `addition_py` und `multiplication_py` in ein japanisches Lastenheft und beschreiben Sie die erforderlichen Tests.
```

2. Führen Sie den folgenden Befehl aus, um den Inhalt von `test_input.md` zu konvertieren und in `output.md` auszugeben:

   ```
   niwatoko test_input.md -o output.md
   ```

3. Führen Sie den folgenden Befehl aus, um den Inhalt von `output.md` in Python-Code zu konvertieren und in `output.py` auszugeben:

   ```
   niwatoko output.md -o output.py
   ```

4. Überprüfen Sie den Inhalt der generierten Dateien `output.md` und `output.py` und stellen Sie sicher, dass die Ausgabe wie erwartet ist.

5. Wiederholen Sie die Schritte, bis Sie die erwartete Ausgabe erhalten.