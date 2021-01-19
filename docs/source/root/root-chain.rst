TChain編
========

``TChain`` を使うと同じ構造の ``TTree``
を複数連結（＝chain）して、ひとつの ``TTree`` として扱うことができます。
``TTree`` を継承したクラスなので、連結した後は ``TTree``
と同じように使えばOKです。

複数のTTreeを読み込みたい
-------------------------

.. code:: cpp

    TChain *chain=new TChain("tree", "tree title");

第１引数
    読み込むTTreeの名前; 読み込むTTreeの名前と一致してないと怒られる
第２引数
    タイトル; 説明みたいなもの。なくても大丈夫

.. code:: cpp

    chain->Add("../anadata/CALIB_RUN10.root");
    chain->Add("../anadata/CALIB_RUN11.root");
    chain->Add("../anadata/CALIB_RUN12.root");

第１引数
    ファイル名; ワイルドカード指定もできる

サンプルコード : ループで読み込む
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: cpp

    TChain *chain=new TChain("chain", "chainname");
    const Int_t fNFile=11;
    Int_t iFile;
    for (iFile=0; iFile<fNFile; ++iFile) {
        chain->Add(Form("../anadata/CALIB_RUN%d.root", iFile+10));
    }

サンプルコード : ワイルドカード指定
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: cpp

    TChain *ch = new TChain("upk");
    ch->Add("upk_run*.root")

読み込んだTTreeの数を知りたい
-----------------------------

.. code:: cpp

    chain->GetNtrees()

読み込んだTTreeのリストを取得したい
-----------------------------------

.. code:: cpp

    TObjArray *fileElements = fBsd->GetListOfFiles();
    TIter next(fileElements);
    TChainElement *chEl = 0;
    while (( chEl=(TChainElement*)next() )) {
        fprintf(stdout, "[%s]\tListOfFiles\t'%s'\n", __FUNCTION__, chEl->GetTitle() );
    }

ROOTマニュアルに載ってた
