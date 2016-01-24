==================================================
パッケージの設定
==================================================

LaTeXエクスポートした時に、プリアンブルに挿入するパッケージの設定。
``org-latex-default-packages-alist`` には手を加えず、
``org-latex-packages-alist`` に追加する。

設定
==================================================

.. code-block:: emacs

   ;; しおりの文字化け対策
   (add-to-list 'org-latex-packages-alist '("" "pxjahyper") t)
   ;; (add-to-list 'org-latex-packages-alist '("" "atbegshi") t)
   ;; (add-to-list 'org-latex-packages-alist "\\AtBeginShipoutFirst{\\special{pdf:tounicode EUC-UCS2}}" t)

   ;; hyperrefの設定
   (add-to-list 'org-latex-packages-alist "\\hypersetup{setpagesize=false}" t)
   (add-to-list 'org-latex-packages-alist "\\hypersetup{colorlinks=true}" t)
   (add-to-list 'org-latex-packages-alist "\\hypersetup{linkcolor=blue}" t)

   ;; その他のパッケージの追加
   (add-to-list 'org-latex-packages-alist '("" "listings") t)
   (add-to-list 'org-latex-packages-alist '("" "color") t)
   (add-to-list 'org-latex-packages-alist '("" "fancyvrb") t)

   ;; 文字ハイライトに minted を使う（pdflatexじゃないと動かない）
   ;;(add-to-list 'org-latex-packages-alist '("" "minted"))
   (setq org-latex-listings t)



これも、 ``alist`` になっているので ``add-to-list`` を使って追加する。
しおりの文字化け対策として ``pxjahyper`` パッケージと
``hyperref`` の設定（ ``hypersetup`` ）を追加した。

``add-to-list`` の第２引数にパッケージかコマンドを指定する。
``hypersetup`` などの先頭につけるバックスラッシュはエスケープする。
第３引数を ``t`` にすることで、書いた順番通りにLaTeXプリアンブルに出力される。

使うパッケージは、すべてのファイルに共通なパッケージにする。
その際、すでに設定されている ``org-format-latex-header`` や
``org-latex-default-packages-alist`` のパッケージとコンフリクトしないこと。
``hyperref`` はすでにインクルードされてるので ``hypersetup`` で指定する必要がある。
また、ファイル内の ``#+LATEX_HEADER:`` で個々の設定もできる。

.. code-block:: emacs

   ;; usepackage型
   (add-to-list 'org-latex-packages-alist '("オプション" "パッケージ名") t)

   ;; maketitle型
   (add-to-list 'org-latex-packages-alist "\\コマンド名{オプション}" t)



hyperref の設定
~~~~~~~~~~~~~~~

.. code-block:: latex

   \usepackage{hyperref}
   \hypersetup{
       setpagesize=false,    %% <-- This line is very important
       pdfkeywords={},
       pdfsubject={},
       pdfcreator={Emacs 24.4.1 (Org mode 8.2.10)}}



``hyperref`` パッケージと ``jsarticle`` は仲が良くないので、
そのままコンパイルするとページの幅がおかしくなってしまう。
これは オプションで ``setpagesize=false`` とすることで解決する。

しかし、デフォルトの ``hyperref`` オプションは、
``ox-latex.el`` にハードコーディングされていて追加／変更できないので ``org-latex-packages-alist`` や ``#+latex_headers:`` ／ ``#+latex_header_extra:``  などを複数回使って、１つずつ呼び出すことにする。



.. code-block:: latex

   \\usepackage{hyperref}
   \\hypersetup{pdfkeywords={},
                pdfsubject={},
                pdfcreator={Emacs 24.4.1 (Org mode8.2.10)}}
   \\hypersetup{ setpagesize=false }


とりあえずテストしたい場合は、編集しているOrgファイルの先頭に
``#+latex_header:`` もしくは ``#+latex_header_extra:`` を
使って定義するとよい。

``latex_header`` と ``latex_header_extra`` の違いを調べるために、
以下の順番で ``hypersetup`` を定義してみた。

.. code-block:: latex

    #+latex_header: \hyperref{setpagesize=false}
    #+latex_header_extra: \hyperref{colorlinks=true}
    #+latex_header: \hyperref{linkcolor=blue}


すると、 ``latex_header`` > ``latex_header_extra``
の順に書かれることが分かった。
いまいちどういう時に順番を考えたらいいのか思いつかないけれど。

.. code-block:: latex

    \usepackage{hyperref}
    \hypersetup{setpagesize=false}    %% latex_header:
    \hypersetup{linkcolor=blue}       %% latex_header:
    \hypersetup{colorlinks=true}      %% latex_header_extra:
    \tolerance=1000
    \author{Shota}
    \date{\today}
    \title{\LaTeX{} Export Test}
    \hypersetup{pdfkeywords={},
                pdfsubject={},
                pdfcreator={Emacs 24.4.1 (Org mode 8.2.10)}}


出力場所は、デフォルト出力の ``hypersetup`` の上になるが、
コンパイルには影響しないのでこれで良しとする。
