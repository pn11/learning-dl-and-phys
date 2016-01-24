============================================================
ドキュメントクラスオプションの設定
============================================================

ドキュメントクラスのオプションを設定する部分です。

プリアンブルの設定は、ここで書くと長くなって読みにくくなるため、
ここでは変数の定義だけしておいて、後で設定します。
設定方法は後述してあります（ :doc:`sphinx-latex-preambles` を参照 ）。

.. code-block:: python

    latex_elements = {
        'papersize' = 'a4paper',
        'pointsize' = '12pt',
        'preamble': '',    # あとで追加するので定義だけしておく
        'figure_align': 'htbp',
    #   'fontpkg': '\\usepackage{times}',
    }


LaTeX文書の出力は以下のようになります。

.. code-block:: latex

   \documentclass[a4paper, 12pt, dvipdfmx]{sphinxmanual}
