## 引用

- `翻訳対象言語集` = [./multilang.md]
- `日本語ファイル` = [./README_ja.md]

## 

```py
import os
`翻訳対象言語`から`対象言語`と`対処言語二文字表現`を1つずつ取り出す。

    以下ファイルを作成
    ```translation_{`対処言語二文字表現`}.md
    `日本語ファイル`を`対象言語`に1行1行翻訳してください。
    ```

    以下コマンドを実行 os subprocess利用
    ```
    niwatoko translation.md -o README_{`対処言語二文字表現`}.md
    ```

`翻訳対象言語`を網羅するまでやる
```