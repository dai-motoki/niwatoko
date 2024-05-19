Voici la traduction en français :

# niwatoko v1.1.4
# niwatoko v1.1.4

Le langage de programmation Niwatoko a commencé à fournir une fonctionnalité d'importation de modules (première mondiale*).
Le langage de programmation Niwatoko a commencé à fournir une fonctionnalité d'importation de modules (première mondiale*).
Le générateur de prompts d'Anthropic peut désormais traiter les fichiers Markdown avec des variables.
Le générateur de prompts d'Anthropic peut désormais traiter les fichiers Markdown avec des variables.

## Mises à jour

### Ajout de la fonctionnalité d'importation (citation)
- Il est maintenant possible de citer le contenu d'autres fichiers dans un fichier Markdown.
- Cela améliore la réutilisabilité du code et facilite la gestion des documents.

- La méthode de citation est la suivante :
   ```markdown
   - `variable_name` = extension [./chemin_fichier(sans_extension)]
   - `variable_name` = [./chemin_fichier]
   ```
- Exemple :
   ```markdown
    `hello.py` = py [./hello]
    `hello.py` = [./hello.py]
   ```
- Cette fonctionnalité est une première mondiale.
- Notez que l'extension de fichier (.py) doit être incluse dans les crochets [].

### Ajout de la fonctionnalité de variables de document
- Il est maintenant possible de définir des variables {{variable}} dans un fichier Markdown et de les référencer ailleurs.
  - Par exemple, `{{variable_name}}` chargera le fichier `variable_name.md` du même niveau.
- Cela améliore la lisibilité et la maintenabilité des documents.

## Installation

Veuillez consulter le lien suivant pour plus de détails :
[https://niwatoko2.vercel.app/installation.html]

1. Pour les utilisateurs ayant déjà configuré Python et les clés Anthropic, vous pouvez utiliser la commande suivante :

   ```
   pip install niwatoko
   ```

   Ou pour mettre à jour vers la dernière version :

   ```
   pip install --upgrade niwatoko
   ```

## Exercices pratiques

Suivez les étapes ci-dessous :

- Préparation
1. Clonez la branche principale de ce référentiel.

   ```
   git clone -b main https://github.com/dai-motoki/niwatoko.git
   ```
2. Accédez au répertoire cloné.

   ```
   cd niwatoko/tests/test_docs/test_niwatoko_v1.1.3
   ```

- Exécution
1. Préparez le fichier `test_input.md`. Ce fichier contient le contenu d'entrée à tester.

```test_input.md
## Citation
- `addition_py` = py [./test_import_module_add]
```py
```
- `multiplication_py` = py [./test_import_module_multiple]  
```py
```

## TODO
`addition_py` et `multiplication_py` doivent être convertis en spécifications fonctionnelles en japonais uniquement.
Décrivez également les tests nécessaires.
```

2. Exécutez la commande suivante pour convertir le contenu de `test_input.md` et générer `output.md` :

   ```
   niwatoko test_input.md -o output.md
   ```

3. Exécutez la commande suivante pour convertir le contenu de `output.md` en code Python et générer `output.py` :

   ```
   niwatoko output.md -o output.py
   ```

4. Vérifiez le contenu des fichiers `output.md` et `output.py` générés pour vous assurer que la sortie est conforme à vos attentes.

5. Répétez les étapes jusqu'à ce que vous obteniez la sortie souhaitée.