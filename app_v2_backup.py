"""
診断士学習記録アプリ v2 - UI/UX改善版
資格取得コンサル × UI/UXデザイナーの視点で再設計
"""
import streamlit as st
from datetime import date, datetime, timedelta
import pyperclip
import pandas as pd

from database.init_db import init_database
from models.record import StudyRecord
from services.database import DatabaseService
from services.obsidian import ObsidianService
from services.tweet import TweetService
from utils.phase import get_current_phase
from utils.stats import (
    calculate_days_until_exam,
    calculate_required_daily_pace,
    calculate_streak,
    calculate_weekly_stats,
    calculate_monthly_stats,
    calculate_subject_progress,
    get_achievement_message
)


# ページ設定
st.set_page_config(
    page_title="診断士学習記録",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# カスタムCSS
st.markdown("""
<style>
    .big-metric {
        font-size: 2.5rem !important;
        font-weight: 700 !important;
        margin: 0 !important;
    }
    .achievement-banner {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        text-align: center;
        font-size: 1.2rem;
        font-weight: 600;
    }
    .metric-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .streak-badge {
        display: inline-block;
        background: #ff6b6b;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: 600;
        margin: 0.5rem 0;
    }
    .phase-badge {
        display: inline-block;
        background: #4ecdc4;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: 600;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)


def init_app():
    """アプリ初期化"""
    init_database()

    if 'db_service' not in st.session_state:
        st.session_state.db_service = DatabaseService()
    if 'obsidian_service' not in st.session_state:
        st.session_state.obsidian_service = ObsidianService()
    if 'tweet_service' not in st.session_state:
        st.session_state.tweet_service = TweetService()


def main():
    """メイン画面"""
    init_app()

    # タイトル
    st.title("📚 診断士学習記録ダッシュボード")

    # タブ切り替え（ダッシュボードを最初に）
    tab1, tab2, tab3, tab4 = st.tabs(["🏠 ダッシュボード", "✏️ 今日の記録", "📊 分析", "⚙️ 設定"])

    with tab1:
        show_dashboard()

    with tab2:
        show_daily_input()

    with tab3:
        show_analytics()

    with tab4:
        show_settings()


def show_dashboard():
    """ダッシュボード画面"""
    # データ取得
    stats = st.session_state.db_service.get_cumulative_stats()
    all_records = st.session_state.db_service.get_all_records()

    # 統計計算
    days_to_toukei, days_to_shindan = calculate_days_until_exam()
    required_pace = calculate_required_daily_pace(
        stats.shindan_total,
        stats.shindan_goal,
        days_to_shindan
    )
    streak = calculate_streak(all_records)
    weekly_stats = calculate_weekly_stats(all_records)
    monthly_stats = calculate_monthly_stats(all_records)
    current_phase = get_current_phase()

    # 称賛メッセージ
    achievement_msg = get_achievement_message(streak, stats.shindan_total, stats.shindan_progress)
    st.markdown(f'<div class="achievement-banner">{achievement_msg}</div>', unsafe_allow_html=True)

    # メトリクス行1: 試験日カウントダウン
    st.subheader("⏰ 試験日までのカウントダウン")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "統計検定2級",
            f"{days_to_toukei}日",
            delta="2月1日",
            delta_color="off"
        )

    with col2:
        st.metric(
            "中小企業診断士",
            f"{days_to_shindan}日",
            delta="8月上旬",
            delta_color="off"
        )

    with col3:
        st.markdown(f'<div class="streak-badge">🔥 {streak}日連続学習中</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="phase-badge">📅 {current_phase}</div>', unsafe_allow_html=True)

    st.divider()

    # メトリクス行2: 累計進捗
    st.subheader("📈 累計進捗")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 中小企業診断士")
        st.metric(
            "累計学習時間",
            f"{stats.shindan_total} h",
            delta=f"{stats.shindan_goal - stats.shindan_total}h 残り"
        )
        st.progress(stats.shindan_progress / 100)
        st.caption(f"進捗率: {stats.shindan_progress}% (目標: {stats.shindan_goal}h)")

        # 必要ペース
        st.info(f"💡 **目標達成には1日あたり {required_pace}h の学習が必要です**")

    with col2:
        st.markdown("### 統計検定2級")
        st.metric(
            "累計学習時間",
            f"{stats.toukei_total} h"
        )
        st.caption("引き続き学習を継続しましょう")

    st.divider()

    # メトリクス行3: 週次・月次サマリー
    st.subheader("📊 最近の学習状況")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 今週の学習時間")
        st.metric("診断士", f"{weekly_stats['shindan']}h")
        st.metric("統計", f"{weekly_stats['toukei']}h")
        st.metric("合計", f"{weekly_stats['total']}h", delta="今週")

    with col2:
        st.markdown("### 今月の学習時間")
        st.metric("診断士", f"{monthly_stats['shindan']}h")
        st.metric("統計", f"{monthly_stats['toukei']}h")
        st.metric("合計", f"{monthly_stats['total']}h", delta="今月")

    st.divider()

    # 科目別進捗
    st.subheader("📚 科目別進捗")
    subject_progress = calculate_subject_progress(all_records)

    if subject_progress:
        # 3列レイアウト
        cols = st.columns(3)
        subjects_list = list(subject_progress.items())

        for idx, (subject, (hours, progress)) in enumerate(subjects_list):
            col_idx = idx % 3
            with cols[col_idx]:
                # 進捗率に応じて色分け
                if progress >= 100:
                    st.success(f"**{subject}** ✅")
                elif progress >= 75:
                    st.info(f"**{subject}**")
                elif progress >= 50:
                    st.warning(f"**{subject}**")
                else:
                    st.error(f"**{subject}**")

                st.progress(min(progress / 100, 1.0))
                st.caption(f"{hours}h / 90h ({progress}%)")
    else:
        st.info("まだ科目別の学習記録がありません。記録を開始しましょう！")

    st.divider()

    # 今日の記録へのショートカット
    st.subheader("✏️ クイックアクション")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("📝 今日の記録を入力", type="primary", use_container_width=True):
            st.switch_page("app_v2.py")  # 「今日の記録」タブに切り替え（実際にはタブ2をアクティブに）

    with col2:
        if st.button("📊 詳細分析を見る", use_container_width=True):
            st.switch_page("app_v2.py")  # 「分析」タブに切り替え


def show_daily_input():
    """日次記録入力画面（改善版）"""
    st.header("✏️ 今日の学習記録")

    # 日付選択
    col1, col2 = st.columns([2, 1])
    with col1:
        target_date = st.date_input("📅 日付", value=date.today())

    with col2:
        phase = get_current_phase()
        st.info(f"**フェーズ**: {phase}")

    # 既存データ読み込み
    existing_record = st.session_state.db_service.get_record_by_date(target_date)

    # クイック入力プリセット
    st.subheader("⚡ クイック入力")
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("1時間学習", use_container_width=True):
            st.session_state['quick_shindan_time'] = 1.0

    with col2:
        if st.button("2時間学習", use_container_width=True):
            st.session_state['quick_shindan_time'] = 2.0

    with col3:
        if st.button("3時間学習", use_container_width=True):
            st.session_state['quick_shindan_time'] = 3.0

    st.divider()

    # 中小企業診断士セクション
    with st.expander("📘 中小企業診断士", expanded=True):
        col1, col2 = st.columns([1, 2])

        with col1:
            default_time = st.session_state.get('quick_shindan_time', 0.0)
            if existing_record:
                default_time = float(existing_record.shindan_time)

            shindan_time = st.number_input(
                "学習時間（h）",
                min_value=0.0,
                max_value=24.0,
                value=default_time,
                step=0.5,
                key="shindan_time"
            )

        with col2:
            subjects = st.session_state.db_service.get_subjects()
            subject_names = [s[0] for s in subjects]

            default_index = 0
            if existing_record and existing_record.shindan_subject:
                try:
                    default_index = subject_names.index(existing_record.shindan_subject)
                except ValueError:
                    pass

            shindan_subject = st.selectbox(
                "科目",
                subject_names,
                index=default_index,
                key="shindan_subject"
            )

        shindan_content = st.text_area(
            "学習内容",
            value=existing_record.shindan_content if existing_record else "",
            placeholder="例: 過去問15問 正答率70%",
            height=100,
            key="shindan_content"
        )

        shindan_issue = st.text_area(
            "課題・気づき",
            value=existing_record.shindan_issue if existing_record else "",
            placeholder="例: 固変分解の理解が必要",
            height=80,
            key="shindan_issue"
        )

    # 統計検定2級セクション
    with st.expander("📊 統計検定2級", expanded=True):
        toukei_time = st.number_input(
            "学習時間（h）",
            min_value=0.0,
            max_value=24.0,
            value=float(existing_record.toukei_time) if existing_record else 0.0,
            step=0.5,
            key="toukei_time"
        )

        toukei_content = st.text_area(
            "学習内容",
            value=existing_record.toukei_content if existing_record else "",
            placeholder="例: 推定演習 第5章",
            height=100,
            key="toukei_content"
        )

        toukei_issue = st.text_area(
            "課題・気づき",
            value=existing_record.toukei_issue if existing_record else "",
            placeholder="例: 信頼区間の計算に時間がかかる",
            height=80,
            key="toukei_issue"
        )

    st.divider()

    # 保存ボタン（大きく目立つように）
    col1, col2 = st.columns([3, 1])

    with col1:
        if st.button("💾 保存してX投稿文を生成", type="primary", use_container_width=True):
            save_and_generate_tweet(
                target_date=target_date,
                phase=phase,
                shindan_time=shindan_time,
                shindan_subject=shindan_subject,
                shindan_content=shindan_content,
                shindan_issue=shindan_issue,
                toukei_time=toukei_time,
                toukei_content=toukei_content,
                toukei_issue=toukei_issue
            )

    with col2:
        if st.button("💾 保存のみ", use_container_width=True):
            save_record_only(
                target_date=target_date,
                phase=phase,
                shindan_time=shindan_time,
                shindan_subject=shindan_subject,
                shindan_content=shindan_content,
                shindan_issue=shindan_issue,
                toukei_time=toukei_time,
                toukei_content=toukei_content,
                toukei_issue=toukei_issue
            )


def save_and_generate_tweet(
    target_date,
    phase,
    shindan_time,
    shindan_subject,
    shindan_content,
    shindan_issue,
    toukei_time,
    toukei_content,
    toukei_issue
):
    """記録を保存してX投稿文を生成"""
    record = StudyRecord(
        date=target_date,
        phase=phase,
        shindan_time=shindan_time,
        shindan_subject=shindan_subject,
        shindan_content=shindan_content,
        shindan_issue=shindan_issue,
        toukei_time=toukei_time,
        toukei_content=toukei_content,
        toukei_issue=toukei_issue
    )

    record_id = st.session_state.db_service.save_record(record)
    stats = st.session_state.db_service.get_cumulative_stats()
    file_path = st.session_state.obsidian_service.export_to_obsidian(record, stats)
    tweet_text = st.session_state.tweet_service.generate_daily_tweet(record, stats)

    try:
        pyperclip.copy(tweet_text)
        clipboard_msg = "✅ クリップボードにコピーしました"
    except:
        clipboard_msg = "⚠️ クリップボードへのコピーに失敗しました"

    st.success(f"✅ 記録を保存しました（ID: {record_id}）")
    st.success(f"✅ Obsidianファイルを出力: {file_path.name}")
    st.info(clipboard_msg)

    st.subheader("📱 X投稿文")
    st.code(tweet_text, language=None)

    if st.button("📋 投稿文を再コピー"):
        try:
            pyperclip.copy(tweet_text)
            st.success("✅ コピーしました")
        except:
            st.error("⚠️ コピーに失敗しました")


def save_record_only(
    target_date,
    phase,
    shindan_time,
    shindan_subject,
    shindan_content,
    shindan_issue,
    toukei_time,
    toukei_content,
    toukei_issue
):
    """記録のみ保存"""
    record = StudyRecord(
        date=target_date,
        phase=phase,
        shindan_time=shindan_time,
        shindan_subject=shindan_subject,
        shindan_content=shindan_content,
        shindan_issue=shindan_issue,
        toukei_time=toukei_time,
        toukei_content=toukei_content,
        toukei_issue=toukei_issue
    )

    record_id = st.session_state.db_service.save_record(record)
    stats = st.session_state.db_service.get_cumulative_stats()
    file_path = st.session_state.obsidian_service.export_to_obsidian(record, stats)

    st.success(f"✅ 記録を保存しました（ID: {record_id}）")
    st.success(f"✅ Obsidianファイルを出力: {file_path.name}")


def show_analytics():
    """分析画面"""
    st.header("📊 学習分析")

    all_records = st.session_state.db_service.get_all_records()

    if not all_records:
        st.info("まだ記録がありません")
        return

    # 学習時間推移グラフ
    st.subheader("📈 学習時間の推移")

    # DataFrameに変換
    df_data = []
    for record in all_records:
        df_data.append({
            '日付': record.date,
            '診断士': record.shindan_time,
            '統計': record.toukei_time,
            '合計': record.shindan_time + record.toukei_time
        })

    df = pd.DataFrame(df_data)
    df = df.sort_values('日付')

    # 折れ線グラフ
    st.line_chart(df.set_index('日付')[['診断士', '統計', '合計']])

    st.divider()

    # 科目別集計
    st.subheader("📚 科目別学習時間")

    subject_hours = {}
    for record in all_records:
        if record.shindan_subject and record.shindan_time > 0:
            if record.shindan_subject not in subject_hours:
                subject_hours[record.shindan_subject] = 0
            subject_hours[record.shindan_subject] += record.shindan_time

    if subject_hours:
        df_subjects = pd.DataFrame(list(subject_hours.items()), columns=['科目', '学習時間'])
        df_subjects = df_subjects.sort_values('学習時間', ascending=False)

        st.bar_chart(df_subjects.set_index('科目'))
    else:
        st.info("科目別データがありません")

    st.divider()

    # 履歴テーブル
    st.subheader("📜 学習履歴")

    for record in all_records[:10]:  # 最新10件
        with st.expander(f"{record.date.strftime('%Y年%m月%d日')} - {record.phase}"):
            col1, col2 = st.columns(2)

            with col1:
                st.markdown("**中小企業診断士**")
                st.write(f"時間: {record.shindan_time}h")
                if record.shindan_subject:
                    st.write(f"科目: {record.shindan_subject}")
                if record.shindan_content:
                    st.write(f"内容: {record.shindan_content}")

            with col2:
                st.markdown("**統計検定2級**")
                st.write(f"時間: {record.toukei_time}h")
                if record.toukei_content:
                    st.write(f"内容: {record.toukei_content}")


def show_settings():
    """設定画面"""
    st.header("⚙️ 設定")

    st.subheader("データベース")
    st.write("パス: `~/study_app/study_records.db`")

    col1, col2 = st.columns(2)
    with col1:
        all_records = st.session_state.db_service.get_all_records()
        st.metric("総記録数", f"{len(all_records)}件")

    with col2:
        stats = st.session_state.db_service.get_cumulative_stats()
        total_hours = stats.shindan_total + stats.toukei_total
        st.metric("総学習時間", f"{total_hours}h")

    st.divider()

    st.subheader("Obsidian出力先")
    obsidian_path = st.session_state.obsidian_service.vault_path
    st.code(str(obsidian_path))

    st.divider()

    st.subheader("科目マスタ")
    subjects = st.session_state.db_service.get_subjects()

    for subject_name, abbr in subjects:
        st.write(f"- {subject_name} ({abbr}) - 目標: 90h")


if __name__ == "__main__":
    main()
