==================================================
Sphinxの使い方
==================================================

**Sphinx** は ``reStructredText（reST）`` 形式で作成されたテキスト文書を、
PDFやHTML、その他のフォーマットへと変換する
**ドキュメンテーションビルダー** というツールです。

この くまROOT も Sphinx を使って作成しています。
くまROOTは Gitでバージョン管理していて、
`GitHub <github_>`_ で公開しています。
HTML版は `Read the Docs <rtd_>`_ で公開しています。
どんなものか気になる方は `KumaROOT <github_>`_ リポジトリをクローンしてみるといいかもしれません。

また、Sphinx自体が元々Pythonのドキュメント生成のために開発されたものなので、
プロジェクトのドキュメント作成にはもってこいです。
いま使っているソフトウェアのドキュメント作成は、
ついつい後回し／ほったらかしにしがち（そして後で自分が困る）ですが、
Sphinxを導入しておけば書くのも、HTML／PDFなどでの共有も楽ちんになるのではないかと思います。
中身はPythonで書かれているので、へびつかいであれば、ある程度カスタマイズすることもできるはずです。

.. _github: https://github.com/shotakaha/kumaroot
.. _rtd: http://kumaroot.readthedocs.org/ja/latest/

.. toctree::
   :maxdepth: 1

   sphinx-install
   sphinx-quickstart
   sphinx-build
   sphinx-conf
   sphinx-readthedocs
   sphinx-pandoc
