"""
エッジケーステスト
"""
from datetime import date
from services.obsidian_sync import ObsidianSyncService
import re

def test_edge_cases():
    print("=== エッジケーステスト ===\n")

    sync = ObsidianSyncService()

    # 1. 正規表現パターンテスト
    print("1. 正規表現パターンテスト:")

    test_cases = [
        ("dur:: 3h subject:: 財務会計", True, 3.0, "財務会計"),
        ("dur:: 25m subject:: 統計検定", True, 0.42, "統計検定"),
        ("dur:: 1.5h subject:: 企業経営理論", True, 1.5, "企業経営理論"),
        ("dur::3h subject::財務会計", True, 3.0, "財務会計"),  # スペースなし
        ("dur:: 2h 30m subject:: 運営管理", False, None, None),  # 複合時間（未対応）
        ("dur:: 0.5h subject:: 経済学", True, 0.5, "経済学"),
        ("dur:: 90m subject:: 経営法務", True, 1.5, "経営法務"),
    ]

    for content, should_match, expected_hours, expected_subject in test_cases:
        logs = sync.parse_study_log(content)

        if should_match:
            if logs:
                actual_hours = logs[0]['duration_hours']
                actual_subject = logs[0]['subject']

                hours_match = abs(actual_hours - expected_hours) < 0.01
                subject_match = actual_subject == expected_subject

                if hours_match and subject_match:
                    print(f"   ✅ '{content}' → {actual_hours}h, {actual_subject}")
                else:
                    print(f"   ❌ '{content}' → 期待: {expected_hours}h/{expected_subject}, 実際: {actual_hours}h/{actual_subject}")
            else:
                print(f"   ❌ '{content}' → マッチなし（期待: マッチあり）")
        else:
            if not logs:
                print(f"   ✅ '{content}' → マッチなし（期待通り）")
            else:
                print(f"   ⚠️  '{content}' → 予期しないマッチ")

    print()

    # 2. 複数行テスト
    print("2. 複数行テスト:")
    multi_line = """
## 学習ログ
- dur:: 2h subject:: 財務会計
- dur:: 1h subject:: 企業経営理論
- dur:: 30m subject:: 統計検定
"""
    logs = sync.parse_study_log(multi_line)
    print(f"   抽出件数: {len(logs)}")

    if len(logs) == 3:
        print("   ✅ 3件抽出成功")
        for log in logs:
            print(f"      - {log['subject']}: {log['duration_hours']}h ({log['type']})")
    else:
        print(f"   ❌ 期待: 3件, 実際: {len(logs)}件")

    print()

    # 3. 集計テスト
    print("3. 集計テスト:")
    shindan_time, shindan_subject, toukei_time = sync.aggregate_logs_by_type(logs)

    expected_shindan = 2.0 + 1.0  # 3.0h
    expected_toukei = 0.5  # 30m = 0.5h

    shindan_ok = abs(shindan_time - expected_shindan) < 0.01
    toukei_ok = abs(toukei_time - expected_toukei) < 0.01

    if shindan_ok and toukei_ok:
        print(f"   ✅ 診断士: {shindan_time}h (期待: {expected_shindan}h)")
        print(f"   ✅ 統計検定: {toukei_time}h (期待: {expected_toukei}h)")
        print(f"   ✅ 代表科目: {shindan_subject}")
    else:
        print(f"   ❌ 診断士: {shindan_time}h (期待: {expected_shindan}h)")
        print(f"   ❌ 統計検定: {toukei_time}h (期待: {expected_toukei}h)")

    print()

    # 4. 空データテスト
    print("4. 空データテスト:")
    empty_logs = sync.parse_study_log("## 今日は勉強しませんでした")
    if len(empty_logs) == 0:
        print("   ✅ 空データの処理成功")
    else:
        print(f"   ❌ 期待: 0件, 実際: {len(empty_logs)}件")

    print()

    # 5. 不正フォーマットテスト
    print("5. 不正フォーマットテスト:")
    invalid_cases = [
        "dur: 2h subject: 財務会計",  # コロンが1つ
        "duration:: 2h subject:: 財務会計",  # durではない
        "dur:: 2 subject:: 財務会計",  # 単位なし
        "dur:: abc subject:: 財務会計",  # 数値でない
    ]

    all_passed = True
    for invalid in invalid_cases:
        result = sync.parse_study_log(invalid)
        if len(result) == 0:
            print(f"   ✅ '{invalid}' → 正しく無視")
        else:
            print(f"   ❌ '{invalid}' → 誤ってマッチ")
            all_passed = False

    print()
    print("=" * 40)
    if all_passed:
        print("全エッジケーステスト完了 ✅")
    else:
        print("一部のテストが失敗 ⚠️")
    print("=" * 40)

if __name__ == "__main__":
    test_edge_cases()
