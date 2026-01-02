"""
診断士学習記録アプリ v3 - ロードマップ&目標vs実績追加版
資格取得コンサル × UI/UXデザイナーの視点で再設計
"""
import streamlit as st
from datetime import date, datetime, timedelta
import pyperclip
import pandas as pd
from urllib.parse import quote

from database.init_db import init_database
from models.record import StudyRecord
from services.database import DatabaseService
from services.obsidian import ObsidianService
from services.obsidian_sync import ObsidianSyncService
from services.tweet import TweetService
from utils.phase import get_current_phase
from utils.stats import (
    calculate_days_until_exam,
    calculate_required_daily_pace,
    calculate_streak,
    calculate_weekly_stats,
    calculate_monthly_stats,
    calculate_subject_progress
)
from utils.quotes import get_daily_quote
from components.roadmap import show_roadmap, show_goal_vs_actual, show_learning_journey_summary
from components.subjects import show_subject_progress_by_category
from components.review import show_weekly_review, show_monthly_review
from components.tweet_char_counter import show_char_counter


# 科目絵文字マッピング（utils.subjectsからインポート）
from utils.subjects import SUBJECT_EMOJI_MAP

# ページ設定（モバイル最適化）
st.set_page_config(
    page_title="診断士学習記録",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="auto",  # モバイルでは自動的に閉じる
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': "# 診断士学習記録アプリ v3\n中小企業診断士・統計検定2級の学習進捗を管理するアプリです。"
    }
)

# カスタムCSS（モバイル対応含む）
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

    /* モバイル対応レスポンシブCSS */
    @media only screen and (max-width: 768px) {
        /* メトリクスのフォントサイズを調整 */
        .big-metric {
            font-size: 1.8rem !important;
        }

        /* バナーのパディング削減 */
        .achievement-banner {
            padding: 1rem;
            font-size: 1rem;
        }

        /* カードのパディング削減 */
        .metric-card {
            padding: 1rem;
        }

        /* Streamlitのカラムを縦積みに */
        [data-testid="column"] {
            width: 100% !important;
            flex: 1 1 100% !important;
            min-width: 100% !important;
        }

        /* ボタンのタッチターゲットサイズを拡大 */
        .stButton > button {
            min-height: 44px !important;
            font-size: 1rem !important;
            padding: 0.75rem 1.5rem !important;
        }

        /* フォーム入力のタッチターゲットサイズを拡大 */
        input, select, textarea {
            min-height: 44px !important;
            font-size: 16px !important; /* iOS Safari ズーム防止 */
        }

        /* タブのフォントサイズ調整 */
        .stTabs [data-baseweb="tab-list"] button {
            font-size: 0.9rem !important;
            padding: 0.5rem 0.75rem !important;
        }

        /* メトリクスのラベルサイズ調整 */
        [data-testid="stMetricLabel"] {
            font-size: 0.85rem !important;
        }

        /* メトリクスの値のサイズ調整 */
        [data-testid="stMetricValue"] {
            font-size: 1.5rem !important;
        }

        /* サイドバーの幅調整 */
        [data-testid="stSidebar"] {
            min-width: 280px !important;
        }

        /* テーブルをスクロール可能に */
        .dataframe-container {
            overflow-x: auto !important;
        }
    }

    /* 小型スマートフォン対応 (320px-480px) */
    @media only screen and (max-width: 480px) {
        .big-metric {
            font-size: 1.5rem !important;
        }

        .achievement-banner {
            padding: 0.75rem;
            font-size: 0.9rem;
        }

        [data-testid="stMetricValue"] {
            font-size: 1.2rem !important;
        }

        /* タブを縦積みに */
        .stTabs [data-baseweb="tab-list"] {
            flex-wrap: wrap !important;
        }

        .stTabs [data-baseweb="tab-list"] button {
            font-size: 0.8rem !important;
            padding: 0.4rem 0.6rem !important;
        }
    }

    /* タブレット対応 (768px-1024px) */
    @media only screen and (min-width: 769px) and (max-width: 1024px) {
        .big-metric {
            font-size: 2rem !important;
        }

        [data-testid="column"] {
            min-width: 45% !important;
        }
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

    # サイドバー：最近の学習記録
    with st.sidebar:
        st.markdown("### 📜 最近の学習記録")
        st.caption("クリックで投稿文を表示")

        recent_records = st.session_state.db_service.get_recent_records(limit=5)

        if not recent_records:
            st.info("まだ学習記録がありません")
        else:
            for i, record in enumerate(recent_records):
                # カード風デザイン
                is_today = record.date == date.today()

                # 日付表示（今日なら強調）
                if is_today:
                    date_label = f"🟢 **今日** {record.date.strftime('%m/%d')}"
                else:
                    date_label = f"{record.date.strftime('%m月%d日')}"

                # 学習時間の合計を計算
                total_hours = record.shindan_time + record.toukei_time

                # サマリー行を作成
                summary_parts = []
                if record.shindan_time > 0:
                    emoji = SUBJECT_EMOJI_MAP.get(record.shindan_subject, "📚")
                    summary_parts.append(f"{emoji}{record.shindan_time}h")
                if record.toukei_time > 0:
                    summary_parts.append(f"📊{record.toukei_time}h")

                summary_text = " + ".join(summary_parts) if summary_parts else "未記録"

                # ワンライン表示でクリック可能
                if st.button(
                    f"{date_label}\n{summary_text}",
                    key=f"tweet_{record.id}",
                    use_container_width=True,
                    type="primary" if is_today else "secondary"
                ):
                    st.session_state.selected_record = record
                    st.rerun()

                # 軽い区切り（最後以外）
                if i < len(recent_records) - 1:
                    st.markdown("<br>", unsafe_allow_html=True)

    # 選択された記録の投稿文を表示（サイドバーのボタンクリック時）
    if 'selected_record' in st.session_state and st.session_state.selected_record:
        selected = st.session_state.selected_record

        # 背景色付きコンテナでモーダル風に
        st.markdown("""
        <style>
        .tweet-modal {
            background: linear-gradient(135deg, #667eea15 0%, #764ba215 100%);
            padding: 2rem;
            border-radius: 15px;
            border: 2px solid #667eea40;
            margin: 1rem 0 2rem 0;
        }
        </style>
        """, unsafe_allow_html=True)

        with st.container():
            # ヘッダー - 閉じボタンを大きく、視認性向上
            col_header, col_close = st.columns([5, 1])
            with col_header:
                st.markdown(f"## 📱 {selected.date.strftime('%Y年%m月%d日')} ({selected.phase})")
            with col_close:
                st.markdown("")  # 垂直方向の調整
                if st.button("✕ 閉じる", key="close_tweet_display", type="secondary", use_container_width=True):
                    st.session_state.selected_record = None
                    st.rerun()

            st.markdown("---")

            # 投稿文を生成
            stats = st.session_state.db_service.get_cumulative_stats()
            tweet_text = TweetService.generate_daily_tweet(selected, stats)

            # 2カラムレイアウト
            col_preview, col_actions = st.columns([2, 1])

            with col_preview:
                # 投稿文プレビュー
                st.markdown("#### 📝 投稿文プレビュー")
                st.text_area(
                    label="preview",
                    value=tweet_text,
                    height=280,
                    key="history_tweet_display",
                    label_visibility="collapsed"
                )

                # 文字数カウント
                show_char_counter(tweet_text)

            with col_actions:
                # アクションエリア
                st.markdown("#### 🎯 アクション")

                # 主要アクション（大きく）
                tweet_url = f"https://x.com/intent/tweet?text={quote(tweet_text)}"
                st.link_button(
                    "🐦 Xで投稿する",
                    tweet_url,
                    use_container_width=True,
                    type="primary"
                )

                st.markdown("")  # スペース

                # 補助アクション
                if st.button("📋 コピー", key="copy_history_tweet", use_container_width=True):
                    try:
                        pyperclip.copy(tweet_text)
                        st.toast("✅ コピーしました！", icon="✅")
                    except pyperclip.PyperclipException:
                        st.error("⚠️ クリップボードへのアクセスに失敗しました")
                        st.caption("ブラウザの設定でクリップボード機能を許可してください")
                    except Exception as e:
                        st.error(f"⚠️ 予期しないエラー: {str(e)}")

                if st.button("✨ Claude助言", key="claude_history_helper", use_container_width=True):
                    helper_prompt = f"""以下の学習記録をもとに、SNS投稿用の文章を140文字以内で簡潔に整形してください：

【学習情報】
日付: {selected.date.strftime('%Y年%m月%d日')}
フェーズ: {selected.phase}

診断士学習: {selected.shindan_time}h
科目: {selected.shindan_subject}
内容: {selected.shindan_content}
気づき: {selected.shindan_issue}

統計検定学習: {selected.toukei_time}h
内容: {selected.toukei_content}
気づき: {selected.toukei_issue}

【フォーマット要件】
- タイトル: 「M月D日 / Day X：中小企業診断士への積み上げ」
- 本文: 簡潔に、絵文字は最小限
- ハッシュタグ: 2-3個まで
- 文字数: 140文字以内厳守（改行含む）"""

                    try:
                        pyperclip.copy(helper_prompt)
                        st.toast("✅ Claudeヘルパーをコピー！", icon="✨")
                        with st.expander("📋 プロンプト確認"):
                            st.code(helper_prompt, language=None)
                    except (pyperclip.PyperclipException, Exception) as e:
                        st.error(f"⚠️ コピーに失敗しました: {type(e).__name__}")

                # 学習詳細
                st.markdown("---")
                st.markdown("#### 📊 学習詳細")
                if selected.shindan_time > 0:
                    st.metric("診断士", f"{selected.shindan_time}h", delta=selected.shindan_subject)
                if selected.toukei_time > 0:
                    st.metric("統計検定", f"{selected.toukei_time}h")

            st.markdown("---")

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


def show_daily_mission(stats, days_to_toukei):
    """今日のミッション - 最優先タスク表示"""
    st.markdown("### 🎯 今日のミッション")

    # 今日の学習記録を取得
    today_record = st.session_state.db_service.get_record_by_date(date.today())

    # 今日の実績
    toukei_today = today_record.toukei_time if today_record else 0.0
    shindan_today = today_record.shindan_time if today_record else 0.0

    # 目標時間を動的に計算（残り日数から逆算）
    # 統計検定: 2026/2/1試験まで
    # 診断士: 2026/8/5試験まで
    toukei_exam_date = date(2026, 2, 1)
    shindan_exam_date = date(2026, 8, 5)

    toukei_days_remaining = max((toukei_exam_date - date.today()).days, 1)
    shindan_days_remaining = max((shindan_exam_date - date.today()).days, 1)

    # 残り時間から1日あたりの目標を計算
    toukei_remaining_hours = max(stats.toukei_goal - stats.toukei_total, 0)
    shindan_remaining_hours = max(stats.shindan_goal - stats.shindan_total, 0)

    # フェーズ別に1日目標を計算
    if date.today() < toukei_exam_date:
        # 統計検定試験前: 統計優先(合計3h/日)
        toukei_goal_daily = min(round(toukei_remaining_hours / toukei_days_remaining, 1), 2.5)
        shindan_goal_daily = 0.5
    elif date.today() < shindan_exam_date:
        # 1次試験対策期間(統計試験後〜1次試験前): 診断士1次のみ(3h/日)
        toukei_goal_daily = 0
        shindan_1st_remaining = 600.0 - stats.shindan_total  # TODO: 1次と2次を分けて記録する必要あり
        shindan_days_to_1st = max((shindan_exam_date - date.today()).days, 1)
        shindan_goal_daily = min(round(shindan_1st_remaining / shindan_days_to_1st, 1), 3.0)
    else:
        # 2次試験対策期間(1次試験後〜2次試験前): 診断士2次のみ(3h/日)
        toukei_goal_daily = 0
        shindan_2nd_remaining = 170.0  # 2次試験対策時間
        shindan_days_to_2nd = max((date(2026, 10, 25) - date.today()).days, 1)
        shindan_goal_daily = min(round(shindan_2nd_remaining / shindan_days_to_2nd, 1), 3.0)

    total_goal_daily = round(toukei_goal_daily + shindan_goal_daily, 1)

    # プログレス計算
    toukei_progress = min((toukei_today / toukei_goal_daily) * 100, 100) if toukei_goal_daily > 0 else 0
    shindan_progress = min((shindan_today / shindan_goal_daily) * 100, 100) if shindan_goal_daily > 0 else 0

    # カードデザイン
    st.markdown(f"""<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 2rem; border-radius: 15px; box-shadow: 0 8px 16px rgba(0,0,0,0.2); margin-bottom: 1rem;">
        <div style="color: white; font-size: 1.1rem; font-weight: 600; margin-bottom: 1.5rem;">📅 {date.today().strftime('%Y年%m月%d日')} の学習目標</div>
        <div style="background: rgba(255, 107, 107, 0.95); padding: 1.5rem; border-radius: 12px; margin-bottom: 1rem; border-left: 5px solid #ff4757;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.8rem;">
                <div>
                    <div style="color: white; font-size: 1.3rem; font-weight: 700;">📊 統計検定2級</div>
                    <div style="color: rgba(255,255,255,0.9); font-size: 0.9rem; margin-top: 0.3rem;">⚠️ 試験まで残り {days_to_toukei} 日</div>
                </div>
                <div style="text-align: right;">
                    <div style="color: white; font-size: 2rem; font-weight: 700;">{toukei_today:.1f}h / {toukei_goal_daily}h</div>
                </div>
            </div>
            <div style="background: rgba(255,255,255,0.3); height: 12px; border-radius: 6px; overflow: hidden;">
                <div style="background: white; height: 100%; width: {toukei_progress}%; transition: width 0.3s ease;"></div>
            </div>
        </div>
        <div style="background: rgba(78, 205, 196, 0.95); padding: 1.5rem; border-radius: 12px; border-left: 5px solid #0fb9b1;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.8rem;">
                <div>
                    <div style="color: white; font-size: 1.3rem; font-weight: 700;">📘 中小企業診断士</div>
                    <div style="color: rgba(255,255,255,0.9); font-size: 0.9rem; margin-top: 0.3rem;">💪 着実に積み上げ</div>
                </div>
                <div style="text-align: right;">
                    <div style="color: white; font-size: 2rem; font-weight: 700;">{shindan_today:.1f}h / {shindan_goal_daily}h</div>
                </div>
            </div>
            <div style="background: rgba(255,255,255,0.3); height: 12px; border-radius: 6px; overflow: hidden;">
                <div style="background: white; height: 100%; width: {shindan_progress}%; transition: width 0.3s ease;"></div>
            </div>
        </div>
        <div style="margin-top: 1.5rem; padding-top: 1.5rem; border-top: 2px solid rgba(255,255,255,0.3); color: white; text-align: center;">
            <div style="font-size: 0.9rem; opacity: 0.9; margin-bottom: 0.5rem;">今日の合計学習時間</div>
            <div style="font-size: 2.5rem; font-weight: 700;">{toukei_today + shindan_today:.1f}h / {total_goal_daily}h</div>
        </div>
    </div>""", unsafe_allow_html=True)

    # 今日の目標達成状況
    remaining = total_goal_daily - (toukei_today + shindan_today)
    if remaining > 0:
        st.info(f"💡 あと {remaining:.1f}h で今日の目標達成！「✏️ 今日の記録」タブで入力できます")
    else:
        st.success("✅ 今日の目標達成！")


def show_dashboard():
    """ダッシュボード画面（完全再設計版）"""
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

    # 今日の古典名言
    daily_quote = get_daily_quote()
    st.markdown(f"""
    <div class="achievement-banner">
        <div style="font-size: 1.3rem; font-weight: 600; margin-bottom: 0.8rem; letter-spacing: 0.05em;">
            {daily_quote['original']}
        </div>
        <div style="font-size: 1rem; opacity: 0.9; margin-bottom: 0.5rem;">
            {daily_quote['translation']}
        </div>
        <div style="font-size: 0.9rem; opacity: 0.75; text-align: right;">
            ― {daily_quote['source']}
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # 🎯 今日のミッション（最優先表示）
    show_daily_mission(stats, days_to_toukei)

    st.divider()

    # ⏰ 試験日カウントダウン & 学習ペース（コンパクト表示）
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "統計検定2級",
            f"{days_to_toukei}日",
            delta="2月1日",
            delta_color="off"
        )

    with col2:
        st.metric(
            "診断士1次試験",
            f"{days_to_shindan}日",
            delta="8月5日",
            delta_color="off"
        )

    with col3:
        st.metric(
            "必要ペース",
            f"{required_pace}h/日",
            delta="診断士目標達成まで",
            delta_color="off"
        )

    with col4:
        st.metric(
            "継続日数",
            f"{streak}日",
            delta="🔥 連続学習中",
            delta_color="off"
        )

    st.divider()

    # 📈 現在の学習進捗（累計目標 vs 実績）
    with st.expander("📈 累計進捗 - 目標 vs 実績", expanded=True):
        show_goal_vs_actual(stats, st.session_state.db_service)

    # 📊 最近の学習状況（週次・月次統合）
    with st.expander("📊 最近の学習状況（週次・月次）", expanded=False):
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("#### 📅 今週の学習時間")
            st.markdown(f"""
            <div style="background: rgba(50, 50, 50, 0.4); padding: 20px; border-radius: 12px; border-left: 4px solid #4ECDC4;">
                <div style="color: #E0E0E0; margin-bottom: 8px;">
                    📘 診断士: <strong style="color: #4ECDC4; font-size: 20px;">{weekly_stats['shindan']:.1f}h</strong>
                </div>
                <div style="color: #E0E0E0; margin-bottom: 8px;">
                    📊 統計: <strong style="color: #FF6B6B; font-size: 20px;">{weekly_stats['toukei']:.1f}h</strong>
                </div>
                <div style="color: #FFD700; margin-top: 12px; font-size: 18px;">
                    合計: <strong>{weekly_stats['total']:.1f}h</strong>
                </div>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("#### 📅 今月の学習時間")
            st.markdown(f"""
            <div style="background: rgba(50, 50, 50, 0.4); padding: 20px; border-radius: 12px; border-left: 4px solid #FF6B6B;">
                <div style="color: #E0E0E0; margin-bottom: 8px;">
                    📘 診断士: <strong style="color: #4ECDC4; font-size: 20px;">{monthly_stats['shindan']:.1f}h</strong>
                </div>
                <div style="color: #E0E0E0; margin-bottom: 8px;">
                    📊 統計: <strong style="color: #FF6B6B; font-size: 20px;">{monthly_stats['toukei']:.1f}h</strong>
                </div>
                <div style="color: #FFD700; margin-top: 12px; font-size: 18px;">
                    合計: <strong>{monthly_stats['total']:.1f}h</strong>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # レビュー機能へのクイックアクセス
    st.markdown("---")
    st.markdown("### 📋 レビュー & 投稿文生成")
    col_review1, col_review2 = st.columns(2)

    with col_review1:
        with st.expander("📅 今週の振り返り", expanded=False):
            show_weekly_review()

    with col_review2:
        with st.expander("📆 今月の振り返り", expanded=False):
            show_monthly_review()

    # その他の分析セクション
    st.markdown("---")
    st.markdown("### 📊 詳細分析")

    # 🗺️ ロードマップ
    with st.expander("🗺️ 学習ロードマップ", expanded=False):
        show_roadmap()

    # 📚 科目別進捗（1次/2次試験別）
    with st.expander("📚 科目別進捗（1次/2次試験）", expanded=False):
        show_subject_progress_by_category(st.session_state.db_service, all_records)

    # 🏆 過去の学習成果
    with st.expander("🏆 過去の学習成果", expanded=False):
        show_learning_journey_summary(st.session_state.db_service, all_records)

    # Obsidian同期モーダル
    if st.session_state.get('show_obsidian_sync', False):
        show_obsidian_sync_modal()


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

    # 中小企業診断士セクション
    with st.expander("📘 中小企業診断士", expanded=True):
        col1, col2 = st.columns([1, 2])

        with col1:
            default_time = 0.0
            if existing_record:
                default_time = float(existing_record.shindan_time)

            shindan_time = st.number_input(
                "学習時間（h）*",
                min_value=0.0,
                max_value=24.0,
                value=default_time,
                step=0.25,
                key="shindan_time",
                help="15分（0.25h）単位で入力できます"
            )

        with col2:
            subjects = st.session_state.db_service.get_subjects()
            subject_names = [s[0] for s in subjects]

            # 絵文字付き表示オプションを作成
            subject_options = []
            subject_name_map = {}  # 表示名 → 科目名のマッピング

            for subject_name in subject_names:
                emoji = SUBJECT_EMOJI_MAP.get(subject_name, "📚")
                display_name = f"{emoji} {subject_name}"
                subject_options.append(display_name)
                subject_name_map[display_name] = subject_name

            default_index = 0
            if existing_record and existing_record.shindan_subject:
                try:
                    # 既存の科目名から表示名を検索
                    for i, (display, actual) in enumerate(subject_name_map.items()):
                        if actual == existing_record.shindan_subject:
                            default_index = i
                            break
                except:
                    pass

            shindan_subject_display = st.selectbox(
                "科目*",
                subject_options,
                index=default_index,
                key="shindan_subject_select"
            )

            # 表示名から実際の科目名を取得
            shindan_subject = subject_name_map[shindan_subject_display]

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
            step=0.25,
            key="toukei_time",
            help="15分（0.25h）単位で入力できます"
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

    try:
        record_id = st.session_state.db_service.save_record(record)
        stats = st.session_state.db_service.get_cumulative_stats()
        file_path = st.session_state.obsidian_service.export_to_obsidian(record, stats)
        tweet_text = st.session_state.tweet_service.generate_daily_tweet(record, stats)
    except Exception as e:
        st.error(f"⚠️ データの保存中にエラーが発生しました: {str(e)}")
        return

    try:
        pyperclip.copy(tweet_text)
        clipboard_msg = "✅ クリップボードにコピーしました"
    except:
        clipboard_msg = "⚠️ クリップボードへのコピーに失敗しました"

    st.success(f"✅ 記録を保存しました（ID: {record_id}）")
    st.success(f"✅ Obsidianファイルを出力: {file_path.name}")
    st.info(clipboard_msg)

    st.subheader("📱 X投稿文")

    # 投稿文プレビュー
    st.text_area(
        label="投稿文プレビュー",
        value=tweet_text,
        height=200,
        key="daily_tweet_preview",
        label_visibility="collapsed"
    )

    # 文字数カウント
    show_char_counter(tweet_text)

    # X投稿リンク生成（URLエンコード）
    import urllib.parse
    encoded_text = urllib.parse.quote(tweet_text)
    twitter_url = f"https://twitter.com/intent/tweet?text={encoded_text}"

    col1, col2, col3 = st.columns(3)
    with col1:
        st.link_button("🐦 Xで投稿する", twitter_url, use_container_width=True, type="primary")
    with col2:
        if st.button("📋 投稿文を再コピー", use_container_width=True):
            try:
                pyperclip.copy(tweet_text)
                st.success("✅ コピーしました")
            except:
                st.error("⚠️ コピーに失敗しました")
    with col3:
        if st.button("✨ Claude助言", use_container_width=True):
            # Claudeヘルパープロンプトを生成
            helper_prompt = f"""以下の学習記録をもとに、SNS投稿用の文章を140文字以内で簡潔に整形してください：

【学習情報】
日付: {target_date.strftime('%Y年%m月%d日')}
フェーズ: {phase}

診断士学習: {shindan_time}h
科目: {shindan_subject}
内容: {shindan_content}
気づき: {shindan_issue}

統計検定学習: {toukei_time}h
内容: {toukei_content}
気づき: {toukei_issue}

【フォーマット要件】
- タイトル: 「M月D日 / Day X：中小企業診断士への積み上げ」
- 本文: 簡潔に、絵文字は最小限
- ハッシュタグ: 2-3個まで
- 文字数: 140文字以内厳守（改行含む）"""

            try:
                pyperclip.copy(helper_prompt)
                st.success("✅ Claudeヘルパープロンプトをコピーしました！")
                st.info("👉 Claude Codeに貼り付けて、文章の改善案をもらってください")
                with st.expander("📋 コピーされたプロンプトを確認"):
                    st.code(helper_prompt, language=None)
            except (pyperclip.PyperclipException, Exception) as e:
                st.error(f"⚠️ コピーに失敗しました: {type(e).__name__}")


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
    """記録のみ保存（バリデーション付き）"""
    # バリデーション: 合計時間チェック
    total_time = shindan_time + toukei_time

    if total_time > 24:
        st.error(f"⚠️ 1日の合計学習時間が24時間を超えています（{total_time}h）")
        st.warning("入力内容を確認してください")
        return False

    if total_time > 16:
        st.warning(f"⚠️ 1日の学習時間が{total_time}時間です。長時間学習にご注意ください。")

    # バリデーション: 0時間チェック
    if total_time == 0:
        st.warning("⚠️ 学習時間が0時間です。記録を保存しますか？")

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

    try:
        record_id = st.session_state.db_service.save_record(record)
        stats = st.session_state.db_service.get_cumulative_stats()
        file_path = st.session_state.obsidian_service.export_to_obsidian(record, stats)

        st.success(f"✅ 記録を保存しました（ID: {record_id}）")
        st.success(f"✅ Obsidianファイルを出力: {file_path.name}")
        return True
    except Exception as e:
        st.error(f"⚠️ データの保存中にエラーが発生しました: {type(e).__name__}")
        with st.expander("📋 詳細エラー情報"):
            st.code(str(e))
        return False


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


def show_obsidian_sync_modal():
    """Obsidian同期モーダル"""
    with st.container():
        st.subheader("🔄 Obsidianから同期")
        st.write("Obsidian Vaultのデイリーノートから学習記録を読み込んでデータベースに同期します。")

        # 同期サービス初期化
        sync_service = ObsidianSyncService()

        # 利用可能なデイリーノートを取得
        available_dates = sync_service.get_available_daily_notes()

        if not available_dates:
            st.warning("⚠️ Obsidian Vaultにデイリーノートが見つかりません")
            st.info(f"パス: {sync_service.daily_notes_path}")
            if st.button("閉じる"):
                st.session_state.show_obsidian_sync = False
                st.rerun()
            return

        st.success(f"✅ {len(available_dates)}件のデイリーノートが見つかりました")

        # 同期モード選択
        sync_mode = st.radio(
            "同期モード",
            ["単一日付", "期間指定"],
            horizontal=True
        )

        if sync_mode == "単一日付":
            # 日付選択
            selected_date = st.selectbox(
                "同期する日付を選択",
                available_dates,
                index=len(available_dates) - 1,  # 最新日をデフォルト
                format_func=lambda d: d.isoformat()
            )

            col1, col2 = st.columns(2)
            with col1:
                if st.button("🔄 同期実行", type="primary", use_container_width=True):
                    with st.spinner("同期中..."):
                        success, message = sync_service.sync_daily_note(selected_date)

                        if success:
                            st.success(message)
                            st.balloons()
                            # ダッシュボードを再読み込み
                            st.rerun()
                        else:
                            st.error(message)

            with col2:
                if st.button("キャンセル", use_container_width=True):
                    st.session_state.show_obsidian_sync = False
                    st.rerun()

        else:  # 期間指定
            col1, col2 = st.columns(2)
            with col1:
                start_date = st.selectbox(
                    "開始日",
                    available_dates,
                    index=0,
                    format_func=lambda d: d.isoformat()
                )
            with col2:
                end_date = st.selectbox(
                    "終了日",
                    available_dates,
                    index=len(available_dates) - 1,
                    format_func=lambda d: d.isoformat()
                )

            if start_date > end_date:
                st.error("⚠️ 開始日は終了日より前の日付を選択してください")
                return

            st.info(f"📅 {start_date.isoformat()} ～ {end_date.isoformat()} ({(end_date - start_date).days + 1}日間)")

            col1, col2 = st.columns(2)
            with col1:
                if st.button("🔄 一括同期実行", type="primary", use_container_width=True):
                    with st.spinner("同期中..."):
                        results = sync_service.sync_date_range(start_date, end_date)

                        st.success(f"✅ 成功: {results['success_count']}件")
                        if results['failed_count'] > 0:
                            st.warning(f"⚠️ 失敗: {results['failed_count']}件")

                        # 詳細を表示
                        with st.expander("詳細ログ"):
                            for msg in results['messages']:
                                st.text(msg)

                        st.balloons()
                        # ダッシュボードを再読み込み
                        st.rerun()

            with col2:
                if st.button("キャンセル", use_container_width=True):
                    st.session_state.show_obsidian_sync = False
                    st.rerun()


if __name__ == "__main__":
    main()
