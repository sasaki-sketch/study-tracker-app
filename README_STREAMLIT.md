# Streamlit学習アプリ - 運用ガイド

最終更新: 2026-01-04

## 📋 概要

中小企業診断士・統計検定2級の学習記録を管理するStreamlitアプリケーションの自動起動設定と設定ファイルの完全ガイド。

---

## 🚀 自動起動設定

### launchdサービス

**設定ファイル**: `~/Library/LaunchAgents/com.user.streamlit.study.plist`

#### サービス管理コマンド

```bash
# サービス状態確認
launchctl list | grep streamlit

# サービス起動
launchctl start com.user.streamlit.study

# サービス停止
launchctl stop com.user.streamlit.study

# サービス再起動
launchctl stop com.user.streamlit.study && launchctl start com.user.streamlit.study

# サービス登録解除
launchctl unload ~/Library/LaunchAgents/com.user.streamlit.study.plist

# サービス再登録
launchctl load ~/Library/LaunchAgents/com.user.streamlit.study.plist
```

#### 自動起動の特徴

- **システム起動時に自動実行**: Mac起動時に自動でStreamlitアプリが起動
- **クラッシュ時の自動再起動**: アプリが停止した場合、10秒後に自動再起動
- **ログ記録**: 起動ログは `~/study_app/logs/` に保存

---

## ⚙️ Streamlit設定ファイル

**設定ファイル**: `~/.streamlit/config.toml`

### 主要設定の説明

#### [server] - サーバー設定
```toml
headless = true                    # ブラウザを自動で開かない
address = "0.0.0.0"                # 全ネットワークインターフェースでリッスン
port = 8501                        # ポート番号
maxUploadSize = 200                # アップロード上限 200MB
enableCORS = false                 # CORS無効（ローカル利用のため）
enableXsrfProtection = true        # CSRF保護有効
enableWebsocketCompression = true  # WebSocket圧縮で高速化
runOnSave = false                  # 自動リロード無効
```

#### [browser] - ブラウザ設定
```toml
gatherUsageStats = false           # 使用統計の送信を無効化
serverAddress = "localhost"        # ブラウザ接続先
serverPort = 8501                  # ブラウザ接続ポート
```

#### [runner] - 実行環境設定
```toml
magicEnabled = true                # マジックコマンド有効
fixMatplotlib = true               # Matplotlib互換性修正
postScriptGC = true                # スクリプト実行後にGC実行（メモリ最適化）
fastReruns = true                  # 高速再実行モード
```

#### [client] - クライアント設定
```toml
showErrorDetails = true            # エラー詳細表示
toolbarMode = "minimal"            # ツールバーをミニマル表示
```

#### [theme] - テーマ設定
```toml
base = "dark"                      # ダークモード
primaryColor = "#667eea"           # プライマリカラー（紫）
backgroundColor = "#0e1117"        # 背景色（黒）
secondaryBackgroundColor = "#262730" # セカンダリ背景色（濃いグレー）
textColor = "#fafafa"              # テキスト色（白）
```

#### [global] - グローバル設定
```toml
developmentMode = false            # 本番モード
suppressDeprecationWarnings = true # 非推奨警告を抑制
disableWatchdogWarning = true      # Watchdog警告を無効化
```

---

## 📁 ディレクトリ構造

```
~/study_app/
├── app_v3.py                      # メインアプリケーション
├── start_streamlit.sh             # 起動スクリプト
├── logs/                          # ログディレクトリ
│   ├── launchd_stdout.log         # launchd標準出力
│   ├── launchd_stderr.log         # launchdエラー出力
│   └── streamlit_*.log            # Streamlit起動ログ
├── database/                      # データベース関連
├── models/                        # データモデル
├── services/                      # サービスレイヤー
├── utils/                         # ユーティリティ
└── components/                    # UIコンポーネント
```

---

## 🔧 トラブルシューティング

### アプリが起動しない場合

1. **ログ確認**
   ```bash
   tail -f ~/study_app/logs/launchd_stderr.log
   ```

2. **手動起動テスト**
   ```bash
   cd ~/study_app
   streamlit run app_v3.py
   ```

3. **ポート競合確認**
   ```bash
   lsof -i :8501
   ```

### サービスが自動起動しない場合

1. **plistファイルの権限確認**
   ```bash
   ls -la ~/Library/LaunchAgents/com.user.streamlit.study.plist
   ```

2. **サービス再登録**
   ```bash
   launchctl unload ~/Library/LaunchAgents/com.user.streamlit.study.plist
   launchctl load ~/Library/LaunchAgents/com.user.streamlit.study.plist
   ```

### メモリ使用量が多い場合

1. **設定調整**: `~/.streamlit/config.toml` の `postScriptGC = true` を確認
2. **不要なデータ削除**: データベースのクリーンアップ

---

## 🌐 アクセス方法

### ローカル
```
http://localhost:8501
```

### 同一ネットワーク内の他デバイスから
```
http://<MacのIPアドレス>:8501
```

IPアドレス確認:
```bash
ifconfig | grep "inet " | grep -v 127.0.0.1
```

---

## 📊 パフォーマンス最適化設定

以下の設定により、アプリのパフォーマンスが最適化されています：

1. **WebSocket圧縮**: 通信の高速化
2. **FastReruns**: UI更新の高速化
3. **PostScriptGC**: メモリ使用量の最適化
4. **Minimal Toolbar**: UIの軽量化

---

## 🔒 セキュリティ設定

1. **XSRF保護有効**: CSRF攻撃を防止
2. **統計送信無効**: プライバシー保護
3. **CORS無効**: ローカル専用利用

---

## 📝 メンテナンス

### ログローテーション

ログファイルが肥大化した場合:

```bash
# 古いログを削除（30日以上前）
find ~/study_app/logs -name "*.log" -mtime +30 -delete
```

### データベースバックアップ

```bash
# データベースのバックアップ
cp ~/study_app/study_records.db ~/study_app/study_records_$(date +%Y%m%d).db
```

---

## 🆘 サポート

問題が発生した場合は、以下のログを確認してください：

1. `~/study_app/logs/launchd_stderr.log` - launchdエラーログ
2. `~/study_app/logs/streamlit_*.log` - Streamlit起動ログ

---

**作成日**: 2026-01-04
**対象OS**: macOS (Darwin 25.2.0)
**Python**: 3.13
**Streamlit**: 1.51.0
