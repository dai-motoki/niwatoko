Voici la traduction française :

# niwatoko v1.1.3

Nous avons reproduit en open source (deuxième au monde*) la fonctionnalité de variable de document d'Anthropic et fourni une fonctionnalité d'importation de module (première au monde*).

## Mises à jour

### Ajout de la fonctionnalité d'importation (citation)
- Vous pouvez désormais citer le contenu d'autres fichiers dans les fichiers Markdown.
- Cela améliore la réutilisabilité du code et facilite la gestion des documents.

- La méthode de citation est la suivante :
   ```markdown
   - `nom_variable` = extension [./chemin_fichier(sans_extension)]
   - `nom_variable` = [./chemin_fichier]
   ```
- Exemple :
   ```markdown
    `hello.py` = py [./hello]
    `hello.py` = [./hello.py]
   ```
- Cette fonctionnalité est une première mondiale.
- Notez que l'extension de fichier (.py) doit être incluse entre crochets [].

### Ajout de la fonctionnalité de variable de document
- Vous pouvez désormais définir des variables dans les fichiers Markdown et les référencer ailleurs.
- Cela améliore la lisibilité et la maintenabilité des documents.
- Cette fonctionnalité est la deuxième implémentation au monde après Anthropic.

## Installation

Pour plus de détails, veuillez consulter l'URL suivante :
[https://niwatoko2.vercel.app/installation.html](https://niwatoko2.vercel.app/installation.html)


1. Si vous avez déjà configuré Python et les clés Anthropic, vous pouvez l'utiliser avec la commande suivante :

   ```
   pip install niwatoko
   ```

   Ou pour mettre à jour vers la dernière version, exécutez :
   
   ```
   pip install --upgrade niwatoko
   ```


## Exercice

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
def add(a, b):
    """
    Fonction pour additionner deux nombres

    Paramètres :
    a (int ou float) : Premier nombre
    b (int ou float) : Deuxième nombre

    Retourne :
    int ou float : Somme de a et b
    """
    return a + b

def add_list(numbers):
    """
    Fonction pour calculer la somme d'une liste de nombres

    Paramètres :
    numbers (list) : Liste de nombres

    Retourne :
    int ou float : Somme des nombres
    """
    total = 0
    for num in numbers:
        total = add(total, num)
    return total

def add_multiple(*args):
    """
    Fonction pour additionner plusieurs nombres

    Paramètres :
    *args : Arguments de longueur variable. Accepte n'importe quel nombre de valeurs numériques

    Retourne :
    int ou float : Somme des arguments passés
    """
    return add_list(args)
```
- `multiplication_py` = py [./test_import_module_multiple]  
```py
def multiply(a, b):
    """
    Fonction pour multiplier deux nombres

    Paramètres :
    a (int ou float) : Premier nombre
    b (int ou float) : Deuxième nombre

    Retourne :
    int ou float : Produit de a et b
    """
    return a * b

def multiply_list(numbers):
    """
    Fonction pour calculer le produit d'une liste de nombres

    Paramètres :
    numbers (list) : Liste de nombres

    Retourne :
    int ou float : Produit des nombres
    """
    total = 1
    for num in numbers:
        total = multiply(total, num)
    return total


def multiply_multiple(*args):
    """
    Fonction pour multiplier plusieurs nombres

    Paramètres :
    *args : Arguments de longueur variable. Accepte n'importe quel nombre de valeurs numériques

    Retourne :
    int ou float : Produit des arguments passés
    """
    return multiply_list(args)```

## TODO
Convertissez `addition_py` et `multiplication_py` en spécifications fonctionnelles en japonais uniquement.
Décrivez également les tests nécessaires.
```

2. Exécutez la commande suivante pour convertir le contenu de `test_input.md` et le stocker dans le fichier `output.md` :

   ```
   niwatoko test_input.md -o output.md
   ```

3. Exécutez la commande suivante pour convertir le contenu de `output.md` en code Python et le stocker dans le fichier `output.py` :

   ```
   niwatoko output.md -o output.py
   ```

4. Examinez le contenu généré dans `output.md` et `output.py` pour vérifier que la sortie est conforme à vos attentes.

5. Répétez les étapes jusqu'à ce que vous obteniez la sortie souhaitée.