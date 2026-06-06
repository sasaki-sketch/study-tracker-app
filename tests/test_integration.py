"""
統合テストスクリプト
全体の機能が正常に動作することを確認
"""
from services.database import DatabaseService

def test_integration():
    print("=== 統合テスト ===\n")

    db = DatabaseService()

    # 1. 目標時間の確認
    print("1. 目標時間の確認:")
    stats = db.get_cumulative_stats()
    print(f"   診断士総目標: {stats.shindan_goal}h")
    assert stats.shindan_goal == 770.0, "目標時間が770hでありません"
    print("   ✅ 正常\n")

    # 2. 2次試験科目の目標時間確認
    print("2. 2次試験科目の目標時間:")
    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT name, target_hours FROM subjects WHERE category = '2次試験'
    ''')
    second_exam_subjects = cursor.fetchall()
    conn.close()

    total_second = 0
    for subject in second_exam_subjects:
        print(f"   {subject['name']}: {subject['target_hours']}h")
        assert subject['target_hours'] == 50.0, f"{subject['name']}が50hでありません"
        total_second += subject['target_hours']

    print(f"   合計: {total_second}h")
    assert total_second == 200.0, "2次試験合計が200hでありません"
    print("   ✅ 正常\n")

    # 3. 関連資格の除外確認
    print("3. 関連資格の除外確認:")
    print(f"   診断士累計: {stats.shindan_total}h (関連資格を除く)")
    print(f"   進捗率: {stats.shindan_progress}%")

    # データベースの実際の記録を確認
    conn2 = db.get_connection()
    cursor2 = conn2.cursor()
    cursor2.execute('''
        SELECT SUM(shindan_time) as total FROM records WHERE phase = '関連資格'
    ''')
    related_total = cursor2.fetchone()['total'] or 0
    cursor2.execute('''
        SELECT SUM(shindan_time) as total FROM records WHERE phase != '関連資格'
    ''')
    shindan_only_total = cursor2.fetchone()['total'] or 0
    conn2.close()

    print(f"   関連資格の学習時間: {related_total}h (除外済み)")
    print(f"   診断士のみ: {shindan_only_total}h")
    assert stats.shindan_total == shindan_only_total, "関連資格が正しく除外されていません"
    print("   ✅ 正常\n")

    # 4. Obsidian同期機能の確認
    print("4. Obsidian同期機能:")
    from services.obsidian_sync import ObsidianSyncService
    sync_service = ObsidianSyncService()
    available_dates = sync_service.get_available_daily_notes()
    print(f"   利用可能なデイリーノート: {len(available_dates)}件")
    for d in available_dates:
        print(f"     - {d.isoformat()}")
    print("   ✅ 正常\n")

    # 5. 科目別進捗の確認
    print("5. 科目別進捗:")
    conn3 = db.get_connection()
    cursor3 = conn3.cursor()
    cursor3.execute('''
        SELECT name, target_hours FROM subjects WHERE category = '1次試験'
    ''')
    first_exam_subjects = cursor3.fetchall()
    conn3.close()

    total_first = sum(s['target_hours'] for s in first_exam_subjects)
    print(f"   1次試験科目数: {len(first_exam_subjects)}科目")
    print(f"   1次試験合計目標: {total_first}h")
    assert total_first == 570.0, "1次試験合計が570hでありません"
    print("   ✅ 正常\n")

    print("=" * 40)
    print("全テスト完了 ✅")
    print("=" * 40)

if __name__ == "__main__":
    test_integration()
