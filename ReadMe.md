# このソフトウェアについて

ファイル名を自動生成する。

# 目的

とにかくコードを書いてやってみるとき、適当なファイル名が欲しい。重複せず、順序を持った、最小の名前を、手間なく。

# 使い方

```sh
python3 NamgeGenerator.py {dir}
```
```sh
python3 NamgeGenerator.py {dir} -e {ext}
```
```sh
python3 NamgeGenerator.py {dir} -e {ext} -r {rad}
```
```sh
python3 NamgeGenerator.py {dir} -e {ext} -r {rad} -a
```

## 位置引数

i|略|意味
-|--|----
0|{dir}|対象ディレクトリのフルパス

指定したディレクトリにあるファイルやディレクトリの数によって名前を生成する。

## オプション引数

略|全|意味|default|
--|--|----|-------|
-e|--extension|対象ファイルの拡張子|なし
-r|--radix|基数|`10`
-a|--alignment|桁合わせ|`False`

alignmentはファイル名の桁を合わせる。`0.sh`〜`9.sh`まであるとき、`10.sh`の名前が生成されたら、`0.sh`たちは`00.sh`になる。

## 値

項目|説明|例
----|----|--
`{dir}`|`/tmp/`|対象ディレクトリのフルパス
`{ext}`|`py`|対象ファイルの拡張子。ない場合はディレクトリを対象とする。
`{rad}`|`10`|基数。2,8,10,16,26,32,36,64,85。

## 結果

名前テキストを返す。`print`する。`sh`スクリプトで取得して利用することを想定。

# 使う字

基数|文字
----|----
2,8,10|数字のみ
26|英字のみ
32,36|英数字
64|英数字(小文字,大文字) + `_-`
85|英数字(小文字,大文字) + Win,Mac,Linuxでパスに使える記号

* 英字は小文字を使う（数字との判別のしやすさ）
* *Windowsは*大文字と小文字の区別がない
    * 64以上の基数を使うと*重複してしまう*

# 開発環境

* [Raspberry Pi](https://ja.wikipedia.org/wiki/Raspberry_Pi) 3 Model B
    * [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) GNU/Linux 8.0 (jessie)
        * [pyenv](http://ytyaru.hatenablog.com/entry/2019/01/06/000000)
            * Python 3.6.4

# ライセンス

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

