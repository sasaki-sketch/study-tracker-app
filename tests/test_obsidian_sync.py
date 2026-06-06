"""
Obsidian同期機能テストスクリプト
"""
from datetime import date
from services.obsidian_sync import ObsidianSyncService

def test_sync():
    print("=== Obsidian同期機能テスト ===\n")

    sync_service = ObsidianSyncService()

    # 1. 利用可能なノート確認
    print("1. 利用可能なデイリーノート:")
    available_dates = sync_service.get_available_daily_notes()
    for d in available_dates:
        print(f"   - {d.isoformat()}")
    print()

    # 2. 単一日付の同期テスト
    test_date = date(2026, 1, 2)
    print(f"2. {test_date.isoformat()}の同期テスト:")
    success, message = sync_service.sync_daily_note(test_date)

    if success:
        print(f"   ✅ {message}")
    else:
        print(f"   ❌ {message}")
    print()

    # 3. データベース確認
    print("3. データベース確認:")
    from services.database import DatabaseService
    db = DatabaseService()
    record = db.get_record_by_date(test_date)

    if record:
        print(f"   日付: {record.date}")
        print(f"   フェーズ: {record.phase}")
        print(f"   診断士時間: {record.shindan_time}h")
        print(f"   診断士科目: {record.shindan_subject}")
        print(f"   統計検定時間: {record.toukei_time}h")
    else:
        print("   ⚠️ レコードが見つかりません")

if __name__ == "__main__":
    test_sync()
