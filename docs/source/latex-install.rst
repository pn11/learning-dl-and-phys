==================================================
インストール
==================================================


つい最近までは「Mac LaTeX インストール」などでググると、なんだかまとまりのない情報で溢れていました。
しかし、現在はそれらを取りまとめようということで開発が進んでいるようで、これからはTeXLive一択で良いみたいです。
TeXLiveは年１回更新されます。


MacTeX
==================================================

MacOSXでLaTeXを使う場合は、MacTeXで決まりです。
`MacTeX <https://tug.org/mactex/>`__ からダウンロードできます。

TeX環境の本体であるTeXLiveと一緒に、TeX編集の統合環境であるTeXShopやTeXworks、
TeX関連のパッケージ管理ツールであるTeX Live Utilityがついてきます。
他にも、文献管理のBibDesk、スペルチェックのExcalibur、そして、
Keynoteに数式を貼り付けるのに必要なLaTeXiTがついてきます。


MacPorts (TeXLive)
==================================================

TeXLiveはMacPortsからインストールすることもできます。
特に理由がなければ ``texlive +full`` をインストールすればいいと思います。

ただし、LaTeXiTなどはついてきません。
（そして、MacPortsにあるLaTeXiTはバージョンが古いため使えません）

.. code-block:: bash

   $ sudo port install texlive +full


Homebrew (MacTeX)
==================================================

HomebrewでTeXLiveパッケージを探すと、Homebrew-Caskを使ってMacTeXをインストールすることを勧められます。
上記 MacTeX のウェブページからバイナリをインストールするのと同じものが入ります。

.. code-block:: bash

   $ brew cask install mactex
