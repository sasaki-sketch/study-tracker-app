"""
SNS投稿用画像生成ユーティリティ
"""
from datetime import datetime, timedelta
from io import BytesIO
from typing import Dict

from PIL import Image, ImageDraw, ImageFont


# カラーパレット
COLORS = {
    'success': '#10B981',      # 緑（合格水準）
    'warning': '#F59E0B',      # オレンジ（要努力）
    'primary': '#3B82F6',      # 青（アクセント）
    'background': '#F9FAFB',   # 明るいグレー
    'card_bg': '#FFFFFF',      # カード背景
    'text_dark': '#1F2937',    # 濃いグレー
    'text_light': '#6B7280',   # 薄いグレー
    'border': '#E5E7EB',       # ボーダー
}


def hex_to_rgb(hex_color: str) -> tuple:
    """HEXカラーコードをRGBタプルに変換"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def generate_weekly_summary_card(stats: Dict) -> BytesIO:
    """週次統計サマリーカード画像生成

    Args:
        stats: {
            'past_exam_count': 過去問実施回数,
            'avg_correct_rate': 平均正答率,
            'recent_trend': トレンド,
            'material_count': 教材数,
            'total_laps': 総周回数,
            'total_study_time': 総学習時間（診断士のみ）,
            'period_start': 集計開始日,
            'period_end': 集計終了日
        }

    Returns:
        BytesIO: PNG画像データ
    """
    # 画像サイズ（Twitter/X最適: 1200x1400）
    width, height = 1200, 1400

    # 画像作成
    img = Image.new('RGB', (width, height), hex_to_rgb(COLORS['background']))
    draw = ImageDraw.Draw(img)

    # フォント設定（システムフォント使用）
    try:
        # macOSのヒラギノフォント
        font_title = ImageFont.truetype('/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc', 80)
        font_heading = ImageFont.truetype('/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc', 60)
        font_large = ImageFont.truetype('/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc', 90)
        font_medium = ImageFont.truetype('/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc', 50)
        font_small = ImageFont.truetype('/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc', 40)
    except OSError:
        # フォールバック（デフォルトフォント）
        font_title = ImageFont.load_default()
        font_heading = ImageFont.load_default()
        font_large = ImageFont.load_default()
        font_medium = ImageFont.load_default()
        font_small = ImageFont.load_default()

    # カード背景
    card_padding = 60
    card_x = card_padding
    card_y = card_padding
    card_width = width - (card_padding * 2)
    card_height = height - (card_padding * 2)

    draw.rounded_rectangle(
        [(card_x, card_y), (card_x + card_width, card_y + card_height)],
        radius=30,
        fill=hex_to_rgb(COLORS['card_bg'])
    )

    # タイトル
    y_offset = card_y + 80
    title_text = "📊 週次学習記録"
    draw.text((width // 2, y_offset), title_text,
              fill=hex_to_rgb(COLORS['text_dark']),
              font=font_title,
              anchor='mm')

    # 期間表示
    y_offset += 100
    period_text = f"{stats['period_start']} 〜 {stats['period_end']}"
    draw.text((width // 2, y_offset), period_text,
              fill=hex_to_rgb(COLORS['text_light']),
              font=font_small,
              anchor='mm')

    # 区切り線
    y_offset += 70
    line_margin = 100
    draw.line([(card_x + line_margin, y_offset),
               (card_x + card_width - line_margin, y_offset)],
              fill=hex_to_rgb(COLORS['border']),
              width=3)

    # 過去問セクション
    y_offset += 90
    draw.text((width // 2, y_offset), "📖 過去問演習",
              fill=hex_to_rgb(COLORS['text_dark']),
              font=font_heading,
              anchor='mm')

    # 過去問回数
    y_offset += 110
    past_exam_text = f"{stats['past_exam_count']}回"
    draw.text((width // 2, y_offset), past_exam_text,
              fill=hex_to_rgb(COLORS['primary']),
              font=font_large,
              anchor='mm')

    # 平均正答率
    y_offset += 120
    correct_rate = stats['avg_correct_rate']
    rate_color = COLORS['success'] if correct_rate >= 70 else COLORS['warning']
    rate_text = f"平均正答率: {correct_rate}%"
    draw.text((width // 2, y_offset), rate_text,
              fill=hex_to_rgb(rate_color),
              font=font_medium,
              anchor='mm')

    # トレンド表示
    y_offset += 80
    trend_map = {
        'improving': '↗️ 改善中',
        'stable': '→ 安定',
        'declining': '↘️ 要改善'
    }
    trend_text = trend_map.get(stats['recent_trend'], '→ 安定')
    draw.text((width // 2, y_offset), trend_text,
              fill=hex_to_rgb(COLORS['text_light']),
              font=font_small,
              anchor='mm')

    # 区切り線
    y_offset += 80
    draw.line([(card_x + line_margin, y_offset),
               (card_x + card_width - line_margin, y_offset)],
              fill=hex_to_rgb(COLORS['border']),
              width=3)

    # 教材セクション
    y_offset += 90
    draw.text((width // 2, y_offset), "📚 教材周回",
              fill=hex_to_rgb(COLORS['text_dark']),
              font=font_heading,
              anchor='mm')

    # 教材数と周回数
    y_offset += 110
    material_text = f"{stats['material_count']}冊"
    draw.text((width // 2 - 150, y_offset), material_text,
              fill=hex_to_rgb(COLORS['primary']),
              font=font_large,
              anchor='mm')

    lap_text = f"{stats['total_laps']}周"
    draw.text((width // 2 + 150, y_offset), lap_text,
              fill=hex_to_rgb(COLORS['primary']),
              font=font_large,
              anchor='mm')

    # 区切り線
    y_offset += 140
    draw.line([(card_x + line_margin, y_offset),
               (card_x + card_width - line_margin, y_offset)],
              fill=hex_to_rgb(COLORS['border']),
              width=3)

    # 総学習時間
    y_offset += 90
    draw.text((width // 2, y_offset), "⏱ 総学習時間",
              fill=hex_to_rgb(COLORS['text_dark']),
              font=font_heading,
              anchor='mm')

    y_offset += 110
    time_text = f"{stats['total_study_time']:.1f}時間"
    draw.text((width // 2, y_offset), time_text,
              fill=hex_to_rgb(COLORS['primary']),
              font=font_large,
              anchor='mm')

    # フッター（ハッシュタグ）
    y_offset = card_y + card_height - 100
    footer_text = "#中小企業診断士 #勉強垢"
    draw.text((width // 2, y_offset), footer_text,
              fill=hex_to_rgb(COLORS['text_light']),
              font=font_small,
              anchor='mm')

    # BytesIOに保存
    output = BytesIO()
    img.save(output, format='PNG')
    output.seek(0)

    return output


def get_weekly_stats(db) -> Dict:
    """週次統計データ取得（直近7日間）

    Args:
        db: DatabaseServiceインスタンス

    Returns:
        統計データ辞書
    """
    from datetime import date
    from utils.event_stats import (
        calculate_past_exam_stats,
        calculate_material_progress_stats
    )

    # 直近7日間のイベントのみ対象
    # ※現在の実装では全期間のデータを使用しているが、
    # 将来的に期間フィルタリングを追加する場合はここを修正

    past_stats = calculate_past_exam_stats(db)
    material_stats = calculate_material_progress_stats(db)

    # 診断士の学習時間取得（直近7日間）
    today = date.today()
    week_ago = today - timedelta(days=7)

    with db.get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT COALESCE(SUM(shindan_time), 0) as total_time
            FROM records
            WHERE phase != '関連資格'
              AND date >= ?
              AND date <= ?
        ''', (week_ago.isoformat(), today.isoformat()))

        row = cursor.fetchone()
        total_study_time = row['total_time']

    return {
        'past_exam_count': past_stats['total_count'],
        'avg_correct_rate': past_stats['avg_correct_rate'],
        'recent_trend': past_stats['recent_trend'],
        'material_count': material_stats['total_materials'],
        'total_laps': sum([1 for _ in range(material_stats['total_materials'])]),  # 簡易計算
        'total_study_time': total_study_time,
        'period_start': week_ago.strftime('%m/%d'),
        'period_end': today.strftime('%m/%d')
    }
