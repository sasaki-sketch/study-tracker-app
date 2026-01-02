# Hostinger VPSデプロイ手順書

診断士学習記録アプリをHostinger VPSにデプロイする手順です。

## 前提条件

- Hostinger VPSプラン契約済み
- SSH接続情報（IPアドレス、ユーザー名、パスワード）
- ドメイン名（オプション）

---

## 1. VPSへのSSH接続

```bash
ssh your-username@your-vps-ip
```

初回接続時はfingerprint確認で`yes`を入力してください。

---

## 2. システムアップデートとPython3インストール

```bash
# システムアップデート
sudo apt update && sudo apt upgrade -y

# Python3とpip、venvをインストール
sudo apt install python3 python3-pip python3-venv git -y

# バージョン確認
python3 --version
```

---

## 3. アプリケーションのアップロード

### 方法A: Gitリポジトリから（推奨）

```bash
# Gitリポジトリからクローン
cd ~
git clone https://github.com/your-username/study_app.git
cd study_app
```

### 方法B: SCPで直接転送

ローカルMacから実行:

```bash
# study_appディレクトリ全体を転送
cd ~/study_app
scp -r * your-username@your-vps-ip:~/study_app/
```

---

## 4. Python仮想環境のセットアップ

```bash
cd ~/study_app

# 仮想環境を作成
python3 -m venv venv

# 仮想環境を有効化
source venv/bin/activate

# 依存パッケージをインストール
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 5. データベースの初期化

```bash
# アプリを一度起動してDBを初期化
python3 -c "from database.init_db import init_database; init_database()"
```

---

## 6. Streamlitの動作確認

```bash
# テスト起動
streamlit run app_v3.py --server.address=0.0.0.0 --server.port=8501

# ブラウザでアクセス: http://your-vps-ip:8501
# 動作確認後、Ctrl+Cで停止
```

---

## 7. systemdサービスの設定（自動起動）

```bash
# サービスファイルを編集（ユーザー名を実際のものに変更）
nano ~/study_app/study-app.service
# 以下を変更:
#   - User=your-username → 実際のユーザー名
#   - WorkingDirectory=/home/your-username/study_app → 実際のパス
#   - ExecStart=/home/your-username/study_app/venv/bin/streamlit → 実際のパス

# systemdにサービスファイルをコピー
sudo cp ~/study_app/study-app.service /etc/systemd/system/

# systemdを再読み込み
sudo systemctl daemon-reload

# サービスを有効化（起動時に自動起動）
sudo systemctl enable study-app

# サービスを起動
sudo systemctl start study-app

# ステータス確認
sudo systemctl status study-app
```

---

## 8. ファイアウォール設定

```bash
# UFW（ファイアウォール）がインストールされていない場合
sudo apt install ufw -y

# SSH（22番ポート）を許可
sudo ufw allow 22/tcp

# Streamlit（8501番ポート）を許可
sudo ufw allow 8501/tcp

# ファイアウォールを有効化
sudo ufw enable

# ステータス確認
sudo ufw status
```

---

## 9. Nginxリバースプロキシ設定（オプション・推奨）

ポート80/443でアクセスできるようにする場合:

```bash
# Nginxをインストール
sudo apt install nginx -y

# Nginx設定ファイルを作成
sudo nano /etc/nginx/sites-available/study-app

# 以下を貼り付け:
server {
    listen 80;
    server_name your-domain.com;  # またはVPSのIPアドレス

    location / {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}

# シンボリックリンクを作成
sudo ln -s /etc/nginx/sites-available/study-app /etc/nginx/sites-enabled/

# Nginx設定テスト
sudo nginx -t

# Nginxを再起動
sudo systemctl restart nginx

# ポート80を許可
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
```

---

## 10. SSL証明書の設定（オプション・推奨）

Let's Encryptで無料SSL証明書を取得:

```bash
# Certbotをインストール
sudo apt install certbot python3-certbot-nginx -y

# SSL証明書を取得・設定
sudo certbot --nginx -d your-domain.com

# 自動更新のテスト
sudo certbot renew --dry-run
```

---

## 11. サービス管理コマンド

```bash
# サービス起動
sudo systemctl start study-app

# サービス停止
sudo systemctl stop study-app

# サービス再起動
sudo systemctl restart study-app

# サービスステータス確認
sudo systemctl status study-app

# ログ確認
sudo journalctl -u study-app -f
```

---

## 12. アップデート手順

コードを更新した場合:

```bash
# VPSにSSH接続
ssh your-username@your-vps-ip

# アプリディレクトリに移動
cd ~/study_app

# Gitから最新版を取得（Gitを使用している場合）
git pull

# 仮想環境を有効化
source venv/bin/activate

# 依存パッケージを更新（必要な場合）
pip install -r requirements.txt --upgrade

# サービスを再起動
sudo systemctl restart study-app

# ステータス確認
sudo systemctl status study-app
```

---

## トラブルシューティング

### アプリが起動しない

```bash
# ログを確認
sudo journalctl -u study-app -n 50

# 手動起動でエラー確認
cd ~/study_app
source venv/bin/activate
streamlit run app_v3.py
```

### ポートが使用中

```bash
# ポート8501を使用しているプロセスを確認
sudo lsof -i :8501

# プロセスを停止
sudo kill -9 <PID>
```

### データベースエラー

```bash
# データベースファイルの権限確認
ls -l ~/study_app/*.db

# 権限を修正
chmod 664 ~/study_app/*.db
```

---

## アクセスURL

- **直接アクセス**: `http://your-vps-ip:8501`
- **Nginx経由**: `http://your-domain.com`
- **HTTPS**: `https://your-domain.com`

---

## セキュリティ推奨事項

1. SSHポートを22番から変更する
2. SSH鍵認証を設定し、パスワード認証を無効化
3. fail2banをインストールして不正アクセスを防止
4. 定期的にシステムアップデートを実行
5. データベースの定期バックアップを設定

---

## 参考リンク

- [Hostinger VPS管理画面](https://hpanel.hostinger.com)
- [Streamlit公式ドキュメント](https://docs.streamlit.io)
- [Let's Encrypt](https://letsencrypt.org)
