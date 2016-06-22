==================================================
Homebrewを使う方法
==================================================

.. note:: 2016年6月4日に追記

前ページで「Homebrewに関する情報があればくださいな」と書きましたが、最近調べてみたら、Homebrewでもインストールできるようになってました。
``ROOT6`` は ``homebrew/science/root6`` 、``ROOT5`` は ``homebrew/science/root`` です。

.. code-block:: bash

   $ brew search root
   ...
   homebrew/science/root
   homebrew/science/root6
   ...


ROOT6
==================================================

.. code-block:: bash

   $ brew info root6
   homebrew/science/root6: stable 6.06.04 (bottled), HEAD
   Object oriented framework for large scale data analysis
   https://root.cern.ch
   Conflicts with: root
   /usr/local/Cellar/root6/6.06.04 (5,045 files, 410.1M) *
   Poured from bottle on 2016-06-01 at 22:59:31
   From: https://github.com/Homebrew/homebrew-science/blob/master/root6.rb
   ==> Dependencies
   Build: cmake ✔
   Recommended: openssl ✔, gsl ✔
   Optional: xrootd ✘
   ==> Options
   --with-xrootd
	Build with xrootd support
   --without-gsl
	Build without gsl support
   --without-openssl
	Build without openssl support
   --without-python
	Build without python support
   --HEAD
	Install HEAD version
   ==> Caveats
   Because ROOT depends on several installation-dependent
   environment variables to function properly, you should
   add the following commands to your shell initialization
   script (.bashrc/.profile/etc.), or call them directly
   before using ROOT.

   For bash users:
     . $(brew --prefix root6)/libexec/thisroot.sh
   For zsh users:
     pushd $(brew --prefix root6) >/dev/null; . libexec/thisroot.sh; popd >/dev/null
   For csh/tcsh users:
     source `brew --prefix root6`/libexec/thisroot.csh

   Emacs Lisp files have been installed to:
     /usr/local/share/emacs/site-lisp/root6


ROOT5
==================================================

.. code-block:: bash

   $ brew info root
   homebrew/science/root: stable 5.34.34 (bottled), HEAD
   Object oriented framework for large scale data analysis
   http://root.cern.ch
   Not installed
   From: https://github.com/Homebrew/homebrew-science/blob/master/root.rb
   ==> Dependencies
   Required: openssl ✔
   Recommended: xrootd ✘, gsl ✔
   Optional: fftw ✘, qt ✘
   ==> Options
   --with-fftw
	Build with fftw support
   --with-qt
	Build with Qt graphics backend and GSI's Qt integration
   --with-x11
	Build with x11 support
   --without-gsl
	Build without gsl support
   --without-xrootd
	Build without xrootd support
   --HEAD
	Install HEAD version
   ==> Caveats
   Because ROOT depends on several installation-dependent
   environment variables to function properly, you should
   add the following commands to your shell initialization
   script (.bashrc/.profile/etc.), or call them directly
   before using ROOT.

   For bash users:
        . $(brew --prefix root)/libexec/thisroot.sh
   For zsh users:
        pushd $(brew --prefix root) >/dev/null; . libexec/thisroot.sh; popd >/dev/null
   For csh/tcsh users:
        source `brew --prefix root`/libexec/thisroot.csh
