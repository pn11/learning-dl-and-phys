==================================================
YASnippet
==================================================

コードを書いていると定型文的なことを何回も書くことがあります。
このような定型文のことを **スニペット** と呼ぶらしいですが、
これらを簡単に作成・挿入できるようにしたのが **YASnippet** です。



設定
==================================================

.. code-block:: emacs

   (use-package yasnippet
     :ensure t
     :diminish yas-minor-mode
     :bind (:map yas-minor-mode-map
                ("C-x i i" . yas-insert-snippet)
                ("C-x i n" . yas-new-snippet)
                ("C-x i v" . yas-visit-snippet-file)
                ("C-x i l" . yas-describe-tables)
                ("C-x i g" . yas-reload-all)
                )
     :config
     (yas-global-mode 1)
     (setq yas-prompt-functions '(yas-ido-prompt))
   )


使い方
==================================================

:kbd:`C-x i` はデフォルトでファイル挿入（:kbd:`M-x insert-file` ）コマンドに割り当てられていますが、あまり使う機会がなく、
また、スニペットの挿入はファイル挿入と似た感覚の機能なので、
コマンドを上書きすることにしました。
ファイル挿入したい場合は、直接 :kbd:`M-x insert-file` すればよいので。

#. スニペットの保存先 :file:`~/.emacs.d/snippets/` を作成しておく
#. :kbd:`(yas-global-mode 1)` して常に（マイナーモードとして）使えるようにする
#. スニペットのキーワードを入力して :kbd:`TAB` を押す、もしくは :kbd:`C-x i i` から選択することでスニペットを挿入
#. :kbd:`C-x i l` で現在のメジャーモードで使えるスニペットのキーワード一覧を確認できる
#. 既存のスニペットを編集したい場合は :kbd:`C-x i v` する
#. 新規にスニペットを作成したい場合は :kbd:`C-x i n` する
