==================================================
パッケージ管理システムの設定
==================================================

Emacs24からパッケージ管理システムがデフォルトで使えるようになりました。
とても便利なので、この設定は必ずしておきましょう。

デフォルトでは ``ELPA`` リポジトリのみが設定されていますが、
パッケージ登録数が少ないらしいので、
``MELPA`` リポジトリも追加しておきましょう。

リポジトリは他にも ``Marmalade`` というのがあります。

.. code-block:: elisp

   (require 'package)
   (add-to-list 'package-archives
                '("melpa" . "http://melpa.org/packages/") t)
   (package-initialize)


前述した Prelude では :file:`~/emacs.d/core/prelud-pacages.el` で設定済みです。
