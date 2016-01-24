==================================================
アジェンダ連携
==================================================


設定
==================================================

.. code-block:: emacs

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
