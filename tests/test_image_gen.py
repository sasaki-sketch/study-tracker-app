"""
画像生成機能のテストスクリプト
"""
from utils.image_generator import generate_weekly_summary_card

# テストデータ
test_stats = {
    'past_exam_count': 5,
    'avg_correct_rate': 72.5,
    'recent_trend': 'improving',
    'material_count': 3,
    'total_laps': 8,
    'total_study_time': 12.5,
    'period_start': '12/27',
    'period_end': '01/03'
}

print("画像生成テスト開始...")
try:
    image_bytes = generate_weekly_summary_card(test_stats)

    # ファイルに保存
    with open('/Users/sasaki/study_app/test_output.png', 'wb') as f:
        f.write(image_bytes.getvalue())

    print("✅ 画像生成成功！")
    print("📁 保存先: /Users/sasaki/study_app/test_output.png")

except Exception as e:
    print(f"❌ エラー発生: {str(e)}")
    import traceback
    traceback.print_exc()
