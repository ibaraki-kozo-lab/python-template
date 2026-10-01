# python-template

研究室でPythonのプロジェクトを作るためのテンプレートである．何度も使う関数（パッケージ），実行するスクリプト，テスト，入力のデータ，出力をフォルダに分けて置き，`make` で検査する．PRを出すと，GitHub Actionsが同じ `make` を実行して検査する．

## 準備

uv，Make，Gitを使う．入れ方は，[研究室ハンドブック][hb]の「[環境構築（uv）][hb-uv-install]」「[Make][hb-make-install]」「[はじめてのGit・GitHub][hb-git]」にある．このテンプレートは，ハンドブックの「[実践：Pythonパッケージ][hb-package]」まで読んだ前提で書いてある．ハンドブックは研究室の人だけが読めるサイトで，開くときは，管理者が登録した大学のメールアドレスを使う．

VS Codeでフォルダを開くと，おすすめの拡張機能（Python，Ruff）を入れるか尋ねられる．入れると，保存するたびに書式が整う．

## はじめにやること

このテンプレートから新しいリポジトリを作るときは，次を1度だけ行う．終わったら，この節は消してよい．

1. テンプレートのページ（`ibaraki-kozo-lab/python-template`）で **Use this template** → **Create a new repository** を選び，リポジトリを作る．研究で使うリポジトリは，管理者が研究室のorganizationに作る．練習なら，自分のアカウントに作ってよい
2. 作ったリポジトリをクローンし，その中で `make` を実行する．最後に `3 passed` と出れば，準備はできている
3. パッケージの名前を，仮の `my_package` から自分のものに変える（[パッケージの名前を変える](#パッケージの名前を変える)）
4. 例として入っている「単純はりのたわみ」を，自分のものに置き換える
    - `src/my_package/beam.py` を消したら，`src/my_package/__init__.py` の `import` の行と `__all__` からも外す
    - `tests/test_beam.py` は，自分のテストを足してから消す．テストが1つもないと，`make` の `test` が失敗する
    - `scripts/plot_deflection.py` と `data/beams.csv` を自分のものにし，`data/README.md` の表も書き換える
5. この `README.md` の見出し（`# python-template`）と最初の段落，`pyproject.toml` の `description` を，何をするリポジトリかの説明に書き換える

### パッケージの名前を変える

リポジトリの名前が `slope-study` なら，プロジェクトの名前を `slope-study`，パッケージの名前を `slope_study` にする．`import` で書く名前には `-` を使えないので，`-` を `_` にしたものがパッケージの名前になる（ハンドブックの「[実践：Pythonパッケージ][hb-package]」の「[パッケージの形でプロジェクトを作る][hb-package-init]」）．

1. パッケージのフォルダの名前を変える

    ```sh
    git mv src/my_package src/slope_study
    ```

2. `pyproject.toml` の `name = "my-package"` を `name = "slope-study"` にする
3. リポジトリの中の `my_package` を，すべて `slope_study` に置き換える（`src/`，`tests/`，`scripts/` の `import` と，この `README.md`）．VS Codeなら，Ctrl+Shift+H（macOSでは Cmd+Shift+H）で，すべてのファイルの中を一度に置き換えられる
4. `make` を実行し，最後まで通ることを確かめる．このとき `uv run` が，`uv.lock` に書かれたプロジェクトの名前も書き直す
5. `uv.lock` も含めて，変更をすべてコミットする

## このリポジトリの地図

| 場所 | 中身 | 扱い |
|------|------|------|
| `src/my_package/` | 何度も使う関数をまとめたパッケージ．`__init__.py` が入口 | 書く |
| `scripts/` | 実行するスクリプト（解析，図を描く）．1つのファイルに1つの目的 | 書く |
| `tests/` | 答えの分かる問題で，パッケージの関数を確かめるテスト | 書く |
| `data/` | 入力のデータ．元のデータは書き換えない．出典は `data/README.md` に書く | 置く |
| `README.md` | この説明 | 書く |
| `pyproject.toml` | 使うパッケージと，道具の設定 | `uv add` で変わる．ときどき直す |
| `uv.lock` | 入れたパッケージのバージョンの記録 | 触らない（コミットはする） |
| `.python-version` | 使うPythonのバージョン（3.12） | 触らない |
| `Makefile` | 検査の手順 | ふだんは触らない |
| `AGENTS.md` | このリポジトリの決まり（人とAIエージェント向け） | ときどき直す |
| `CLAUDE.md` | Claude Codeに `AGENTS.md` を読ませる1行（`@AGENTS.md`） | 触らない |
| `.github/` | CI（`workflows/check.yml`）とPRのひな形 | ふだんは触らない |
| `.vscode/` | VS Codeのおすすめの拡張機能と設定 | ふだんは触らない |
| `.gitignore` | Gitに記録しないものの一覧 | ふだんは触らない |
| `results/` | スクリプトの出力（図，表） | Gitに記録しない |
| `.venv/` | uvが作る仮想環境 | Gitに記録しない |
| `__pycache__/`，`.pytest_cache/`，`.ruff_cache/` | Pythonと検査の道具が作るもの | Gitに記録しない |

`results/` はスクリプトを実行すると，そのほかの記録しないものは `make` や `uv run` を実行するとできる．どれもいつでも作り直せるので，Gitには記録しない．

## 使い方

スクリプトは，リポジトリの一番上から `uv run` で実行する．

```sh
uv run python scripts/plot_deflection.py
```

`data/beams.csv` の条件ごとのたわみを計算し，1枚の図に線で描いて，`results/deflection.png` に保存する．図は `savefig` で保存し，`plt.show()` は使わない（研究室の計算機のように，画面のないところでも動くようにする）．

パッケージを足すときは `uv add`，検査の道具を足すときは `uv add --dev` を使う．`pyproject.toml` と `uv.lock` が書き換わるので，両方をコミットする．たとえば，pandasを足すなら次のようにする．

```sh
uv add pandas
```

検査は `make` で行う．CIも同じ `make`（`make check`）を実行するので，手元で通ればCIでも通る．

| コマンド | すること |
|----------|----------|
| `make` | 検査する（CIと同じ）．`lint`，`typecheck`，`test` の順に実行し，失敗したらそこで止まる |
| `make format` | 書き方の指摘のうち自動で直せるものを直し，書式を整える．`lint` で止まったら実行する |
| `make test` | テストだけを実行する |
| `make help` | この一覧を表示する |

`make` が実行する検査は次の3つである．道具の使い方は，ハンドブックの「[品質チェック][hb-quality]」にある．

| 検査 | 道具 | 確かめること |
|------|------|--------------|
| `lint` | ruff | 書き方の誤りと，書式が整っているか |
| `typecheck` | pyright | 型ヒントと合わない使い方をしていないか |
| `test` | pytest | `tests/` のテストが通るか |

## 関数とスクリプトを足す

- 2つ以上のスクリプトやテストから使う関数は，`src/my_package/` のファイルに書く．`__init__.py` の `import` の行と `__all__` に足すと，どのフォルダのファイルからも `from my_package import 関数の名前` で読み込める．型ヒントとdocstringを書き，答えの分かる問題で確かめるテストを `tests/` に足す（小数は `pytest.approx` で比べる）
- 1回の解析や1枚の図を作るものは，`scripts/` に置く．入力は `data/` から読み，出力は `results/` に書く．順に実行するものは，`01_preprocess.py` のように番号を付けると，順番が分かる
- Jupyterで試すときは，`uv add --dev jupyterlab` で入れ（ハンドブックの「[Jupyter][hb-jupyter]」），ノートブックは `notebooks/` を作って置く．`notebooks/` は `make` の検査から外してある．コミットする前に出力を消し（同じページの「[ノートブックをGitで扱う][hb-jupyter-git]」），結果として残す計算はスクリプトにする

## 結果を残す

`results/` はGitに記録しない．論文などに使う結果は，どのコードと入力で計算したかを一緒に残す．

1. 計算する前に，変更をすべてコミットする
2. `git rev-parse HEAD` で表示されるコミットの番号と，乱数の種（使うなら）を，結果のファイルと一緒に記録する
3. パッケージのバージョンは `uv.lock` に残っているので，同じコミットを `uv run` すれば同じバージョンで計算される

スクリプトの中で記録する書き方は，ハンドブックの「[実践：パラメータスタディ][hb-study]」の「[再現できるように記録する][hb-study-reproduce]」にある．時間のかかる計算は，同じページの手順で研究室の計算機で回す．

## 困ったとき

| 表示や様子 | 原因と対処 |
|------------|------------|
| `ModuleNotFoundError: No module named 'matplotlib'` など | `uv run` を付けずに `python3` で実行した．`uv run python scripts/…` で実行する |
| `Expected a Python module at: src/…/__init__.py` | パッケージのフォルダの名前と，`pyproject.toml` の `name` が合っていない．2つを見比べて直す（[パッケージの名前を変える](#パッケージの名前を変える)） |
| `make` が `lint` で止まり，`1 file would be reformatted` と出る | 書式が整っていない．`make format` で直す |
| `make` が `test` で止まり，`no tests ran`（`tests/` のフォルダがないときは `No files were found in testpaths`）と `Error 5` が出る | テストが1つもない．`tests/` にテストを足す |

## 変更の流れ

変更はブランチで作り，PRを出す．PRではCIが `make` を実行する．✗ が付いたら，**Details** からログを開いて直す（ハンドブックの「[ブランチとPR][hb-branches]」と「[GitHub Actions（CI）][hb-actions]」）．PRの本文は，ひな形のChecklistを埋める．このリポジトリの決まりは `AGENTS.md` にある．

<!-- 研究室ハンドブックへのリンク．ハンドブックのページの場所が変わったら，ここを直す -->

[hb]: https://lab-handbook-ein.pages.dev/
[hb-uv-install]: https://lab-handbook-ein.pages.dev/python/uv/#install
[hb-make-install]: https://lab-handbook-ein.pages.dev/dev/make/#install
[hb-git]: https://lab-handbook-ein.pages.dev/dev/git/
[hb-package]: https://lab-handbook-ein.pages.dev/practice/package/
[hb-package-init]: https://lab-handbook-ein.pages.dev/practice/package/#init
[hb-quality]: https://lab-handbook-ein.pages.dev/python/quality/
[hb-jupyter]: https://lab-handbook-ein.pages.dev/python/jupyter/
[hb-jupyter-git]: https://lab-handbook-ein.pages.dev/python/jupyter/#notebooks-in-git
[hb-study]: https://lab-handbook-ein.pages.dev/practice/parameter-study/
[hb-study-reproduce]: https://lab-handbook-ein.pages.dev/practice/parameter-study/#reproduce
[hb-branches]: https://lab-handbook-ein.pages.dev/dev/branches/
[hb-actions]: https://lab-handbook-ein.pages.dev/dev/actions/
