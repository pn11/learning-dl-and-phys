==================================================
Org-mode
==================================================

Emacs標準の「アウトラインモード」です。
ただし、それ以上のことがたくさんできるので、
詳しくは :kbd:`M-x org-info` でドキュメントを参照してください。


設定
==================================================


.. code-block:: emacs

   (use-package org
     :ensure t
     :mode (("\\.txt$" . org-mode))
     :bind (("C-c c" . org-capture)
            ("C-c l" . org-store-link)
            ("C-c a" . org-agenda)
            ("C-c b" . org-iswitchb)
           )
     :init
     (setq my-org-directory "~/Documents/org/")
     (setq my-org-agenda-directory "~/Documents/org/agenda/")
     (setq my-org-gcal-directory "~/Documents/org/gcal/")
     (setq my-org-default-notes-file "captured.org")
     :config
     (setq org-directory my-org-directory)
     (setq org-default-notes-file my-org-default-notes-file)
     (setq org-agenda-files (list my-org-directory
                                  my-org-agenda-directory
                                  my-org-gcal-directory))

     ;; 基本設定
     ;; #+startup: hidestars / showstars
     (setq org-hide-leading-stars t)
     ;; RET will follow the link : nil --> t
     (setq org-return-follows-link t)
     (setq org-use-speed-commands t)

     ;; org-capture
     (setq org-capture-templates
         `(("a" "あっと思ったことを さっとφ(..)メモする" entry
           (file+headline nil "MEMO")
           "* %U%?\n\n%a\n%F\n"
           :empty-lines 1)

           ...（略）...

           ("m" "みんなで会議" entry
           (file+datetree "~/Documents/org/minutes.org")
           "* %? %T"
           :empty-lines 1
           :jump-to-captured 1)

           ...（略）...

           ("t" "とりあえず 仕事を放り込む" entry
           (file+headline "~/Documents/org/gtd.org" "GTD")
           "** TODO %?\n   SCHEDULED: %T\n   Entered on %U    %i\n"
           :prepend 1
           :empty-lines 1
           :unnarrowed 1)
          )
        )

     ;; org-agenda の設定
     ;; 標準の祝日を利用しない
     (setq calendar-holidays nil)

     ;; TODO状態の設定
     ;; ! をつけることで、その状態へ変更した日時を記録することが可能
     ;; @ をつけることで、その状態へ変更した時にメモを残すことが可能
     (setq org-todo-keywords
        '((sequence "APPT(a@/!)" "TODO(t)" "STARTED(s!)" "WAIT(w@/!)" "|" "DONE(d!)" "CANCEL(c@/!)")))
     (setq org-log-done 'time)   ;;; DONEの時刻を記録
     ;; (setq org-log-done 'note)  ;;; DONEの時刻とメモを記録

     ;; TAGリストの設定
     ;; #+TAGS: @OFFICE(o) @HOME(h)
     ;; #+TAGS: SHOPPING(s) MAIL(m) PROJECT(p)
     (setq org-tag-alist
        '((:startgroup . nil)
          ("HOME" . ?h) ("OFFICE" . ?o)("IPNSPR" . ?i)("KEKPR" . ?k)
          (:endgroup . nil)
          (:newline . nil)
          (:startgroup . nil)
          ("TOPICS" . ?t) ("PRESS" . ?p)("HIGHLIGHT" . ?l)("EVENT" . ?e)
          (:endgroup . nil)
          (:newline . nil)
          (:startgroup . nil)
          ("T2K" . nil) ("BELLE" . nil)("COMET" . nil)
          (:endgroup . nil)
          (:newline . nil)
          (:startgroup . nil)
          ("READING" . ?r) ("WRITING" . ?w)("ASKING" . ?a)
          (:endgroup . nil))
        )

     ;; アジェンダ表示で下線を用いる
     (add-hook 'org-agenda-mode-hook '(lambda () (hl-line-mode 1)))
  )


使い方
==================================================


.. toctree::
   :maxdepth: 1

   emacs-org-latex
   emacs-org-agenda
   emacs-org-capture
