"""
日次記録入力フォーム（複数科目対応版）
"""
import streamlit as st
from datetime import date
from typing import List
from models.record import StudySession
from utils.phase import get_current_phase
from utils.subjects import SUBJECT_EMOJI_MAP


def render_daily_input_form():
    """日次記録入力フォーム（複数科目対応）"""
    st.header("✏️ 今日の学習記録")

    # 日付選択
    col1, col2 = st.columns([2, 1])
    with col1:
        target_date = st.date_input("📅 日付", value=date.today(), key="input_date")

    with col2:
        phase = get_current_phase()
        st.info(f"**フェーズ**: {phase}")

    # 既存データ読み込み
    db = st.session_state.db_service
    existing_record = db.get_record_by_date(target_date)

    # 既存セッションを取得（record_idがある場合）
    existing_sessions = []
    if existing_record and existing_record.id:
        existing_sessions = db.get_study_sessions(existing_record.id)

    # セッション状態の初期化
    if 'shindan_sessions' not in st.session_state:
        if existing_sessions:
            # 既存データから復元
            st.session_state.shindan_sessions = [
                s for s in existing_sessions if s.qualification in ('shindan_1ji', 'shindan_2ji')
            ]
        else:
            # デフォルト: 1セッション
            st.session_state.shindan_sessions = [
                StudySession(
                    record_id=0,
                    qualification='shindan_1ji',
                    subject='財務・会計',
                    time_hours=0.0,
                    content='',
                    issue=''
                )
            ]

    # 統計検定セッションは常に空リストに固定（入力UIは削除済み）
    st.session_state.toukei_sessions = []

    # 科目リスト取得
    subjects = db.get_subjects()
    subject_names = [s[0] for s in subjects]

    # 中小企業診断士セクション
    st.markdown("### 📘 中小企業診断士")

    # 診断士セッションの入力
    sessions_to_remove = []
    for i, session in enumerate(st.session_state.shindan_sessions):
        with st.container():
            col_header, col_remove = st.columns([5, 1])

            with col_header:
                st.markdown(f"**科目 #{i+1}**")

            with col_remove:
                if len(st.session_state.shindan_sessions) > 1:
                    if st.button("🗑️", key=f"remove_shindan_{i}", help="この科目を削除"):
                        sessions_to_remove.append(i)

            col1, col2 = st.columns([1, 2])

            with col1:
                time_hours = st.number_input(
                    "学習時間（h）",
                    min_value=0.0,
                    max_value=24.0,
                    value=float(session.time_hours),
                    step=0.25,
                    key=f"shindan_time_{i}",
                    help="15分（0.25h）単位で入力できます"
                )
                session.time_hours = time_hours

            with col2:
                # 絵文字付き表示オプション作成
                subject_options = []
                subject_name_map = {}

                for subject_name in subject_names:
                    emoji = SUBJECT_EMOJI_MAP.get(subject_name, "📚")
                    display_name = f"{emoji} {subject_name}"
                    subject_options.append(display_name)
                    subject_name_map[display_name] = subject_name

                # デフォルトインデックス取得
                default_index = 0
                for idx, (display, actual) in enumerate(subject_name_map.items()):
                    if actual == session.subject:
                        default_index = idx
                        break

                selected_display = st.selectbox(
                    "科目",
                    subject_options,
                    index=default_index,
                    key=f"shindan_subject_{i}"
                )
                session.subject = subject_name_map[selected_display]

            content = st.text_area(
                "学習内容",
                value=session.content,
                placeholder="まとめシートチェック＋過去問演習、正答率83%（19/23問正解）",
                height=100,
                key=f"shindan_content_{i}",
                help="📝 投稿文にそのまま表示されます"
            )
            session.content = content

            issue = st.text_area(
                "課題・気づき",
                value=session.issue,
                placeholder="・要確認項目：無形固定資産、営業損益計算区分の勘定科目",
                height=80,
                key=f"shindan_issue_{i}",
                help="📝 投稿文にそのまま表示されます"
            )
            session.issue = issue

            st.markdown("---")

    # セッション削除処理
    for idx in reversed(sessions_to_remove):
        st.session_state.shindan_sessions.pop(idx)
        st.rerun()

    # 科目追加ボタン
    if st.button("➕ 診断士科目を追加", key="add_shindan_session"):
        st.session_state.shindan_sessions.append(
            StudySession(
                record_id=0,
                qualification='shindan_1ji',
                subject='財務・会計',
                time_hours=0.0,
                content='',
                issue=''
            )
        )
        st.rerun()

    st.divider()

    # 保存ボタン
    col1, col2 = st.columns([3, 1])

    with col1:
        if st.button("💾 保存してX投稿文を生成", type="primary", width="stretch"):
            return {
                'action': 'save_and_tweet',
                'date': target_date,
                'phase': phase,
                'shindan_sessions': st.session_state.shindan_sessions,
                'toukei_sessions': []  # 統計検定は新規入力なし
            }

    with col2:
        if st.button("💾 保存のみ", width="stretch"):
            return {
                'action': 'save_only',
                'date': target_date,
                'phase': phase,
                'shindan_sessions': st.session_state.shindan_sessions,
                'toukei_sessions': []  # 統計検定は新規入力なし
            }

    return None
