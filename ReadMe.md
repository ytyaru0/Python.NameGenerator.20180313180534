# このソフトウェアについて

ファイル名を自動生成する。

# 目的

とにかくコードを書いてやってみるとき、適当なファイル名が欲しい。重複せず、順序を持った、最小の名前を、手間なく。

# 使い方

```sh
python3 NamgeGenerator.py 対象ディレクトリのフルパス
```

# 結果

テキストを返す。`echo`する。`sh`スクリプトで取得して利用する。

# 機能

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

# 開発環境

* [Raspberry Pi](https://ja.wikipedia.org/wiki/Raspberry_Pi) 3 Model B
    * [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) GNU/Linux 8.0 (jessie)
        * bash 4.3.30

# ライセンス

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

