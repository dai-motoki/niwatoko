要件定義書

### 機能概要

本機能は、数値の足し算を行う機能を提供する。

### 機能詳細

#### 1. 2つの数値の足し算

* **機能名:** add
* **入力:** 
    * a (int or float): 1つ目の数値
    * b (int or float): 2つ目の数値
* **出力:** 
    * int or float: aとbの和
* **処理内容:** aとbの値を足し合わせる。
* **テストケース:**
    * a = 1, b = 2, 出力 = 3
    * a = -1, b = 1, 出力 = 0
    * a = 1.5, b = 2.5, 出力 = 4.0

#### 2. 数値のリストの合計計算

* **機能名:** add_list
* **入力:** 
    * numbers (list): 数値のリスト
* **出力:** 
    * int or float: numbersの合計値
* **処理内容:** リスト内の数値を順次足し合わせる。
* **テストケース:**
    * numbers = [1, 2, 3], 出力 = 6
    * numbers = [-1, 1, 2], 出力 = 2
    * numbers = [1.5, 2.5, 3.0], 出力 = 7.0

#### 3. 複数の数値の足し算

* **機能名:** add_multiple
* **入力:** 
    * *args: 可変長引数。任意の数の数値を受け取る
* **出力:** 
    * int or float: 引数として渡された数値の合計
* **処理内容:** 可変長引数として渡された数値を全て足し合わせる。
* **テストケース:**
    * args = (1, 2, 3), 出力 = 6
    * args = (-1, 1, 2), 出力 = 2
    * args = (1.5, 2.5, 3.0), 出力 = 7.0


## 掛け算py 要件定義書

### 機能概要

本機能は、数値の掛け算を行う機能を提供する。

### 機能詳細

#### 1. 2つの数値の掛け算

* **機能名:** multiply
* **入力:** 
    * a (int or float): 1つ目の数値
    * b (int or float): 2つ目の数値
* **出力:** 
    * int or float: aとbの積
* **処理内容:** aとbの値を掛け合わせる。
* **テストケース:**
    * a = 2, b = 3, 出力 = 6
    * a = -2, b = 3, 出力 = -6
    * a = 1.5, b = 2.0, 出力 = 3.0

#### 2. 数値のリストの積計算

* **機能名:** multiply_list
* **入力:** 
    * numbers (list): 数値のリスト
* **出力:** 
    * int or float: numbersの積
* **処理内容:** リスト内の数値を順次掛け合わせる。
* **テストケース:**
    * numbers = [2, 3, 4], 出力 = 24
    * numbers = [-2, 3, 4], 出力 = -24
    * numbers = [1.5, 2.0, 3.0], 出力 = 9.0

#### 3. 複数の数値の掛け算

* **機能名:** multiply_multiple
* **入力:** 
    * *args: 可変長引数。任意の数の数値を受け取る
* **出力:** 
    * int or float: 引数として渡された数値の積
* **処理内容:** 可変長引数として渡された数値を全て掛け合わせる。
* **テストケース:**
    * args = (2, 3, 4), 出力 = 24
    * args = (-2, 3, 4), 出力 = -24
    * args = (1.5, 2.0, 3.0), 出力 = 9.0


## テストに関する追加情報

上記に記載したテストケースに加えて、以下のテストも実施する。

* **境界値テスト:** 入力値の境界値 (最小値、最大値、ゼロなど) を使用して、機能が正しく動作することを確認する。
* **異常値テスト:** 無効な入力値 (文字列、リストなど) を使用して、機能が適切にエラー処理を行うことを確認する。
* **パフォーマンステスト:** 大量のデータや複雑な計算を用いて、機能の性能を評価する