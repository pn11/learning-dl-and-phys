==================================================
ドキュメントのビルド
==================================================

例として、この文書（ ``KumaROOT`` ）をGitHubからクローンして、ビルドする方法です。

.. code-block:: bash

   $ git clone https://github.com/shotakaha/kumaroot.git
   $ cd kumaroot/docs
   $ make html        ## HTMLの生成
   $ make latexpdfja  ## PDFの生成

.. note::

   HTMLのビルドは問題なくできると思いますが、
   PDFのビルドはLaTeX環境が整ってないとエラーがでると思います。



HTML文書のビルド
==================================================

HTML変換には ``make html`` を実行します。
変換ファイルは ``build/html/`` 以下に作成されます。

.. code-block:: bash

    $ cd kumaroot/docs
    $ make html
    $ open build/html/index.html



PDF文書のビルド
==================================================

日本語を含む文書のPDF変換には ``make latexpdfja`` を実行します。
これは裏で ``platex / dvipdfmx`` を実行しているため、日本語もきちんと処理できます。
変換ファイルは ``build/latex/`` 以下に作成されます。

.. code-block:: bash

    $ cd $kumaroot/docs
    $ make latexpdfja
    $ open build/latex/KumaROOT.pdf
