"""
診断士学習記録アプリ - Streamlit版
"""
import streamlit as st
from datetime import date, datetime
import pyperclip

from database.init_db import init_database
from models.record import StudyRecord
from services.database import DatabaseService
from services.obsidian import ObsidianService
from services.tweet import TweetService
from utils.phase import get_current_phase


# ページ設定
st.set_page_config(
    page_title="診断士学習記録",
    page_icon="📚",
    layout="wide"
)


def init_app():
    """アプリ初期化"""
    # データベース初期化
    init_database()

    # セッションステート初期化
    if 'db_service' not in st.session_state:
        st.session_state.db_service = DatabaseService()
    if 'obsidian_service' not in st.session_state:
        st.session_state.obsidian_service = ObsidianService()
    if 'tweet_service' not in st.session_state:
        st.session_state.tweet_service = TweetService()


def main():
    """メイン画面"""
    init_app()

    st.title("📚 診断士学習記録")

    # サイドバー: 累計統計
    with st.sidebar:
        st.header("📊 累計統計")
        stats = st.session_state.db_service.get_cumulative_stats()

        st.metric(
            "中小企業診断士",
            f"{stats.shindan_total}h",
            f"{stats.shindan_progress}%"
        )
        st.progress(stats.shindan_progress / 100)

        st.metric("統計検定2級", f"{stats.toukei_total}h")

        st.divider()

        # 現在のフェーズ
        current_phase = get_current_phase()
        st.info(f"📅 現在のフェーズ: **{current_phase}**")

    # タブ切り替え
    tab1, tab2, tab3 = st.tabs(["日次記録", "履歴", "設定"])

    with tab1:
        show_daily_input()

    with tab2:
        show_history()

    with tab3:
        show_settings()


def show_daily_input():
    """日次記録入力画面"""
    st.header("今日の学習記録")

    # 日付選択
    target_date = st.date_input("日付", value=date.today())

    # 既存データ読み込み
    existing_record = st.session_state.db_service.get_record_by_date(target_date)

    # フェーズ
    phase = get_current_phase()
    st.write(f"**フェーズ**: {phase}")

    st.divider()

    # 中小企業診断士セクション
    st.subheader("中小企業診断士")

    col1, col2 = st.columns([1, 3])

    with col1:
        shindan_time = st.number_input(
            "学習時間（h）",
            min_value=0.0,
            max_value=24.0,
            value=float(existing_record.shindan_time) if existing_record else 0.0,
            step=0.5,
            key="shindan_time"
        )

    with col2:
        # 科目選択
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
        key="shindan_content"
    )

    shindan_issue = st.text_area(
        "課題",
        value=existing_record.shindan_issue if existing_record else "",
        placeholder="例: 固変分解の理解",
        key="shindan_issue"
    )

    st.divider()

    # 統計検定2級セクション
    st.subheader("統計検定2級")

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
        placeholder="例: 推定演習",
        key="toukei_content"
    )

    toukei_issue = st.text_area(
        "課題",
        value=existing_record.toukei_issue if existing_record else "",
        placeholder="例: 信頼区間の理解",
        key="toukei_issue"
    )

    st.divider()

    # 保存ボタン
    col1, col2, col3 = st.columns([2, 1, 1])

    with col1:
        if st.button("💾 保存してX投稿文生成", type="primary", use_container_width=True):
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

    with col3:
        if st.button("🔄 リセット", use_container_width=True):
            st.rerun()


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
    # レコード作成
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

    # データベースに保存
    record_id = st.session_state.db_service.save_record(record)

    # 累計統計取得
    stats = st.session_state.db_service.get_cumulative_stats()

    # Obsidianファイル出力
    file_path = st.session_state.obsidian_service.export_to_obsidian(record, stats)

    # X投稿文生成
    tweet_text = st.session_state.tweet_service.generate_daily_tweet(record, stats)

    # クリップボードにコピー
    try:
        pyperclip.copy(tweet_text)
        clipboard_msg = "✅ クリップボードにコピーしました"
    except:
        clipboard_msg = "⚠️ クリップボードへのコピーに失敗しました"

    # 成功メッセージ
    st.success(f"✅ 記録を保存しました（ID: {record_id}）")
    st.success(f"✅ Obsidianファイルを出力しました: {file_path.name}")
    st.info(clipboard_msg)

    # 投稿文表示
    st.subheader("📱 X投稿文")
    st.code(tweet_text, language=None)

    # コピーボタン
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
    """記録のみ保存（投稿文生成なし）"""
    # レコード作成
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

    # データベースに保存
    record_id = st.session_state.db_service.save_record(record)

    # 累計統計取得
    stats = st.session_state.db_service.get_cumulative_stats()

    # Obsidianファイル出力
    file_path = st.session_state.obsidian_service.export_to_obsidian(record, stats)

    # 成功メッセージ
    st.success(f"✅ 記録を保存しました（ID: {record_id}）")
    st.success(f"✅ Obsidianファイルを出力しました: {file_path.name}")


def show_history():
    """履歴表示画面"""
    st.header("📜 学習履歴")

    # 全記録取得
    records = st.session_state.db_service.get_all_records()

    if not records:
        st.info("まだ記録がありません")
        return

    # テーブル表示
    st.write(f"**全{len(records)}件**")

    for record in records:
        with st.expander(f"{record.date.strftime('%Y年%m月%d日')} - {record.phase}"):
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("中小企業診断士")
                st.write(f"**時間**: {record.shindan_time}h")
                if record.shindan_subject:
                    st.write(f"**科目**: {record.shindan_subject}")
                if record.shindan_content:
                    st.write(f"**内容**: {record.shindan_content}")
                if record.shindan_issue:
                    st.write(f"**課題**: {record.shindan_issue}")

            with col2:
                st.subheader("統計検定2級")
                st.write(f"**時間**: {record.toukei_time}h")
                if record.toukei_content:
                    st.write(f"**内容**: {record.toukei_content}")
                if record.toukei_issue:
                    st.write(f"**課題**: {record.toukei_issue}")


def show_settings():
    """設定画面"""
    st.header("⚙️ 設定")

    st.subheader("データベース")
    st.write("データベースパス: `~/study_app/study_records.db`")

    st.subheader("Obsidian出力先")
    obsidian_path = st.session_state.obsidian_service.vault_path
    st.write(f"パス: `{obsidian_path}`")

    st.subheader("科目マスタ")
    subjects = st.session_state.db_service.get_subjects()

    for subject_name, abbr in subjects:
        st.write(f"- {subject_name} ({abbr})")


if __name__ == "__main__":
    main()
