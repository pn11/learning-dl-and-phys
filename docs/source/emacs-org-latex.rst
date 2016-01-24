==================================================
LaTeX連携
==================================================


Org文書を LaTeX 文書に変換する方法です。
YaTeXと組み合わせると更に捗ります。その時のワークフローは以下のよう。

#. Orgファイルの編集（ ``emacs kumaroot.org`` ）
#. LaTeXエクスポート（ ``C-c C-e l l`` ）
#. LaTeXファイルのバッファを開く（ ``C-x b kumaroot.tex`` ）
#. YaTeXコマンドでコンパイル（ ``C-c C-t j`` ）
#. YaTeXコマンドでプレビュー（ ``C-c C-t p`` ）


必要なパッケージは :file:`ox-latex.el` というファイルです。
最近（2014年頃） :file:`org-latex` から :file:`ox-latex` に変更されたようです。
ググッて :file:`org-latex` を ``require`` してたら、その内容は古い可能性があります。
パッケージ管理ツールでインストールしていれば、
``autoload`` されてるはずなので ``(require 'ox-latex)`` は特に要らないはず。


設定
==================================================

.. code-block:: emacs

   (use-package ox-latex
     :config
     (setq org-latex-default-class "jsarticle")
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

     ;; hyperrefのしおりの文字化け対策
     (add-to-list 'org-latex-packages-alist '("" "pxjahyper") t)
     ;; (add-to-list 'org-latex-packages-alist '("" "atbegshi") t)
     ;; (add-to-list 'org-latex-packages-alist "\\AtBeginShipoutFirst{\\special{pdf:tounicode EUC-UCS2}}" t)

     ;; hyperrefの設定
     (add-to-list 'org-latex-packages-alist "\\hypersetup{setpagesize=false}" t)
     (add-to-list 'org-latex-packages-alist "\\hypersetup{colorlinks=true}" t)
     (add-to-list 'org-latex-packages-alist "\\hypersetup{linkcolor=blue}" t)

     (add-to-list 'org-latex-packages-alist '("" "listings") t)
     (add-to-list 'org-latex-packages-alist '("" "color") t)
     (add-to-list 'org-latex-packages-alist '("" "fancyvrb") t)

     ;;(add-to-list 'org-latex-packages-alist '("" "minted")) ;; gives an error while compilling
     (setq org-latex-listings t)

     (setq org-use-sub-superscripts nil)
     (setq org-export-with-sub-superscripts nil)

     ;; (setq org-latex-pdf-process
     ;;       ("ptex2pdf -l -ot -synctex=1 -file-line-error")

     ;;       )
     ;; (setq org-export-latex-coding-system "utf8")
     ;; (setq org-export-latex-date-format "%Y-%m-%d")
     ;; (setq org-file-apps '(("pdf" . "/usr/bin/open -a Preview.app %s")))

     )



設定の詳細
==================================================


.. toctree::
   :maxdepth: 1

   emacs-org-latex-class
   emacs-org-latex-packages





上文字、下文字の自動変換をオフにする
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: emacs

   (setq org-use-sub-superscripts nil)
   (setq org-export-with-sub-superscripts nil)


Orgファイル中の ``^（ハット）`` ``_（アンダースコア）`` 以降の
英数字は自動的に上文字、下文字に変換されてしまいます。
便利なのかもしれませんが、意図しない箇所も変換されてしまうのはやっぱり不便なのでオフにします。
エクスポートするときも同じ理由でオフにしておきます。

上付き・下付きにしたい場合は、
``文字^{上付き}`` 、 ``文字_{下付き}`` のように ``中括弧 {}`` で囲みます。
Orgファイル中で ``C-c C-x \`` すればプレビューできます。
