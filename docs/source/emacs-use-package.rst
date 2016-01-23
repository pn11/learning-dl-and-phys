==================================================
use-package
==================================================

パッケージ設定を強化するパッケージです。
パッケージ管理ツールと連携した自動インストールを楽にしたり、
キーバインドや各種設定ができるようになっています。

例えば、パッケージがインストールされてない場合にロードしないようにする設定は、
これまで自分で書かなければいけなかかったのが、不要になったり、
ロードするタイミングを簡単に指定できるようになってます。


設定
==================================================

`use-package <github_>`_ の使い方の一番下に書いてある通りに設定しておきます。

.. code-block:: elisp

   (eval-when-compile (require 'use-package))
   (require 'diminish)    ;; if you use :diminish
   (require 'bind-key)    ;; if you use any :bind variant
   (setq use-package-verbose t)
   (setq use-package-minimum-reported-time 0.001)


使い方
==================================================

後述する YaTeX の設定内容を載せておきます。
``(use-package ...)`` と書けるので、パッケージ単位の設定がより見やすく・分かりやすくなります。

.. code-block:: elisp

   (use-package yatex
     :ensure t
     :mode (("\\.tex$" . yatex-mode))
     :bind(("C-c C-t" . YaTeX-typeset-menu))
     :config
     (setq YaTeX-inhibit-prefix-letter t)
     (setq YaTeX-nervous nil)
     (setq tex-command "ptex2pdf -l -ot -synctex=1 -file-line-error")
     (setq bibtex-command "pbibtex")
     (setq dvi2-command "open -a Preview")
     (setq tex-pdfview-command "open -a Preview")
     (setq dviprint-command-format "dvipdfmx %s")
     (setq YaTeX-skip-default-reader t)
     (setq YaTeX-simple-messages t)
   )

とりあえず今の設定をそのまま移行したい場合、

#. ``(require \`yatex)`` を ``(use-package yatex`` と書き直す（クォートが取れることに注意）
#. 以降の設定を ``:config`` 以下に移動する
#. 最後の括弧 ``)`` で閉じる

をすれば大丈夫です。

より詳細な使い方や、
``:ensure``, ``:mode``, ``:bind`` などのキーワードに関しては、
下に挙げたウェブサイトを見たほうがとよいと思います。
ただ、日本語のブログは内容が古くなっているので、概要把握にとどめ、
詳細な設定項目は本家サイトで確認するのがよいでしょう。


- `use-package - GitHub <github_>`_
- `use-packageで可読性の高いinit.elを書く - Qiita <qiita_>`_
- `use-package - るびきち日刊Emacs <rubikitch_>`_

.. _github: https://github.com/jwiegley/use-package
.. _qiita: http://qiita.com/kai2nenobu/items/5dfae3767514584f5220
.. _rubikitch: http://rubikitch.com/2014/09/09/use-package/
