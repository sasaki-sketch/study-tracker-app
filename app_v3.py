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
from models.record import StudyRecord, StudySession
from services.database import DatabaseService
from services.obsidian import ObsidianService
from services.obsidian_sync import ObsidianSyncService
from services.tweet import TweetService
from utils.phase import get_current_phase
from components.event_forms import (
    render_past_exam_form,
    show_recent_past_exams,
    render_material_lap_form,
    show_materials_list,
    render_mock_exam_form,
    show_recent_mock_exams
)
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
        'About': "# 診断士学習記録アプリ v3\n中小企業診断士の学習進捗を管理するアプリです。"
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
                    width="stretch",
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
                if st.button("✕ 閉じる", key="close_tweet_display", type="secondary", width="stretch"):
                    st.session_state.selected_record = None
                    st.rerun()

            st.markdown("---")

            # 投稿文を生成（再生成された投稿文がある場合はそれを使用）
            stats = st.session_state.db_service.get_cumulative_stats()

            # セッション状態キー
            tweet_display_key = f"tweet_display_{selected.date.isoformat()}"

            # 初期値設定（まだセッション状態にない場合）
            if tweet_display_key not in st.session_state:
                if selected.id:
                    preview_sessions = st.session_state.db_service.get_study_sessions(selected.id)
                    st.session_state[tweet_display_key] = TweetService.generate_daily_tweet_from_sessions(selected, stats, preview_sessions)
                else:
                    st.session_state[tweet_display_key] = TweetService.generate_daily_tweet(selected, stats)

            # 2カラムレイアウト
            col_preview, col_actions = st.columns([2, 1])

            with col_preview:
                # 投稿文プレビュー
                st.markdown("#### 📝 投稿文プレビュー")
                st.text_area(
                    label="preview",
                    height=500,
                    key=tweet_display_key,
                    label_visibility="collapsed"
                )

                # 文字数カウント
                show_char_counter(st.session_state[tweet_display_key])

            with col_actions:
                # アクションエリア
                st.markdown("#### 🎯 アクション")

                # 主要アクション（大きく）
                current_tweet = st.session_state[tweet_display_key]
                tweet_url = f"https://x.com/intent/tweet?text={quote(current_tweet)}"
                st.link_button(
                    "🐦 Xで投稿する",
                    tweet_url,
                    width="stretch",
                    type="primary"
                )

                st.markdown("")  # スペース

                # 補助アクション
                if st.button("📋 コピー", key="copy_history_tweet", width="stretch"):
                    try:
                        pyperclip.copy(current_tweet)
                        st.toast("✅ コピーしました！", icon="✅")
                    except pyperclip.PyperclipException:
                        st.error("⚠️ クリップボードへのアクセスに失敗しました")
                        st.caption("ブラウザの設定でクリップボード機能を許可してください")
                    except Exception as e:
                        st.error(f"⚠️ 予期しないエラー: {str(e)}")

                # プロンプト生成（統一テンプレートを使用）
                from utils.tweet_prompts import generate_tweet_prompt_from_sessions, generate_tweet_prompt_legacy
                stats = st.session_state.db_service.get_cumulative_stats()

                # セッション取得してプロンプト生成
                if selected.id:
                    history_sessions = st.session_state.db_service.get_study_sessions(selected.id)
                    default_prompt = generate_tweet_prompt_from_sessions(selected, stats, history_sessions)
                else:
                    default_prompt = generate_tweet_prompt_legacy(selected, stats)

                # プロンプト編集エリア（展開可能）
                with st.expander("📝 プロンプト確認・編集", expanded=False):
                    edited_prompt = st.text_area(
                        "プロンプトを編集できます",
                        value=default_prompt,
                        height=300,
                        key="edited_prompt_history",
                        help="プロンプトを編集してカスタマイズできます"
                    )

                # アクションボタン
                col_action1, col_action2 = st.columns(2)

                with col_action1:
                    if st.button("📋 プロンプトをコピー", key="copy_prompt_history", width="stretch"):
                        try:
                            pyperclip.copy(edited_prompt)
                            st.toast("✅ プロンプトをコピー！", icon="📋")
                        except (pyperclip.PyperclipException, Exception) as e:
                            st.error(f"⚠️ コピーに失敗しました: {type(e).__name__}")

                with col_action2:
                    if st.button("🔄 再生成", key="regenerate_history_tweet", width="stretch", type="primary"):
                        from anthropic import Anthropic
                        import os

                        with st.spinner("🤖 AIが投稿文を作成中..."):
                            try:
                                # カスタムプロンプトを使用
                                api_key = os.environ.get("ANTHROPIC_API_KEY")
                                if not api_key:
                                    raise ValueError("ANTHROPIC_API_KEYが設定されていません")

                                client = Anthropic(api_key=api_key)
                                message = client.messages.create(
                                    model="claude-sonnet-4-20250514",
                                    max_tokens=1200,  # 4,000文字対応（日本語約800文字）
                                    temperature=0.7,
                                    messages=[{"role": "user", "content": edited_prompt}]
                                )

                                improved_tweet = message.content[0].text.strip()

                                # 既存のキーを削除してから新しい値を設定
                                if tweet_display_key in st.session_state:
                                    del st.session_state[tweet_display_key]

                                # 新しい投稿文を設定
                                st.session_state[tweet_display_key] = improved_tweet

                                st.success("✅ 投稿文を再生成しました！")
                                st.rerun()  # 画面を更新して投稿文プレビューに反映

                            except ValueError as e:
                                st.error(f"⚠️ {str(e)}")
                                st.info("💡 ANTHROPIC_API_KEYを環境変数に設定してください")
                            except Exception as e:
                                st.error(f"⚠️ 生成エラー: {str(e)}")

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

    # タブ切り替え（カテゴリ整理版 + アーカイブ）
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["🏠 ダッシュボード", "📝 記録", "📊 分析", "📦 アーカイブ", "⚙️ 設定"])

    with tab1:
        show_dashboard()

    with tab2:
        # 記録タブ内のサブタブ
        subtab1, subtab2 = st.tabs(["✏️ 今日の記録", "📖 イベント記録"])

        with subtab1:
            show_daily_input()

        with subtab2:
            show_event_page()

    with tab3:
        show_analytics()

    with tab4:
        show_archive()

    with tab5:
        show_settings()


def show_event_summary_cards():
    """イベント記録のサマリーカード表示"""
    from utils.event_stats import (
        calculate_past_exam_stats,
        calculate_material_progress_stats,
        calculate_mock_exam_stats
    )

    db = st.session_state.db_service

    # 統計計算
    past_stats = calculate_past_exam_stats(db)
    material_stats = calculate_material_progress_stats(db)
    mock_stats = calculate_mock_exam_stats(db)

    # データが全くない場合
    total_events = past_stats['total_count'] + material_stats['total_materials'] + mock_stats['total_count']

    if total_events == 0:
        st.info("📝 まだイベント記録がありません。過去問や教材の学習記録を始めましょう!")
        if st.button("📖 イベント記録ページへ", width="stretch"):
            st.session_state.active_tab = "record"
            st.rerun()
        return

    # 3列レイアウト
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("#### 📖 過去問演習")

        if past_stats['total_count'] == 0:
            st.info("まだ記録がありません")
            st.caption("過去問を解いたら記録してみましょう!")
        else:
            st.metric("実施回数", f"{past_stats['total_count']}回")
            st.metric("平均正答率", f"{past_stats['avg_correct_rate']}%")

            if past_stats['avg_correct_rate'] >= 70:
                st.success(f"✓ 合格水準達成率: {past_stats['pass_rate']}%")
            elif past_stats['avg_correct_rate'] >= 60:
                st.warning(f"⚠ 合格水準達成率: {past_stats['pass_rate']}%")
            else:
                st.info(f"→ 合格水準達成率: {past_stats['pass_rate']}%")

    with col2:
        st.markdown("#### 📚 教材周回")

        if material_stats['total_materials'] == 0:
            st.info("まだ登録がありません")
            st.caption("使用している教材を登録しましょう!")
        else:
            st.metric("登録教材数", f"{material_stats['total_materials']}件")
            st.metric("平均進捗率", f"{material_stats['avg_progress']}%")

            if material_stats['completed_count'] > 0:
                st.success(f"✓ 完了: {material_stats['completed_count']}件")
            else:
                st.info(f"→ 総学習時間: {material_stats['total_study_time']:.0f}分")

            if material_stats['avg_understanding'] > 0:
                stars = "⭐" * int(material_stats['avg_understanding'])
                st.caption(f"平均理解度: {stars} ({material_stats['avg_understanding']})")

    with col3:
        st.markdown("#### 📊 模試・答練")

        if mock_stats['total_count'] == 0:
            st.info("まだ記録がありません")
            st.caption("模試を受けたら結果を記録しましょう!")
        else:
            st.metric("受験回数", f"{mock_stats['total_count']}回")

            if mock_stats['first_exam_avg_score'] > 0:
                st.metric("1次平均得点率", f"{mock_stats['first_exam_avg_score']}%")

            if mock_stats['second_exam_pass_count'] > 0:
                st.success(f"✓ 2次合格水準達成: {mock_stats['second_exam_pass_count']}回")

            if mock_stats['recent_performance'] == 'excellent':
                st.success("パフォーマンス: 優秀!")
            elif mock_stats['recent_performance'] == 'good':
                st.info("パフォーマンス: 良好")
            elif mock_stats['total_count'] > 0:
                st.caption("パフォーマンス: 要改善")

    # SNS投稿用画像ダウンロードボタン
    st.markdown("---")
    st.markdown("#### 📸 SNS投稿用画像")

    col_btn1, col_btn2 = st.columns([1, 2])

    with col_btn1:
        if st.button("🖼 週次サマリー画像を生成", width="stretch", type="primary"):
            from utils.image_generator import get_weekly_stats, generate_weekly_summary_card
            from datetime import datetime

            with st.spinner("画像生成中..."):
                try:
                    # 統計データ取得
                    weekly_stats_data = get_weekly_stats(db)

                    # 画像生成
                    image_bytes = generate_weekly_summary_card(weekly_stats_data)

                    # ダウンロードボタン表示
                    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                    st.download_button(
                        label="💾 画像をダウンロード",
                        data=image_bytes,
                        file_name=f"study_summary_{timestamp}.png",
                        mime="image/png",
                        width="stretch"
                    )

                    st.success("✅ 画像生成完了！ダウンロードボタンをクリックしてください")

                except Exception as e:
                    st.error(f"⚠️ 画像生成エラー: {str(e)}")

    with col_btn2:
        st.caption("📊 過去問・教材・学習時間の週次統計を美しい画像にします（X/Twitter投稿用）")


def show_daily_mission(stats, days_to_shindan):
    """今日のミッション - 最優先タスク表示"""
    # ヘッダーは削除（レイアウトの整合性のため）

    # 今日の学習記録を取得
    today_record = st.session_state.db_service.get_record_by_date(date.today())

    # 今日の実績
    shindan_today = today_record.shindan_time if today_record else 0.0

    # 目標時間を動的に計算（残り日数から逆算）
    shindan_exam_date = date(2026, 8, 5)
    shindan_days_remaining = max((shindan_exam_date - date.today()).days, 1)

    # 残り時間から1日あたりの目標を計算
    shindan_remaining_hours = max(stats.shindan_goal - stats.shindan_total, 0)

    # 1次試験対策期間: 診断士1次のみ(3h/日)
    if date.today() < shindan_exam_date:
        shindan_1st_remaining = 600.0 - stats.shindan_total
        shindan_days_to_1st = max((shindan_exam_date - date.today()).days, 1)
        shindan_goal_daily = min(round(shindan_1st_remaining / shindan_days_to_1st, 1), 3.0)
    else:
        # 2次試験対策期間(1次試験後〜2次試験前): 診断士2次のみ(3h/日)
        shindan_2nd_remaining = 170.0  # 2次試験対策時間
        shindan_days_to_2nd = max((date(2026, 10, 25) - date.today()).days, 1)
        shindan_goal_daily = min(round(shindan_2nd_remaining / shindan_days_to_2nd, 1), 3.0)

    # プログレス計算
    shindan_progress = min((shindan_today / shindan_goal_daily) * 100, 100) if shindan_goal_daily > 0 else 0

    # カードデザイン（診断士のみ、中央寄せ、最大幅70%）
    st.markdown(f"""<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 2rem; border-radius: 15px; box-shadow: 0 8px 16px rgba(0,0,0,0.2); margin-bottom: 1rem; max-width: 70%; margin-left: auto; margin-right: auto;">
        <div style="color: white; font-size: 1.1rem; font-weight: 600; margin-bottom: 1.5rem;">📅 {date.today().strftime('%Y年%m月%d日')} の学習目標</div>
        <div style="background: rgba(78, 205, 196, 0.95); padding: 1.5rem; border-radius: 12px; border-left: 5px solid #0fb9b1;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.8rem;">
                <div>
                    <div style="color: white; font-size: 1.3rem; font-weight: 700;">📘 中小企業診断士</div>
                    <div style="color: rgba(255,255,255,0.9); font-size: 0.9rem; margin-top: 0.3rem;">⚠️ 1次試験まで残り {days_to_shindan} 日</div>
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
            <div style="font-size: 2.5rem; font-weight: 700;">{shindan_today:.1f}h / {shindan_goal_daily}h</div>
        </div>
    </div>""", unsafe_allow_html=True)

    # 目標達成メッセージは削除（UIをシンプルに）


def show_dashboard():
    """ダッシュボード画面（完全再設計版）"""
    # データ取得
    stats = st.session_state.db_service.get_cumulative_stats()
    all_records = st.session_state.db_service.get_all_records()

    # 統計計算
    days_to_toukei, days_to_shindan = calculate_days_until_exam()

    # フェーズ別必要ペース計算（診断士のみ）
    required_pace_shindan = calculate_required_daily_pace(
        stats.shindan_1ji_total,
        stats.shindan_1ji_goal,
        days_to_shindan
    )
    streak = calculate_streak(all_records)
    weekly_stats = calculate_weekly_stats(all_records)
    monthly_stats = calculate_monthly_stats(all_records)
    current_phase = get_current_phase()

    # グリッドレイアウト: 上段（名言+ミッション）/ 下段（カウントダウン）

    # 上段: 2カラム（名言 + ミッション）
    top_left, top_right = st.columns([1, 1])

    with top_left:
        # 📜 今日の古典名言
        daily_quote = get_daily_quote()
        st.markdown(f"""
        <div class="achievement-banner" style="margin-bottom: 1rem;">
            <div style="font-size: 1.2rem; font-weight: 600; margin-bottom: 0.6rem; letter-spacing: 0.05em;">
                {daily_quote['original']}
            </div>
            <div style="font-size: 0.95rem; opacity: 0.9; margin-bottom: 0.4rem;">
                {daily_quote['translation']}
            </div>
            <div style="font-size: 0.85rem; opacity: 0.75; text-align: right;">
                ― {daily_quote['source']}
            </div>
        </div>
        """, unsafe_allow_html=True)

        # 📈 現在の学習進捗（名言の下に配置）
        show_goal_vs_actual(stats, st.session_state.db_service)

    with top_right:
        # 🎯 今日のミッション
        show_daily_mission(stats, days_to_shindan)

    # 📊 学習進捗評価（カウントダウン統合版）
    st.divider()
    st.markdown("### 📊 学習進捗評価")

    # 診断士1次の今週実績（関連資格を除外）
    today = date.today()
    week_start = today - timedelta(days=today.weekday())
    weekly_shindan_1ji = sum(
        record.shindan_time
        for record in all_records
        if record.phase in ['基礎固め期', 'インプット期', 'アウトプット期', '直前期']
        and week_start <= record.date <= today
    )

    # 診断士1次のみ表示（全幅）
    weekly_pace_shindan = round(required_pace_shindan * 7, 1)
    shindan_achievement_rate = (weekly_shindan_1ji / weekly_pace_shindan) * 100 if weekly_pace_shindan > 0 else 0

    # 週の進行度を考慮した評価
    weekday = today.weekday()
    week_progress = (weekday + 1) / 7
    expected_achievement = week_progress * 100

    # 評価判定
    if shindan_achievement_rate >= expected_achievement:
        status = "🟢 順調！"
        status_color = "#27ae60"
        message = "必要ペースを達成しています！この調子で継続しましょう"
    elif shindan_achievement_rate >= expected_achievement * 0.7:
        status = "🟡 あと一息！"
        status_color = "#f39c12"
        message = "もう少しペースアップして目標達成を目指しましょう"
    else:
        status = "🔴 頑張ろう！"
        status_color = "#e74c3c"
        message = "今週の学習時間を増やして挽回しましょう"

    html_content = f"""
    <div style="background: linear-gradient(135deg, {status_color}20 0%, {status_color}10 100%); padding: 35px; border-radius: 15px; border-left: 5px solid {status_color}; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); max-width: 700px; margin: 0 auto;">
        <div style="font-size: 22px; font-weight: 600; margin-bottom: 15px; color: #e0e0e0;">📚 中小企業診断士 1次試験</div>
        <div style="font-size: 40px; font-weight: bold; margin: 15px 0; color: {status_color};">{status}</div>
        <div style="background: rgba(255,255,255,0.12); padding: 15px; border-radius: 8px; margin: 15px 0;">
            <div style="font-size: 14px; color: #b0b0b0; margin-bottom: 6px;">⏰ 試験まで</div>
            <div style="font-size: 28px; font-weight: bold; color: #ffffff;">{days_to_shindan}日 <span style="font-size: 15px; font-weight: normal; color: #d0d0d0;">(8月5日)</span></div>
        </div>
        <div style="background: rgba(255,255,255,0.12); padding: 15px; border-radius: 8px; margin: 15px 0;">
            <div style="font-size: 14px; color: #b0b0b0; margin-bottom: 6px;">📊 今週の学習</div>
            <div style="font-size: 24px; font-weight: bold; color: #ffffff;">{weekly_shindan_1ji:.1f}h <span style="font-size: 16px; color: #d0d0d0;">/ {weekly_pace_shindan:.1f}h</span></div>
            <div style="font-size: 14px; color: #b0b0b0; margin-top: 6px;">達成率: {shindan_achievement_rate:.0f}% | 目標: 520h</div>
        </div>
        <div style="font-size: 14px; color: #b0b0b0; margin-top: 15px; font-style: italic;">{message}</div>
    </div>
    """
    st.markdown(html_content, unsafe_allow_html=True)

    # 🗺️ ロードマップ（全幅表示）
    st.divider()
    show_roadmap()

    # Obsidian同期モーダル
    if st.session_state.get('show_obsidian_sync', False):
        show_obsidian_sync_modal()


def show_daily_input():
    """日次記録入力画面（複数科目対応版）"""
    from components.daily_input import render_daily_input_form
    from services.record_handler import save_record_with_sessions, generate_and_display_tweet

    # フォーム表示
    form_result = render_daily_input_form()

    if form_result:
        action = form_result['action']
        target_date = form_result['date']
        phase = form_result['phase']
        shindan_sessions = form_result['shindan_sessions']
        toukei_sessions = form_result['toukei_sessions']

        try:
            # レコード保存
            record_id = save_record_with_sessions(
                target_date,
                phase,
                shindan_sessions,
                toukei_sessions,
                st.session_state.db_service
            )

            st.success(f"✅ 記録を保存しました（ID: {record_id}）")

            # レコード再取得
            record = st.session_state.db_service.get_record_by_date(target_date)
            all_sessions = shindan_sessions + toukei_sessions

            if action == 'save_and_tweet':
                # 投稿文生成・表示
                generate_and_display_tweet(
                    record,
                    all_sessions,
                    st.session_state.db_service,
                    st.session_state.obsidian_service
                )
            else:
                # 保存のみ
                st.info("💾 保存完了しました")

            # セッション状態クリア
            if 'shindan_sessions' in st.session_state:
                del st.session_state['shindan_sessions']
            if 'toukei_sessions' in st.session_state:
                del st.session_state['toukei_sessions']

        except Exception as e:
            st.error(f"⚠️ エラーが発生しました: {str(e)}")
            import traceback
            with st.expander("詳細エラー情報"):
                st.code(traceback.format_exc())

def show_analytics():
    """分析画面（リファクタリング版 - セッションベース）"""
    st.header("📊 学習分析")

    # 資格フィルタ
    col_filter1, col_filter2 = st.columns([3, 1])
    with col_filter1:
        qualification_filter = st.selectbox(
            "📚 表示する資格",
            options=[
                "現在の学習（診断士＋統計）",
                "診断士（一次＋二次）",
                "診断士一次試験のみ",
                "診断士二次試験のみ",
                "統計検定のみ",
                "全て（過去資格含む）"
            ],
            index=0,
            help="分析対象の資格を選択してください"
        )

    # フィルタ条件を決定
    if qualification_filter == "診断士（一次＋二次）":
        filter_qualifications = ["shindan_1ji", "shindan_2ji"]
    elif qualification_filter == "診断士一次試験のみ":
        filter_qualifications = ["shindan_1ji"]
    elif qualification_filter == "診断士二次試験のみ":
        filter_qualifications = ["shindan_2ji"]
    elif qualification_filter == "統計検定のみ":
        filter_qualifications = ["toukei"]
    elif qualification_filter == "現在の学習（診断士＋統計）":
        filter_qualifications = ["shindan_1ji", "shindan_2ji", "toukei"]
    else:  # 全て
        filter_qualifications = None  # None = フィルタなし

    st.divider()

    # サービス初期化
    from services.analytics import AnalyticsService
    from components.kpi_dashboard import render_kpi_cards, render_motivational_message, render_insights
    from components.analytics_charts import (
        render_time_series_chart,
        render_subject_bar_chart,
        render_weekly_comparison_chart
    )

    analytics = AnalyticsService(st.session_state.db_service)

    # 現在のフェーズを取得
    from utils.phase import get_current_phase
    current_phase = get_current_phase()

    # データ取得（N+1問題解消済み、フェーズ別平均計算、資格フィルタ対応）
    try:
        summaries = analytics.get_daily_summary(qualification_filter=filter_qualifications)
        subject_stats = analytics.get_subject_breakdown(qualification_filter=filter_qualifications)
        weekly_stats = analytics.get_weekly_stats(weeks=4, qualification_filter=filter_qualifications)
        kpi_metrics = analytics.get_kpi_metrics(
            current_phase=current_phase,
            qualification_filter=filter_qualifications
        )
    except Exception as e:
        st.error(f"⚠️ データ取得エラー: {str(e)}")
        return

    if not summaries:
        st.info("まだ記録がありません")
        return

    # KPIダッシュボード
    render_kpi_cards(kpi_metrics)

    # モチベーションメッセージ
    render_motivational_message(kpi_metrics)

    st.divider()

    # グラフセクション（2カラム）
    col1, col2 = st.columns(2)

    with col1:
        # 学習時間推移グラフ（Plotly版）
        fig_time_series = render_time_series_chart(summaries, height=400)
        if fig_time_series:
            st.plotly_chart(fig_time_series, width="stretch", key="time_series_chart")

    with col2:
        # 週次比較グラフ（Plotly版）
        fig_weekly = render_weekly_comparison_chart(weekly_stats, height=400)
        if fig_weekly:
            st.plotly_chart(fig_weekly, width="stretch", key="weekly_comparison_chart")

    st.divider()

    # 科目別グラフ（全幅）
    if subject_stats:
        fig_subjects = render_subject_bar_chart(subject_stats, show_emoji=True, height=400)
        if fig_subjects:
            st.plotly_chart(fig_subjects, width="stretch", key="subject_bar_chart")
    else:
        st.info("📚 科目別データがありません")

    st.divider()

    # インサイト表示
    render_insights(kpi_metrics, subject_stats)

    st.divider()

    # 履歴テーブル
    st.subheader("📜 学習履歴")

    # 全レコード取得
    all_records = st.session_state.db_service.get_all_records()

    for record in all_records[:10]:  # 最新10件
        with st.expander(f"{record.date.strftime('%Y年%m月%d日')} - {record.phase}"):
            # セッション取得（record.idがある場合）
            sessions = []
            if record.id:
                sessions = st.session_state.db_service.get_study_sessions(record.id)

            if sessions:
                # 新形式: セッション別表示
                shindan_sessions = [s for s in sessions if s.qualification in ('shindan_1ji', 'shindan_2ji')]
                toukei_sessions = [s for s in sessions if s.qualification == 'toukei']

                col1, col2 = st.columns(2)

                with col1:
                    st.markdown("**中小企業診断士**")
                    st.write(f"合計: {record.shindan_time}h")
                    for session in shindan_sessions:
                        st.markdown(f"- **{session.subject}** {session.time_hours}h")
                        if session.content:
                            st.caption(f"内容: {session.content}")

                with col2:
                    st.markdown("**統計検定2級**")
                    st.write(f"合計: {record.toukei_time}h")
                    for session in toukei_sessions:
                        if session.content:
                            st.caption(f"内容: {session.content}")
            else:
                # レガシー形式表示
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

            # 投稿文再生成ボタン
            if st.button("📱 投稿文を生成", key=f"generate_tweet_{record.id or record.date}"):
                from services.record_handler import generate_and_display_tweet

                # セッション取得（なければレガシー変換）
                if sessions:
                    all_sessions = sessions
                else:
                    # レガシーデータをセッション形式に変換
                    all_sessions = []
                    if record.shindan_time > 0:
                        all_sessions.append(StudySession(
                            record_id=record.id or 0,
                            qualification='shindan',
                            subject=record.shindan_subject or '未分類',
                            time_hours=record.shindan_time,
                            content=record.shindan_content,
                            issue=record.shindan_issue
                        ))
                    if record.toukei_time > 0:
                        all_sessions.append(StudySession(
                            record_id=record.id or 0,
                            qualification='toukei',
                            subject='統計検定2級',
                            time_hours=record.toukei_time,
                            content=record.toukei_content,
                            issue=record.toukei_issue
                        ))

                generate_and_display_tweet(
                    record,
                    all_sessions,
                    st.session_state.db_service,
                    st.session_state.obsidian_service
                )


def show_archive():
    """アーカイブ画面（過去取得資格の記録）"""
    st.header("📦 学習アーカイブ")

    st.info("""
    💡 **アーカイブについて**

    このタブでは、過去に取得した資格の学習記録を確認できます。
    現在の学習（中小企業診断士・統計検定2級）とは別に管理されています。
    """)

    # サービス初期化
    from services.analytics import AnalyticsService
    from components.analytics_charts import render_subject_bar_chart

    analytics = AnalyticsService(st.session_state.db_service)

    st.divider()

    # 過去資格のデータを表示
    st.subheader("📚 過去取得資格の学習実績")

    # 全科目データを取得（フィルタなし）
    all_subject_stats = analytics.get_subject_breakdown(qualification_filter=None)

    # 現在の学習資格を除外（診断士・統計以外）
    archive_subjects = {
        subject: stats
        for subject, stats in all_subject_stats.items()
        if stats.qualification not in ['shindan_1ji', 'shindan_2ji', 'toukei']
    }

    if not archive_subjects:
        st.info("📭 アーカイブ記録はまだありません。")
        st.caption("過去に取得した資格のデータがここに表示されます。")
    else:
        # 資格ごとにグループ化
        qualifications = {}
        for subject, stats in archive_subjects.items():
            qual = stats.qualification
            if qual not in qualifications:
                qualifications[qual] = []
            qualifications[qual].append((subject, stats))

        # 資格ごとに表示
        for qualification, subjects in qualifications.items():
            # 資格名の表示
            qual_name_map = {
                'boki': '📊 簿記',
                'kihon_joho': '💻 基本情報技術者',
                'other': '📖 その他'
            }
            qual_display = qual_name_map.get(qualification, f"📖 {qualification}")

            st.markdown(f"### {qual_display}")

            # その資格の合計時間を計算
            total_hours = sum(stats.total_hours for _, stats in subjects)
            session_count = sum(stats.session_count for _, stats in subjects)

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("📚 科目数", f"{len(subjects)}科目")
            with col2:
                st.metric("⏱️ 総学習時間", f"{total_hours}h")
            with col3:
                st.metric("📝 セッション数", f"{session_count}回")

            # 科目別詳細テーブル
            with st.expander("📋 科目別詳細", expanded=False):
                subject_data = []
                for subject, stats in subjects:
                    subject_data.append({
                        "科目": subject,
                        "学習時間": f"{stats.total_hours}h",
                        "セッション数": f"{stats.session_count}回",
                        "平均時間": f"{stats.avg_hours_per_session}h",
                        "最終学習日": stats.last_studied.strftime('%Y-%m-%d') if stats.last_studied else "-"
                    })

                df = pd.DataFrame(subject_data)
                st.dataframe(df, width="stretch", hide_index=True)

            st.divider()

    st.divider()

    # データ管理セクション
    st.subheader("🔧 データ管理")

    st.warning("""
    ⚠️ **データ整理について**

    現在、過去資格のデータが「診断士」として誤って登録されている可能性があります。
    将来的には、データの資格分類を修正する機能を追加予定です。
    """)

    # 全セッションの資格分類を確認
    with st.expander("🔍 データ分類状況の確認", expanded=False):
        with st.session_state.db_service.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT s.qualification, COUNT(s.id) as count, SUM(s.time_hours) as total_hours
                FROM study_sessions s
                GROUP BY s.qualification
                ORDER BY total_hours DESC
            """)

            qual_data = []
            for row in cursor.fetchall():
                qual_map = {
                    'shindan_1ji': '🏢 診断士(一次試験)',
                    'shindan_2ji': '🏢 診断士(二次試験)',
                    'toukei': '📈 統計検定2級',
                    'boki': '📊 簿記',
                    'kihon_joho': '💻 基本情報技術者',
                    'other': '📖 その他'
                }
                qual_data.append({
                    "資格": qual_map.get(row[0], row[0]),
                    "セッション数": f"{row[1]}回",
                    "総学習時間": f"{row[2]}h"
                })

            df_qual = pd.DataFrame(qual_data)
            st.dataframe(df_qual, width="stretch", hide_index=True)


def show_settings():
    """設定画面"""
    st.header("⚙️ 設定")

    # 科目設定セクション
    from components.subject_settings import show_subject_settings
    show_subject_settings()

    st.divider()

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

    # 生データビューアー
    st.subheader("🔍 生データビューアー")
    st.write("全セッションデータを表示・編集・削除できます")

    with st.session_state.db_service.get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT
                s.id,
                r.date,
                r.phase,
                s.qualification,
                s.subject,
                s.time_hours,
                s.content,
                s.issue
            FROM study_sessions s
            JOIN records r ON s.record_id = r.id
            ORDER BY r.date DESC, s.id DESC
        """)

        data = cursor.fetchall()

        if data:
            # データフレームに変換
            df = pd.DataFrame(data, columns=[
                "ID", "日付", "フェーズ", "資格", "科目", "時間(h)", "内容", "課題"
            ])

            # 資格名を日本語に変換
            qual_map = {
                'shindan_1ji': '診断士(一次)',
                'shindan_2ji': '診断士(二次)',
                'toukei': '統計検定',
                'boki': '簿記',
                'kihon_joho': '基本情報',
                'other': 'その他'
            }
            df['資格'] = df['資格'].map(lambda x: qual_map.get(x, x))

            # 表示
            st.dataframe(df, width="stretch", hide_index=True)

            st.caption(f"総セッション数: {len(df)}件")

            # 削除機能
            with st.expander("🗑️ データ削除"):
                st.warning("⚠️ 削除したデータは復元できません。慎重に操作してください。")

                session_id = st.number_input(
                    "削除するセッションID",
                    min_value=1,
                    max_value=int(df['ID'].max()) if len(df) > 0 else 1,
                    step=1
                )

                if st.button("🗑️ 選択したセッションを削除", type="secondary"):
                    with st.session_state.db_service.get_connection() as del_conn:
                        del_cursor = del_conn.cursor()
                        del_cursor.execute("DELETE FROM study_sessions WHERE id = ?", (session_id,))
                        del_conn.commit()
                        st.success(f"✅ セッションID {session_id} を削除しました")
                        st.rerun()
        else:
            st.info("データがありません")

    st.divider()

    st.subheader("Obsidian出力先")
    obsidian_path = st.session_state.obsidian_service.vault_path
    st.code(str(obsidian_path))

    st.divider()

    st.subheader("💾 データバックアップ")
    st.write("学習記録をCSV形式でエクスポートできます")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📅 日々の記録をエクスポート", width="stretch"):
            import csv
            from io import StringIO
            from datetime import datetime

            # 全記録取得
            all_records = st.session_state.db_service.get_all_records()

            if all_records:
                # CSV生成
                output = StringIO()
                writer = csv.writer(output)

                # ヘッダー
                writer.writerow([
                    '日付', 'フェーズ',
                    '診断士時間', '診断士科目', '診断士内容', '診断士課題',
                    '統計時間', '統計内容', '統計課題'
                ])

                # データ
                for record in all_records:
                    writer.writerow([
                        record.date.isoformat(),
                        record.phase,
                        record.shindan_time,
                        record.shindan_subject,
                        record.shindan_content,
                        record.shindan_issue,
                        record.toukei_time,
                        record.toukei_content,
                        record.toukei_issue
                    ])

                # ダウンロードボタン
                csv_data = output.getvalue()
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

                st.download_button(
                    label="💾 CSVダウンロード",
                    data=csv_data,
                    file_name=f"study_records_{timestamp}.csv",
                    mime="text/csv",
                    width="stretch"
                )
                st.success(f"✅ {len(all_records)}件の記録を準備しました")
            else:
                st.warning("データがありません")

    with col2:
        if st.button("📖 イベント記録をエクスポート", width="stretch"):
            import csv
            import json
            from io import StringIO
            from datetime import datetime

            # 全イベント取得
            db = st.session_state.db_service
            all_events = db.get_recent_events(limit=10000)

            if all_events:
                # CSV生成
                output = StringIO()
                writer = csv.writer(output)

                # ヘッダー
                writer.writerow([
                    'ID', 'イベント種別', '日付', '科目', 'メモ', '詳細データ'
                ])

                # データ
                for event in all_events:
                    writer.writerow([
                        event['id'],
                        event['event_type'],
                        event['date'],
                        event['subject'],
                        event['memo'],
                        json.dumps(event['details'], ensure_ascii=False)
                    ])

                # ダウンロードボタン
                csv_data = output.getvalue()
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

                st.download_button(
                    label="💾 CSVダウンロード",
                    data=csv_data,
                    file_name=f"study_events_{timestamp}.csv",
                    mime="text/csv",
                    width="stretch"
                )
                st.success(f"✅ {len(all_events)}件のイベントを準備しました")
            else:
                st.warning("データがありません")

    with col3:
        if st.button("📚 教材マスタをエクスポート", width="stretch"):
            import csv
            from io import StringIO
            from datetime import datetime

            # 全教材取得
            db = st.session_state.db_service
            all_materials = db.get_all_materials()

            if all_materials:
                # CSV生成
                output = StringIO()
                writer = csv.writer(output)

                # ヘッダー
                writer.writerow([
                    'ID', '教材名', '科目', '種別', '目標周回数',
                    '現在周回数', '総学習時間', '平均理解度', '最終学習日'
                ])

                # データ
                for material in all_materials:
                    writer.writerow([
                        material['id'],
                        material['name'],
                        material['subject'],
                        material['material_type'],
                        material['target_laps'],
                        material['current_lap'],
                        material['total_time'],
                        material['avg_understanding'],
                        material['last_study_date']
                    ])

                # ダウンロードボタン
                csv_data = output.getvalue()
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

                st.download_button(
                    label="💾 CSVダウンロード",
                    data=csv_data,
                    file_name=f"materials_{timestamp}.csv",
                    mime="text/csv",
                    width="stretch"
                )
                st.success(f"✅ {len(all_materials)}件の教材を準備しました")
            else:
                st.warning("データがありません")

    st.caption("💡 定期的にバックアップを取得することをおすすめします")

    st.divider()

    st.subheader("🔗 n8n連携")
    st.write("学習データをn8nワークフローに送信できます")

    col_n8n1, col_n8n2 = st.columns(2)

    with col_n8n1:
        st.info("📊 イベント登録時に自動でWebhook送信されます")
        st.caption("過去問・教材周回・模試の記録が自動的にn8nに送信されます")

    with col_n8n2:
        if st.button("📤 週次サマリーを送信", width="stretch", type="primary"):
            from utils.webhook import send_weekly_summary_to_n8n

            with st.spinner("週次サマリーを送信中..."):
                success = send_weekly_summary_to_n8n(st.session_state.db_service)

                if success:
                    st.success("✅ 週次サマリーをn8nに送信しました！")
                else:
                    st.error("⚠️ 送信に失敗しました。n8nワークフローが起動しているか確認してください。")



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
                if st.button("🔄 同期実行", type="primary", width="stretch"):
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
                if st.button("キャンセル", width="stretch"):
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
                if st.button("🔄 一括同期実行", type="primary", width="stretch"):
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
                if st.button("キャンセル", width="stretch"):
                    st.session_state.show_obsidian_sync = False
                    st.rerun()


def show_event_page():
    """イベント記録ページ - 過去問演習・教材周回・模試記録"""
    st.markdown("## 📝 イベント記録")
    st.markdown("過去問演習や教材の周回状況を記録して、学習の進捗を可視化します")

    # イベント種類のタブ
    event_tab1, event_tab2, event_tab3 = st.tabs(["📖 過去問演習", "📚 教材周回", "📊 模試・答練"])

    with event_tab1:
        # 過去問演習記録セクション
        render_past_exam_form()
        st.markdown("---")
        show_recent_past_exams()

    with event_tab2:
        # 教材周回記録セクション
        render_material_lap_form()
        st.markdown("---")
        show_materials_list()

    with event_tab3:
        # 模試・答練記録セクション
        render_mock_exam_form()
        st.markdown("---")
        show_recent_mock_exams()


if __name__ == "__main__":
    main()
