# Learning *Deep Learning and Physics*

## 開発情報

Sphinx で書いていきます。マークアップは reStructuredText（reST）ではなく Markdown を使います。
Poetry を使って Sphinx 環境を作るために、 [shotakaha/kumaroot](https://github.com/shotakaha/kumaroot) を fork させて頂きました。

### 環境構築

#### Poetry による Python 環境の構築

- [Sphinxによるドキュメント作成と国際化の事始め - Qiita](https://qiita.com/tatsurou313/items/8bf7b43842b7827760fa#poetry-%E3%82%92%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%97%E3%81%A6%E4%BB%AE%E6%83%B3%E7%92%B0%E5%A2%83%E3%82%92%E6%A7%8B%E7%AF%89%E3%81%99%E3%82%8B)

が参考になります。

```sh
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

で Poetry をインストールして、 PATH を設定後、

```sh
poetry install
```

すると必要パッケージがインストールされます。

### ビルド

```sh
poetry run make html
```

で `build/html` に HTML が生成されます。

## License

- 本リポジトリは [MIT ライセンス](https://github.com/pn11/learning-dl-and-phys/blob/master/LICENSE)です。
- [kumaroot](https://github.com/shotakaha/kumaroot) は [MIT ライセンスです](https://github.com/shotakaha/kumaroot/blob/master/LICENSE)。
