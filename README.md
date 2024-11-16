# python ディレクトリ構成サンプル

## 概要

以前からpythonのモジュールimportエラーに悩まされていた。

メインのモジュールとテスト用ディレクトリをプロジェクトに配置して、動くことを確認したのでここに残す。

## 実行方法

メインモジュールの実行

```python
python -m example_tree
```

テストの実行（unittest）

```python
python -m unittest discover -s tests -p "*.py"
```
