# 「データ分析と情報管理特論」サポートサイト

```sh
  mkdir gdb2026py # 作業フォルダを作成
  cd gdb2026py # 作業フォルダに入る

# 仮想環境作成(Pythonバージョン指定)
  python3.13 -m venv .venv-gdb2026

# 仮想環境を切り替える
  source .venv-gdb2026/bin/activate

# 仮想環境を終了
  deactivate

# 必要なパッケージをインストール
　pip install パッケージ名 
　　
# インストールされたパッケージの確認
　pip list 
　pip show パッケージ名

# インストールされたパッケージリスト出力（再インストール）
　pip freeze 
　pip freeze > requirements.txt 

# 再インストール
  pip install -r requirements.txt

```