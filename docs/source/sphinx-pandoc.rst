==================================================
pandocコマンドの使い方
==================================================

**A General Markup Converter** です。
``Markdown`` などのあるマークアップから、別のマークアップへ変換するコマンドです。

``Org`` や ``Markdown`` をすでに使っている場合、
新しく ``reST`` を覚えるのは、やはりめんどうです。
そのような場合 :command:`pandoc` コマンドがあれば、以下のようなワークフローを考えることができます。

#. Orgモードで文章を作成（ただし ``QuickLook`` できるように ``.txt形式`` で保存）
#. ``pandoc`` を使って ``reST形式`` に変換
#. ``Sphinx`` を使って HTML と PDFに変換

.. note::

   僕は最初、上記手順でやろうと思っていました。
   しかし、複数のマシンを使う場合、環境の構築に手間がかかったり
   （主に当初の公開サーバにpandocがインストールできなかった）、
   毎回変換させるのがやっぱりめんどくさかったり（ワンライナー書けばいい話だけども）、
   結局 ``reST`` を覚えることにしました。

   感想としては、Sphinxは元の ``reST`` を拡張した機能（ディレクティブ）もあるためか、
   ``Markdown`` よりも細かくドキュメントをマークアップできる気がして僕は好きです。
   Emacsの ``yasnippet`` パッケージとうまく組み合わせれば、
   マークアップの違いをそんなに気にせずに使うことができると思います。








Org から reST への変換
==================================================

``Org`` には ``reST`` エクスポート（ ``ox-rst`` ）があるのですが、なぜかうまく働かないので :command:`pandoc` を使って変換します。
今回の場合、Org文書の拡張子が ``.txt`` なので ``-f org`` を使って :command:`pandoc` に入力フォーマットを教えています。
出力ファイルは拡張子で reST形式（ ``-o FILENAME.rst`` ）と分かるので、
出力フォーマットを指定する必要はありません。

.. code-block:: bash

    $ cd $KUMAROOT
    $ pandoc -f org source/FILENAME.txt -o source/FILENAME.rst

毎回、手動で変換するのが面倒くさいのでワンライナーを書いてみました。
これを ``Makefile`` に書いておけばいいのかもしれないです。

.. code-block:: bash

    $ for f in source/*.txt; do pandoc -f org -t rst $f -o "source/`basename $f .txt`.rst"; done


HTML から reST への変換
==================================================

``pandoc`` は ``reST`` を ``doc/docx`` （Word形式）に変換できるのですが、逆はできないようです。
Word形式を ``reST`` にできたら便利かなと思うのですが、
``HTML`` を経由する方法を紹介します。


#. Word上でファイルをHTMLとして書き出す
#. ``pandoc`` を使って HTMLをreSTに変換する

この場合は、入力フォーマットも出力フォーマットも、ファイル形式を見れば分かるので、
オプションは必要ありません。

.. code-block:: bash

    $ cd $KUMAROOT
    $ pandoc source/FILENAME.html -o source/FILENAME.rst
