Übersetzung ins Deutsche:

# niwatoko v1.1.4
# niwatoko v1.1.4

Die Programmiersprache Niwatoko bietet nun die Funktion zum Importieren von Modulen (weltweit erstmalig*).
Die Programmiersprache Niwatoko bietet nun die Funktion zum Importieren von Modulen (weltweit erstmalig*).
Es ist nun möglich, mit Variablen versehene Markdown-Dateien, die vom Prompt-Generator von Anthropic erstellt wurden, in Niwatoko zu verarbeiten.
Es ist nun möglich, mit Variablen versehene Markdown-Dateien, die vom Prompt-Generator von Anthropic erstellt wurden, in Niwatoko zu verarbeiten.


## Aktualisierungen
## Aktualisierungen

### Hinzufügen der Import-(Zitat-)Funktion
### Hinzufügen der Import-(Zitat-)Funktion
- Es ist nun möglich, den Inhalt anderer Dateien innerhalb einer Markdown-Datei zu zitieren.
- Es ist nun möglich, den Inhalt anderer Dateien innerhalb einer Markdown-Datei zu zitieren.
- Dadurch wird die Wiederverwendbarkeit des Codes verbessert und die Verwaltung der Dokumentation erleichtert.
- Dadurch wird die Wiederverwendbarkeit des Codes verbessert und die Verwaltung der Dokumentation erleichtert.

- Die Zitierweise ist wie folgt:
- Die Zitierweise ist wie folgt:
   ```markdown
   ```markdown
   - `Variablenname` = Erweiterung [./Dateipfad(ohne Erweiterung)]
   - `Variablenname` = Erweiterung [./Dateipfad(ohne Erweiterung)]
   - `Variablenname` = [./Dateipfad]
   - `Variablenname` = [./Dateipfad]
   ```
   ```
- Beispiel:
- Beispiel:
   ```markdown
   ```markdown
    `hello.py` = py [./hello]
    `hello.py` = py [./hello]
    `hello.py` = [./hello.py]
    `hello.py` = [./hello.py]
   ```
   ```
- Diese Funktion ist ein weltweit erstmaliger Versuch.
- Diese Funktion ist ein weltweit erstmaliger Versuch.
- Bitte beachten Sie, dass die Dateiendung (.py) in eckige Klammern [] eingeschlossen werden muss.
- Bitte beachten Sie, dass die Dateiendung (.py) in eckige Klammern [] eingeschlossen werden muss.

### Hinzufügen der Dokumentationsvariablenfunktion
### Hinzufügen der Dokumentationsvariablenfunktion
```
```
- Es ist nun möglich, innerhalb einer Markdown-Datei {{Variablen}} zu definieren und diese {{Variablen}} an anderer Stelle zu referenzieren.
```
```
- Es ist nun möglich, innerhalb einer Markdown-Datei {{Variablen}} zu definieren und diese {{Variablen}} an anderer Stelle zu referenzieren.
  - Zum Beispiel wird, wenn Sie `{{Variablenname}}` schreiben, die Datei `Variablenname.md` aus dem gleichen Verzeichnis eingelesen.
```
```
  - Zum Beispiel wird, wenn Sie `{{Variablenname}}` schreiben, die Datei `Variablenname.md` aus dem gleichen Verzeichnis eingelesen.
- Dadurch wird die Lesbarkeit und Wartbarkeit der Dokumentation verbessert.
- Dadurch wird die Lesbarkeit und Wartbarkeit der Dokumentation verbessert.

## Installation
## Installation
```
```

Weitere Informationen finden Sie unter folgendem Link:
Weitere Informationen finden Sie unter folgendem Link:
[https://niwatoko2.vercel.app/installation.html](https://niwatoko2.vercel.app/installation.html)

1. Für Nutzer, die Python und den Anthropic-Schlüssel bereits eingerichtet haben, kann Niwatoko mit folgendem Befehl verwendet werden:
1. Für Nutzer, die Python und den Anthropic-Schlüssel bereits eingerichtet haben, kann Niwatoko mit folgendem Befehl verwendet werden:

   ```
   ```
   pip install niwatoko
   pip install niwatoko
   ```
   ```

   Oder um auf die neueste Version upzugraden, führen Sie bitte folgenden Befehl aus:
   Oder um auf die neueste Version upzugraden, führen Sie bitte folgenden Befehl aus:

   ```
   ```
   pip install --upgrade niwatoko
   pip install --upgrade niwatoko
   ```
   ```

## Übungsaufgabe
## Übungsaufgabe

Bitte verwenden Sie die folgenden Schritte:
Bitte verwenden Sie die folgenden Schritte:
- Vorbereitung
- Vorbereitung
1. Klonen Sie den main-Branch dieses Repositorys.
1. Klonen Sie den main-Branch dieses Repositorys.

   ```
   ```
   git clone -b main https://github.com/dai-motoki/niwatoko.git
   git clone -b main https://github.com/dai-motoki/niwatoko.git
   ```
   ```

2. Wechseln Sie in das geklonte Verzeichnis.
2. Wechseln Sie in das geklonte Verzeichnis.

   ```
   ```
   cd niwatoko/tests/test_docs/test_niwatoko_v1.1.3
   cd niwatoko/tests/test_docs/test_niwatoko_v1.1.3
   ```
   ```

- Ausführung
- Ausführung

1. Bereiten Sie die Datei `test_input.md` vor. Diese Datei enthält den Testinhalt.
1. Bereiten Sie die Datei `test_input.md` vor. Diese Datei enthält den Testinhalt.

```test_input.md
```test_input.md
## Zitate
## Zitate
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
Konvertieren Sie `addition_py` und `multiplication_py` in ein japanisches Pflichtenheft.
Konvertieren Sie `addition_py` und `multiplication_py` in ein japanisches Pflichtenheft.
Beschreiben Sie auch die erforderlichen Tests.
Beschreiben Sie auch die erforderlichen Tests.
```
```

2. Führen Sie den folgenden Befehl aus, um den Inhalt von `test_input.md` zu konvertieren und in `output.md` auszugeben:
2. Führen Sie den folgenden Befehl aus, um den Inhalt von `test_input.md` zu konvertieren und in `output.md` auszugeben:

   ```
   ```
   niwatoko test_input.md -o output.md
   niwatoko test_input.md -o output.md
   ```
   ```

3. Führen Sie den folgenden Befehl aus, um den Inhalt von `output.md` in Python-Code zu konvertieren und in `output.py` auszugeben:
3. Führen Sie den folgenden Befehl aus, um den Inhalt von `output.md` in Python-Code zu konvertieren und in `output.py` auszugeben:

   ```
   ```
   niwatoko output.md -o output.py
   niwatoko output.md -o output.py
   ```
   ```

4. Überprüfen Sie den Inhalt der generierten Dateien `output.md` und `output.py`, um sicherzustellen, dass die Ausgabe wie erwartet ist.
4. Überprüfen Sie den Inhalt der generierten Dateien `output.md` und `output.py`, um sicherzustellen, dass die Ausgabe wie erwartet ist.

5. Wiederholen Sie die Schritte, bis Sie die erwartete Ausgabe erhalten.
5. Wiederholen Sie die Schritte, bis Sie die erwartete Ausgabe erhalten.