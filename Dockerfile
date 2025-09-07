FROM python:3.11-slim
# https://hub.docker.com/にてpython＞「Official Image」
# bookworm Debianという安定性の高いOSのバージョン名
# コミュニティでの評価: GitHubやStack Overflowなどで検索
# 最新すぎず、ある程度の期間を経て安定しているという理由で、信頼性が高い選択肢

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
# ①バイトコード書かない コンテナ内で環境変数を設定する命令 .pycというバイトコードファイル生成を無効
# コンテナを頻繁にビルド・再構築する場合、このファイルを生成しないことで少しだけ高速化したり、
# イメージのサイズを小さく保つことができます。
# ②アンバッファード Pythonの標準出力（print()関数など）が即座に表示されるようにする設定
# ログがバッファ（一時的なメモリ）に溜められてしまい、リアルタイムでログを確認できない
# この設定は、開発中やデバッグ時に特に役立つ

WORKDIR /app
# コンテナ内の/appディレクトリを基準
# Dockerでのプロジェクトルートディレクトリ

# 依存を先に入れる（キャッシュ利用）
COPY requirements.txt .
# 自分の部屋のファイルを隣の部屋に置く
RUN pip install --no-cache-dir -r requirements.txt
# pipツールでインストール　pipはインストールしたパッケージをキャッシュディレクトリに保存
# Dockerでは、各命令（FROM, RUN, COPYなど）が実行されるたびに、新しいレイヤーが作成
# イメージサイズの増加/ビルドの非効率化

# パッケージ & テストをコピー
COPY app_day02 ./app_day02
COPY tests ./tests
# app_day02フォルダとtests**フォルダを、それぞれコンテナ内の作業ディレクトリにコピーする
# COPY <ソースパス> <コンテナ内のパス>Dockerfileがあるディレクトリ）からの相対パスを指定
# learning-log/app_day02フォルダを、コンテナ内の/app/app_day02にコピー

EXPOSE 8000
CMD ["uvicorn", "app_day02.main:app", "--host", "0.0.0.0", "--port", "8000"]
# コンテナが起動したときに実行されるコマンド
# uvicornは、PythonのWebサーバーを起動するためのツール
# app_day02.mainにあるWebアプリケーション（app）を、0.0.0.0というアドレスのポート8000で起動

# ========================================
# Docker コマンド集
# ========================================
# 1. イメージビルド
#    docker build --no-cache -t day02-echo .
#
# 2. コンテナ起動
#    docker run -p 8080:8000 day02-echo
#
# 3. 動作確認
#    docker ps                    # コンテナ状態確認
#    http://localhost:8080/docs   # APIドキュメント
#    http://localhost:8080/echo   # Echoエンドポイント
#
# 4. その他のコマンド
#    docker stop <container_id>   # コンテナ停止
#    docker logs <container_id>   # ログ確認
# ========================================

# 1. 既存のコンテナを停止
# docker ps                    # コンテナIDを確認
# docker stop <コンテナID>     # 既存のコンテナを停止

# 2. Dockerイメージの再ビルド
# docker build --no-cache -t day02-echo .
# 注意: .dockerignoreで不要なファイルを除外

# 3. 新しいコンテナを起動
# docker run -p 8080:8000 day02-echo
