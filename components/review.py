"""
週次・月次レビュー画面コンポーネント
"""
import streamlit as st
import pandas as pd
from datetime import date, datetime, timedelta
from urllib.parse import quote
import pyperclip

from services.database import DatabaseService
from services.tweet import TweetService
from utils.subjects import format_subject_with_emoji
from components.tweet_char_counter import show_char_counter


def show_weekly_review():
    """週次レビュー画面"""
    st.markdown("### 📅 今週の振り返り")
    st.caption("週単位で学習状況を確認し、投稿文を生成できます")

    db_service = DatabaseService()

    # 今週の開始日・終了日を計算（月曜始まり）
    today = date.today()
    weekday = today.weekday()  # 0=月曜, 6=日曜
    week_start = today - timedelta(days=weekday)
    week_end = week_start + timedelta(days=6)

    # 日付範囲セレクター
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input(
            "開始日（月曜）",
            value=week_start,
            key="weekly_start"
        )
    with col2:
        end_date = st.date_input(
            "終了日（日曜）",
            value=week_end,
            key="weekly_end"
        )

    # 期間内のレコードを取得
    all_records = db_service.get_all_records()

    # 期間でフィルタリング
    period_records = [
        r for r in all_records
        if start_date <= r.date <= end_date and r.phase != '関連資格'
    ]

    # 統計計算
    weekly_stats = {
        'total_shindan': sum(r.shindan_time for r in period_records),
        'total_toukei': sum(r.toukei_time for r in period_records),
        'subject_hours': {}
    }

    # 科目別集計
    for record in period_records:
        if record.shindan_time > 0 and record.shindan_subject:
            subject = record.shindan_subject
            weekly_stats['subject_hours'][subject] = weekly_stats['subject_hours'].get(subject, 0) + record.shindan_time

    # サマリーカード
    st.markdown("### 📊 週間サマリー")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "診断士学習",
            f"{weekly_stats['total_shindan']}h",
            delta=f"{weekly_stats.get('shindan_vs_last_week', 0):+.1f}h vs 前週" if 'shindan_vs_last_week' in weekly_stats else None
        )

    with col2:
        st.metric(
            "統計検定学習",
            f"{weekly_stats['total_toukei']}h",
            delta=f"{weekly_stats.get('toukei_vs_last_week', 0):+.1f}h vs 前週" if 'toukei_vs_last_week' in weekly_stats else None
        )

    with col3:
        total_hours = weekly_stats['total_shindan'] + weekly_stats['total_toukei']
        st.metric(
            "合計学習時間",
            f"{total_hours}h",
            delta=f"1日平均 {total_hours/7:.1f}h"
        )

    # 科目別詳細
    if weekly_stats['subject_hours']:
        st.markdown("### 📚 科目別内訳")

        # DataFrameに変換
        subject_data = []
        for subject, hours in sorted(weekly_stats['subject_hours'].items(), key=lambda x: x[1], reverse=True):
            subject_data.append({
                '科目': format_subject_with_emoji(subject),
                '学習時間': f"{hours}h",
                '割合': f"{(hours/weekly_stats['total_shindan']*100):.1f}%" if weekly_stats['total_shindan'] > 0 else "0%"
            })

        df = pd.DataFrame(subject_data)
        st.dataframe(df, use_container_width=True, hide_index=True)

        # 棒グラフ
        chart_data = pd.DataFrame({
            '科目': [item['科目'] for item in subject_data[:5]],  # 上位5科目
            '時間': [float(item['学習時間'].replace('h', '')) for item in subject_data[:5]]
        })
        st.bar_chart(chart_data.set_index('科目'))

    # X投稿文生成
    st.markdown("---")
    st.markdown("### 🐦 週次投稿文を生成")

    if st.button("📱 週次投稿文を生成", key="generate_weekly_tweet", type="primary", use_container_width=True):
        # フェーズを取得（最新の記録から）
        records = db_service.get_recent_records(limit=1)
        phase = records[0].phase if records else "基礎固め期"

        tweet_text = TweetService.generate_weekly_tweet(
            weekly_stats=weekly_stats['subject_hours'],
            total_shindan=weekly_stats['total_shindan'],
            total_toukei=weekly_stats['total_toukei'],
            phase=phase
        )

        st.text_area(
            "生成された投稿文",
            value=tweet_text,
            height=250,
            key="weekly_tweet_preview"
        )

        # 文字数カウント
        show_char_counter(tweet_text)

        # アクションボタン
        col1, col2 = st.columns(2)
        with col1:
            tweet_url = f"https://x.com/intent/tweet?text={quote(tweet_text)}"
            st.link_button("🐦 Xで投稿", tweet_url, use_container_width=True)
        with col2:
            if st.button("📋 コピー", key="copy_weekly_tweet", use_container_width=True):
                try:
                    pyperclip.copy(tweet_text)
                    st.toast("✅ コピーしました！", icon="✅")
                except (pyperclip.PyperclipException, Exception) as e:
                    st.error(f"⚠️ コピーに失敗: {type(e).__name__}")


def show_monthly_review():
    """月次レビュー画面"""
    st.markdown("### 📆 今月の振り返り")
    st.caption("月単位で学習状況を確認し、投稿文を生成できます")

    db_service = DatabaseService()

    # 今月の開始日・終了日
    today = date.today()
    month_start = date(today.year, today.month, 1)

    # 月末日を計算
    if today.month == 12:
        month_end = date(today.year, 12, 31)
    else:
        month_end = date(today.year, today.month + 1, 1) - timedelta(days=1)

    # 月選択
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input(
            "開始日",
            value=month_start,
            key="monthly_start"
        )
    with col2:
        end_date = st.date_input(
            "終了日",
            value=month_end,
            key="monthly_end"
        )

    # 期間内のレコードを取得
    all_records = db_service.get_all_records()

    # 期間でフィルタリング
    period_records = [
        r for r in all_records
        if start_date <= r.date <= end_date and r.phase != '関連資格'
    ]

    # 統計計算
    monthly_stats = {
        'total_shindan': sum(r.shindan_time for r in period_records),
        'total_toukei': sum(r.toukei_time for r in period_records),
        'subject_hours': {}
    }

    # 科目別集計
    for record in period_records:
        if record.shindan_time > 0 and record.shindan_subject:
            subject = record.shindan_subject
            monthly_stats['subject_hours'][subject] = monthly_stats['subject_hours'].get(subject, 0) + record.shindan_time

    cumulative_stats = db_service.get_cumulative_stats()

    # サマリーカード
    st.markdown("### 📊 月間サマリー")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "診断士学習",
            f"{monthly_stats['total_shindan']}h",
            delta=f"累計 {cumulative_stats.shindan_total}h"
        )

    with col2:
        st.metric(
            "統計検定学習",
            f"{monthly_stats['total_toukei']}h",
            delta=f"累計 {cumulative_stats.toukei_total}h"
        )

    with col3:
        total_hours = monthly_stats['total_shindan'] + monthly_stats['total_toukei']
        days_in_period = (end_date - start_date).days + 1
        st.metric(
            "合計学習時間",
            f"{total_hours}h",
            delta=f"1日平均 {total_hours/days_in_period:.1f}h"
        )

    with col4:
        st.metric(
            "目標達成率",
            f"{cumulative_stats.shindan_progress:.1f}%",
            delta=f"{cumulative_stats.shindan_total}/{cumulative_stats.shindan_goal}h"
        )

    # 科目別詳細
    if monthly_stats['subject_hours']:
        st.markdown("### 📚 科目別学習時間")

        # DataFrameに変換
        subject_data = []
        for subject, hours in sorted(monthly_stats['subject_hours'].items(), key=lambda x: x[1], reverse=True):
            subject_data.append({
                '科目': format_subject_with_emoji(subject),
                '学習時間': f"{hours}h",
                '割合': f"{(hours/monthly_stats['total_shindan']*100):.1f}%" if monthly_stats['total_shindan'] > 0 else "0%"
            })

        df = pd.DataFrame(subject_data)

        # 2カラムレイアウト
        col_table, col_chart = st.columns([1, 1])

        with col_table:
            st.dataframe(df, use_container_width=True, hide_index=True)

        with col_chart:
            # 棒グラフ
            chart_data = pd.DataFrame({
                '科目': [item['科目'] for item in subject_data],
                '時間': [float(item['学習時間'].replace('h', '')) for item in subject_data]
            })
            st.bar_chart(chart_data.set_index('科目'))

    # X投稿文生成
    st.markdown("---")
    st.markdown("### 🐦 月次投稿文を生成")

    if st.button("📱 月次投稿文を生成", key="generate_monthly_tweet", type="primary", use_container_width=True):
        # フェーズを取得
        records = db_service.get_recent_records(limit=1)
        phase = records[0].phase if records else "基礎固め期"

        tweet_text = TweetService.generate_monthly_tweet(
            monthly_stats=monthly_stats['subject_hours'],
            total_shindan=monthly_stats['total_shindan'],
            total_toukei=monthly_stats['total_toukei'],
            cumulative_shindan=cumulative_stats.shindan_total,
            shindan_goal=cumulative_stats.shindan_goal,
            progress=cumulative_stats.shindan_progress,
            phase=phase
        )

        st.text_area(
            "生成された投稿文",
            value=tweet_text,
            height=300,
            key="monthly_tweet_preview"
        )

        # 文字数カウント
        show_char_counter(tweet_text)

        # アクションボタン
        col1, col2 = st.columns(2)
        with col1:
            tweet_url = f"https://x.com/intent/tweet?text={quote(tweet_text)}"
            st.link_button("🐦 Xで投稿", tweet_url, use_container_width=True)
        with col2:
            if st.button("📋 コピー", key="copy_monthly_tweet", use_container_width=True):
                try:
                    pyperclip.copy(tweet_text)
                    st.toast("✅ コピーしました！", icon="✅")
                except (pyperclip.PyperclipException, Exception) as e:
                    st.error(f"⚠️ コピーに失敗: {type(e).__name__}")
