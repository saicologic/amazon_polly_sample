# Python Env

```
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

# 環境変数の設定

```
export AWS_PROFILE=xxxx
```

# 実行

読み上げたい文書を設定する。日本語に固定している

例: こんにちは

```
python ./voice.py say "こんにちは"
```
