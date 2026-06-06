"""
アプリコンポーネントのテストスクリプト
"""
from datetime import date
from services.database import DatabaseService
from services.obsidian import ObsidianService
from services.tweet import TweetService
from models.record import StudyRecord
from utils.phase import get_current_phase


def test_basic_workflow():
    """基本的なワークフローをテスト"""
    print("=" * 60)
    print("診断士学習記録アプリ - テスト実行")
    print("=" * 60)

    # サービス初期化
    db_service = DatabaseService()
    obsidian_service = ObsidianService()
    tweet_service = TweetService()

    # テストデータ作成
    print("\n[1] テストレコード作成...")
    test_record = StudyRecord(
        date=date.today(),
        phase=get_current_phase(),
        shindan_time=3.0,
        shindan_subject="財務会計",
        shindan_content="過去問15問 正答率70%",
        shindan_issue="固変分解の理解が必要",
        toukei_time=1.0,
        toukei_content="推定演習",
        toukei_issue="信頼区間の計算"
    )
    print(f"  日付: {test_record.date}")
    print(f"  フェーズ: {test_record.phase}")
    print(f"  診断士: {test_record.shindan_time}h ({test_record.shindan_subject})")
    print(f"  統計: {test_record.toukei_time}h")

    # データベースに保存
    print("\n[2] データベースに保存...")
    record_id = db_service.save_record(test_record)
    print(f"  ✅ 保存成功 (ID: {record_id})")

    # 累計統計取得
    print("\n[3] 累計統計を取得...")
    stats = db_service.get_cumulative_stats()
    print(f"  診断士累計: {stats.shindan_total}h / {stats.shindan_goal}h ({stats.shindan_progress}%)")
    print(f"  統計累計: {stats.toukei_total}h")

    # Obsidianファイル出力
    print("\n[4] Obsidianファイル出力...")
    file_path = obsidian_service.export_to_obsidian(test_record, stats)
    print(f"  ✅ ファイル作成: {file_path}")

    # X投稿文生成
    print("\n[5] X投稿文生成...")
    tweet_text = tweet_service.generate_daily_tweet(test_record, stats)
    print("  ✅ 投稿文:")
    print("-" * 60)
    print(tweet_text)
    print("-" * 60)

    # 履歴確認
    print("\n[6] 全記録を取得...")
    all_records = db_service.get_all_records()
    print(f"  ✅ 全{len(all_records)}件の記録が存在")

    print("\n" + "=" * 60)
    print("✅ すべてのテストが正常に完了しました！")
    print("=" * 60)


if __name__ == "__main__":
    test_basic_workflow()
