## Quotes

- `languages_to_translate` = [./multilang.md]
- `japanese_file` = [./README_ja.md]

## 

```py
From `languages_to_translate`, take one `target_language` and one `target_language_code`.

    Create the following file:
    ```translation_{`target_language_code`}.md
    Translate `japanese_file` line by line into `target_language`.
    ```

    Run the following command using os subprocess:
    ```
    niwatoko translation.md -o README_{`target_language_code`}.md
    ```

Repeat until all `languages_to_translate` are covered.
```
