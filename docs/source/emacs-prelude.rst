==================================================
Emacs初期設定集の導入
==================================================

Emacsを **便利に使う** ためには、ある程度設定をきちんとしないといけません。
でもそれはなかなかめんどくさいです。
そんなめんどくさがり屋さんのために（？）、
GitHubで公開されているEmacs初期設定集があります。
（ありがたや、ありがたや）

少しググるだけで以下のものが見つかります。

* `Prelude <https://github.com/bbatsov/prelude>`__
* `oh-my-emacs <https://github.com/xiaohanyu/oh-my-emacs>`__
* `emacs24-starter-kit <https://github.com/eschulte/emacs24-starter-kit>`__

他にもいろいろあるのかもしれませんが、
名前がオシャレだなと思ったので、僕はPreludeに決めました。

以下ではPreludeの設定方法を説明します。


Preludeのインストール
==================================================

PreludeはGitHubにあります。
本家リポジトリを直接cloneしてしまうと、
自分の変更をpushしたときに大変なことになるため、
自分のGitHubにforkするのがよいでしょう。

ただし、本家の更新も取り込みたいので、
いつでも参照できるように専用のブランチを作ります。
（あとで追記する）

.. code-block:: bash

    $ cd ~/repos/github/
    $ git clone https://github.com/shotakaha/prelude
    $ export PRELUDE_URL="https://github.com/yourname/prelude.git" && curl -L https://github.com/bbatsov/prelude/raw/master/utils/installer.sh | sh


Preludeの更新・管理
==================================================

オリジナル（ :file:`bbatsov/prelude` ）の変更を簡単に取り込めるようにリモートブランチを設定する。
以下ではリモートブランチ名を ``upstream`` とした。

.. code-block:: bash

   $ cd .emacs.d/
   $ git remote -v
   origin	https://github.com/shotakaha/prelude.git (fetch)
   origin	https://github.com/shotakaha/prelude.git (push)
   $ git remote set-url upstream https://github.com/bbatsov/prelude.git
   $ git remote -v
   origin	https://github.com/shotakaha/prelude.git (fetch)
   origin	https://github.com/shotakaha/prelude.git (push)
   upstream	https://github.com/bbatsov/prelude.git (fetch)    ## <-- 追加
   upstream	https://github.com/bbatsov/prelude.git (push)     ## <-- 追加


更新は以下の手順で行う。

#. オリジナル（ :file:`bbatsov/prelude` ）の更新を取り込む
#. 自分のmasterブランチ（= :file:`origin/master` ）にマージする
#. 更新したmasterブランチをdevelopブランチにマージする

そのGit操作は以下のようになる。

.. code-block:: bash

   ## bbastov/preludeの更新を取り込む
   $ git fetch upstream

   ## 自分のmasterブランチにマージする
   $ git checkout master
   $ git merge upstream/master

   ## 更新したmasterブランチをdevelopブランチにマージする
   $ git checkout develop
   $ git merge master




Preludeの初期設定
==================================================

#. :file:`.emacs.d/prelude-module.el` を開き、使いたいモジュールを選択（コメントしたり、コメントアウトしたり）する。
#. Emacsを起動すると、初期設定に必要なパッケージ群が自動でインストールされる（後述するEmacsのパッケージ管理ツールを利用してます）


Preludeの個人設定
==================================================

個人設定は :file:`.emacs.d/personal/` 以下にファイルを作成する。
