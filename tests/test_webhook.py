"""
Webhook機能のテストスクリプト
"""
from datetime import date
from utils.webhook import send_event_to_n8n, send_weekly_summary_to_n8n
from services.database import DatabaseService

print("=" * 60)
print("📡 Webhook機能テスト開始")
print("=" * 60)

# テスト1: イベントWebhook送信
print("\n【テスト1】イベントWebhook送信")
print("-" * 60)

test_event_data = {
    'event_type': 'past_exam',
    'subject': 'テスト科目',
    'date': date.today().isoformat(),
    'details': {
        'exam_year': 'R5',
        'question_range': '全問',
        'correct_count': 20,
        'total_count': 25,
        'time_spent': 60
    }
}

print("送信データ:", test_event_data)
print("\n送信中...")

try:
    success = send_event_to_n8n(test_event_data)
    if success:
        print("✅ イベントWebhook送信成功！")
    else:
        print("⚠️ イベントWebhook送信失敗")
except Exception as e:
    print(f"❌ エラー発生: {str(e)}")

# テスト2: 週次サマリーWebhook送信
print("\n【テスト2】週次サマリーWebhook送信")
print("-" * 60)

try:
    db = DatabaseService()
    print("データベース接続成功")
    print("\n送信中...")

    success = send_weekly_summary_to_n8n(db)
    if success:
        print("✅ 週次サマリーWebhook送信成功！")
    else:
        print("⚠️ 週次サマリーWebhook送信失敗")
except Exception as e:
    print(f"❌ エラー発生: {str(e)}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 60)
print("テスト完了")
print("=" * 60)
print("\n💡 n8nワークフローで受信データを確認してください")
print(f"   URL: https://n8n.srv1080856.hstgr.cloud/workflow")
