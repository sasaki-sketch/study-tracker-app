#!/bin/bash

# Streamlit学習アプリ起動スクリプト
# 作成日: 2026-01-04

# 環境変数の読み込み
if [ -f ~/.zshrc ]; then
    source ~/.zshrc
fi

# ログディレクトリ作成
LOG_DIR="$HOME/study_app/logs"
mkdir -p "$LOG_DIR"

# タイムスタンプ
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
LOG_FILE="$LOG_DIR/streamlit_${TIMESTAMP}.log"

# アプリディレクトリに移動
cd "$HOME/study_app" || exit 1

# Python3とStreamlitのパス確認
PYTHON_PATH=$(which python3)
STREAMLIT_PATH=$(which streamlit)

echo "=== Streamlit起動 ===" | tee -a "$LOG_FILE"
echo "起動時刻: $(date)" | tee -a "$LOG_FILE"
echo "Python: $PYTHON_PATH" | tee -a "$LOG_FILE"
echo "Streamlit: $STREAMLIT_PATH" | tee -a "$LOG_FILE"
echo "作業ディレクトリ: $(pwd)" | tee -a "$LOG_FILE"
echo "=====================" | tee -a "$LOG_FILE"

# Streamlit起動（バックグラウンド実行）
exec streamlit run app_v3.py \
    --server.headless=true \
    --server.address=0.0.0.0 \
    --server.port=8501 \
    >> "$LOG_FILE" 2>&1
