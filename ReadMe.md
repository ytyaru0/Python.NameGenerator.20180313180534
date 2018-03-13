# このソフトウェアについて

ファイル名を自動生成する。

現状、0〜zを返す。

# 目的

とにかくコードを書いてやってみるとき、適当なファイル名が欲しい。重複せず、順序を持った、最小の名前を、手間なく。

# 使い方

```sh
python3 NamgeGenerator.py {dir}
```
```sh
python3 NamgeGenerator.py {dir} -e {ext}
```

## 位置引数

項目|説明|例
----|----|--
`{dir}`|`/tmp/`|対象ディレクトリのフルパス

## オプション引数

略|全|意味|default|
--|--|----|-------|
-e|--extension|対象ファイルの拡張子|なし
-r|--radix|基数|`36`
-a|--alignment|桁合わせ|`False`

## 結果

名前テキストを返す。`print`する。`sh`スクリプトで取得して利用することを想定。

# 予定する機能

* 使う字
    * `[0-9]`
    * `[a-z]`
        * Windowsは大文字と小文字の区別がない
            * 数字との判別のしやすさから小文字を使う
    * 基数(10,26,36)
        * 10: 数字のみ
        * 26: 英字のみ
        * 36: 英数字
* 桁合わせ
    * ONなら`0`,`a`で埋める

# 課題

* 未実装
    * 基数、桁繰り上げ、桁合わせ
* 引数のオプション化

# 開発環境

* [Raspberry Pi](https://ja.wikipedia.org/wiki/Raspberry_Pi) 3 Model B
    * [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) GNU/Linux 8.0 (jessie)
        * bash 4.3.30

# ライセンス

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

