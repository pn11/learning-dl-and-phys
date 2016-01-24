==================================================
ドキュメントクラスの設定
==================================================

LaTeX エクスポートで使うドキュメントクラスの設定です。

まず使いたいドキュメントクラスを ``org-latex-classes`` に追加します。
デフォルト値は :file:`jsarticle` にておきます。
Orgファイルのヘッダで ``#+LATEX_CLASS: jsarticle`` （大文字／小文字の区別なし）と書くことで、
ファイル毎に変更することができます。


デフォルト値の設定
==================================================

日本語を使う ``jsarticle`` にします。
後述する ``org-latex-classes`` に追加しておく必要があります。
デフォルト値は :kbd:`M-x describe-variable org-latex-default-class` で確認できます。

.. code-block:: emacs

   (setq org-latex-default-class "jsarticle")



スタイルの追加
==================================================

``org-latex-classes`` は ``alist`` なので、``add-to-list`` を使って追加できます。
デフォルト値は :kbd:`M-x describe-variable org-latex-classes` で確認できます。


jsarticle
--------------------------------------------------

日本語レポートのデフォルトスタイルです。
``article`` と比べると余白が狭くなっていたりと、
日本語ドキュメントに合ったようになってます。

.. code-block:: emacs

   (add-to-list 'org-latex-classes
                '("jsarticle"
                  "\\documentclass[dvipdfmx,12pt]{jsarticle}"
                  ("\\section{%s}" . "\\section*{%s}")
                  ("\\subsection{%s}" . "\\subsection*{%s}")
                  ("\\subsubsection{%s}" . "\\subsubsection*{%s}")
                  ("\\paragraph{%s}" . "\\paragraph*{%s}")
                  ("\\subparagraph{%s}" . "\\subparagraph*{%s}")
                )
   )


jsreport
--------------------------------------------------

英語用には ``report`` があるのですが、
それに対応する日本語スタイル（仮に ``jsreport`` ）はありません。
``jsbook`` をベースに自分で定義します。

.. code-block:: emacs

   (add-to-list 'org-latex-classes
                '("jsreport"
                  "\\documentclass[dvipdfmx,12pt,report]{jsbook}"
                  ("\\chapter{%s}" . "\\chapter*{%s}")
                  ("\\section{%s}" . "\\section*{%s}")
                  ("\\subsection{%s}" . "\\subsection*{%s}")
                  ("\\subsubsection{%s}" . "\\subsubsection*{%s}")
                  ("\\paragraph{%s}" . "\\paragraph*{%s}")
                )
   )

jsbook
--------------------------------------------------

英語用 ``book`` に対応する日本語スタイルです。

.. code-block:: emacs

   (add-to-list 'org-latex-classes
                '("jsbook"
                  "\\documentclass[dvipdfmx,12pt]{jsbook}"
                  ("\\part{%s}" . "\\part*{%s}")
                  ("\\chapter{%s}" . "\\chapter*{%s}")
                  ("\\section{%s}" . "\\section*{%s}")
                  ("\\subsection{%s}" . "\\subsection*{%s}")
                  ("\\subsubsection{%s}" . "\\subsubsection*{%s}")
                )
   )


bxjsarticle
--------------------------------------------------

pdfLaTeXで使える日本語スタイルです。

.. code-block:: emacs

   (add-to-list 'org-latex-classes
                '("bxjsarticle"
                  "\\documentclass[pdflatex,jadriver=standard,12pt]{bxjsarticle}"
                  ("\\section{%s}" . "\\section*{%s}")
                  ("\\subsection{%s}" . "\\subsection*{%s}")
                  ("\\subsubsection{%s}" . "\\subsubsection*{%s}")
                  ("\\paragraph{%s}" . "\\paragraph*{%s}")
                  ("\\subparagraph{%s}" . "\\subparagraph*{%s}")
                )
   )


beamer
--------------------------------------------------

プレゼンテーション用のスタイルです。

.. code-block:: emacs

   (add-to-list 'org-latex-classes
                '("beamer"
                  "\\documentclass[dvipdfmx,12pt]{beamer}"
                  ("\\section{%s}" . "\\section*{%s}")
                  ("\\subsection{%s}" . "\\subsection*{%s}")
                  ("\\subsubsection{%s}" . "\\subsubsection*{%s}")
                  ("\\paragraph{%s}" . "\\paragraph*{%s}")
                  ("\\subparagraph{%s}" . "\\subparagraph*{%s}")
                )
   )
