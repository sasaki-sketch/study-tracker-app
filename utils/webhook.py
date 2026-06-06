"""
n8n Webhook連携ユーティリティ
"""
import json
import requests
from datetime import datetime, date, timedelta
from typing import Dict, Optional


# n8n Webhook URL（設定ファイルから読み込み可能に）
N8N_WEBHOOK_URL = "https://n8n.srv1080856.hstgr.cloud/webhook-test/study-log"


def send_event_to_n8n(event_data: Dict, webhook_url: Optional[str] = None) -> bool:
    """学習イベントをn8nに送信

    Args:
        event_data: イベントデータ辞書
        webhook_url: カスタムWebhook URL（Noneの場合はデフォルト使用）

    Returns:
        bool: 送信成功したらTrue
    """
    url = webhook_url or N8N_WEBHOOK_URL

    try:
        # イベントデータを整形
        payload = {
            'event_type': event_data.get('event_type'),
            'subject': event_data.get('subject'),
            'date': event_data.get('date'),
            'details': event_data.get('details', {}),
            'timestamp': datetime.now().isoformat(),
            'source': 'study_app'
        }

        # n8nに送信
        response = requests.post(
            url,
            json=payload,
            headers={'Content-Type': 'application/json'},
            timeout=5
        )

        response.raise_for_status()
        return True

    except requests.exceptions.RequestException as e:
        print(f"⚠️ Webhook送信エラー: {str(e)}")
        return False


def send_weekly_summary_to_n8n(db, webhook_url: Optional[str] = None) -> bool:
    """週次サマリーをn8nに送信

    Args:
        db: DatabaseServiceインスタンス
        webhook_url: カスタムWebhook URL

    Returns:
        bool: 送信成功したらTrue
    """
    from utils.event_stats import (
        calculate_past_exam_stats,
        calculate_material_progress_stats
    )

    url = webhook_url or N8N_WEBHOOK_URL

    try:
        # 週次統計データ取得
        today = date.today()
        week_ago = today - timedelta(days=7)

        # 過去問統計
        past_stats = calculate_past_exam_stats(db)

        # 教材統計
        material_stats = calculate_material_progress_stats(db)

        # 診断士学習時間（直近7日間）
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

        # Webhook送信用ペイロード
        payload = {
            'event_type': 'weekly_summary',
            'period': {
                'start': week_ago.strftime('%Y-%m-%d'),
                'end': today.strftime('%Y-%m-%d')
            },
            'past_exam': {
                'count': past_stats['total_count'],
                'avg_correct_rate': past_stats['avg_correct_rate'],
                'trend': past_stats['recent_trend']
            },
            'materials': {
                'total_materials': material_stats['total_materials'],
                'avg_progress': material_stats['avg_progress']
            },
            'study_time': {
                'total_hours': round(total_study_time, 1)
            },
            'timestamp': datetime.now().isoformat(),
            'source': 'study_app'
        }

        # n8nに送信
        response = requests.post(
            url,
            json=payload,
            headers={'Content-Type': 'application/json'},
            timeout=5
        )

        response.raise_for_status()
        return True

    except Exception as e:
        print(f"⚠️ 週次サマリーWebhook送信エラー: {str(e)}")
        return False


def send_daily_record_to_n8n(record_data: Dict, webhook_url: Optional[str] = None) -> bool:
    """日々の学習記録をn8nに送信

    Args:
        record_data: 日次記録データ辞書
        webhook_url: カスタムWebhook URL

    Returns:
        bool: 送信成功したらTrue
    """
    url = webhook_url or N8N_WEBHOOK_URL

    try:
        payload = {
            'event_type': 'daily_record',
            'date': record_data.get('date'),
            'phase': record_data.get('phase'),
            'shindan_time': record_data.get('shindan_time', 0),
            'shindan_subject': record_data.get('shindan_subject'),
            'toukei_time': record_data.get('toukei_time', 0),
            'timestamp': datetime.now().isoformat(),
            'source': 'study_app'
        }

        response = requests.post(
            url,
            json=payload,
            headers={'Content-Type': 'application/json'},
            timeout=5
        )

        response.raise_for_status()
        return True

    except requests.exceptions.RequestException as e:
        print(f"⚠️ 日次記録Webhook送信エラー: {str(e)}")
        return False
