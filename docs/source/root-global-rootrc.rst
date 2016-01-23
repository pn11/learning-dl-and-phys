==================================================
個人設定したい
==================================================

bashの個人設定を :file:`~/.bashrc` に書くように、ROOTの個人設定は :file:`~/.rootrc` に書きます。
デフォルト値は :file:`$ROOTSYS/etc/system.rootrc` に書かれているので、
これをホームディレクトリにコピーして編集すればOKです。

.. code-block:: console

    $ locate system.root
    ## =>  $ROOTSYS/etc/system.rootrc
    $ cp $ROOTSYS/etc/system.rootrc ~/.rootrc


ディレクトリ毎の設定
==================================================

ディレクトリ（やプロジェクト）毎の設定は
ROOTマクロを起動するディレクトリ直下の :file:`rootlogon.C` に書きます。
