# 検査をまとめたもの．使い方は README.md にある．
# コマンドの行の先頭はタブ．空白にすると missing separator で止まる．

.PHONY: check lint typecheck test format help

# make だけで実行される（最初のターゲット）．CIも同じ make check を実行する
check: lint typecheck test

# 書き方の検査（ruff check）と，書式が整っているかの検査（ruff format --check）
lint:
	uv run ruff check .
	uv run ruff format --check .

# 型の検査
typecheck:
	uv run pyright

# テスト（tests/）
test:
	uv run pytest

# lint の指摘のうち自動で直せるものを直し（ruff check --fix），書式を整える（ruff format）
format:
	uv run ruff check --fix .
	uv run ruff format .

help:
	@echo "make         検査する（CIと同じ．lint，typecheck，test の順）"
	@echo "make format  書き方の指摘のうち直せるものを直し，書式を整える"
	@echo "make test    テストだけを実行する"
