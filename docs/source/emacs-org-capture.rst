==================================================
メモ連携
==================================================

設定
==================================================


.. code-block:: emacs

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
