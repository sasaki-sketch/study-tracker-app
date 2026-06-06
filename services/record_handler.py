"""
学習記録の保存・投稿文生成処理（複数科目対応版）
"""
import streamlit as st
import pyperclip
from typing import List
from datetime import date
from urllib.parse import quote

from models.record import StudyRecord, StudySession
from services.database import DatabaseService
from services.obsidian import ObsidianService
from services.tweet import TweetService
from utils.tweet_prompts import generate_tweet_prompt_from_sessions, generate_tweet_text_from_prompt
from components.tweet_char_counter import show_char_counter


def save_record_with_sessions(
    target_date: date,
    phase: str,
    shindan_sessions: List[StudySession],
    toukei_sessions: List[StudySession],
    db_service: DatabaseService
) -> int:
    """学習記録とセッションを保存

    Args:
        target_date: 学習日
        phase: フェーズ
        shindan_sessions: 診断士セッションリスト
        toukei_sessions: 統計検定セッションリスト
        db_service: データベースサービス

    Returns:
        保存したレコードID
    """
    # 合計時間を計算
    shindan_total = sum(s.time_hours for s in shindan_sessions)
    toukei_total = sum(s.time_hours for s in toukei_sessions)

    # レコード作成（レガシー形式 - 後方互換性のため）
    record = StudyRecord(
        date=target_date,
        phase=phase,
        shindan_time=shindan_total,
        shindan_subject=shindan_sessions[0].subject if shindan_sessions else '',
        shindan_content='',  # セッション側に記録
        shindan_issue='',    # セッション側に記録
        toukei_time=toukei_total,
        toukei_content='',   # セッション側に記録
        toukei_issue=''      # セッション側に記録
    )

    # レコード保存
    record_id = db_service.save_record(record)
    record.id = record_id

    # セッション保存
    all_sessions = []

    for session in shindan_sessions:
        session.record_id = record_id
        all_sessions.append(session)

    for session in toukei_sessions:
        session.record_id = record_id
        all_sessions.append(session)

    db_service.save_study_sessions(record_id, all_sessions)

    return record_id


def generate_and_display_tweet(
    record: StudyRecord,
    sessions: List[StudySession],
    db_service: DatabaseService,
    obsidian_service: ObsidianService
):
    """投稿文を生成して表示

    Args:
        record: 学習記録
        sessions: 学習セッションリスト
        db_service: データベースサービス
        obsidian_service: Obsidianサービス
    """
    # 統計取得
    stats = db_service.get_cumulative_stats()

    # Obsidian出力
    try:
        file_path = obsidian_service.export_to_obsidian(record, stats)
        st.success(f"✅ Obsidianファイルを出力: {file_path.name}")
    except Exception as e:
        st.warning(f"⚠️ Obsidian出力エラー: {str(e)}")

    # プロンプト生成
    prompt = generate_tweet_prompt_from_sessions(record, stats, sessions)

    # 投稿文生成
    tweet_text = generate_tweet_text_from_prompt(prompt)

    # クリップボードコピー
    try:
        pyperclip.copy(tweet_text)
        st.info("✅ クリップボードにコピーしました")
    except:
        st.warning("⚠️ クリップボードへのコピーに失敗しました")

    # 投稿文表示
    st.subheader("📱 X投稿文")

    # タブで切り替え
    tab1, tab2 = st.tabs(["📝 投稿文", "🤖 プロンプト"])

    with tab1:
        # 投稿文プレビュー（編集可能）
        tweet_preview = st.text_area(
            "投稿文（編集可能）",
            value=tweet_text,
            height=400,
            key="tweet_preview_main"
        )

        # 文字数カウント
        show_char_counter(tweet_preview)

        # アクションボタン
        col1, col2, col3 = st.columns(3)

        with col1:
            tweet_url = f"https://x.com/intent/tweet?text={quote(tweet_preview)}"
            st.link_button("🐦 Xで投稿する", tweet_url, width="stretch", type="primary")

        with col2:
            if st.button("📋 コピー", key="copy_tweet_main", width="stretch"):
                try:
                    pyperclip.copy(tweet_preview)
                    st.toast("✅ コピーしました！", icon="✅")
                except:
                    st.error("⚠️ コピーに失敗しました")

        with col3:
            if st.button("🔄 再読込", key="reload_tweet", width="stretch"):
                st.rerun()

    with tab2:
        # プロンプト表示・編集
        st.info("💡 このプロンプトをClaude AIに渡すと、投稿文が生成されます")

        edited_prompt = st.text_area(
            "プロンプト（編集可能）",
            value=prompt,
            height=500,
            key="prompt_editor_main"
        )

        col1, col2 = st.columns(2)

        with col1:
            if st.button("🔄 AI再生成", key="regenerate_ai", width="stretch", type="primary"):
                from anthropic import Anthropic
                import os

                with st.spinner("🤖 AIが投稿文を作成中..."):
                    try:
                        # ⚠️⚠️⚠️ CRITICAL: ONLY ALLOWED USE OF ANTHROPIC API IN THIS PROJECT ⚠️⚠️⚠️
                        # This is the ONLY place where anthropic.Anthropic() is permitted
                        # Do NOT use Anthropic API anywhere else in this codebase
                        # API usage is restricted to X post generation ONLY
                        api_key = os.environ.get("ANTHROPIC_API_KEY")
                        if not api_key:
                            raise ValueError("ANTHROPIC_API_KEYが設定されていません")

                        client = Anthropic(api_key=api_key)
                        message = client.messages.create(
                            model="claude-sonnet-4-20250514",
                            max_tokens=1200,
                            temperature=0.7,
                            messages=[{"role": "user", "content": edited_prompt}]
                        )

                        improved_tweet = message.content[0].text.strip()

                        # セッション状態に保存
                        st.session_state.generated_tweet = improved_tweet
                        st.success("✅ 投稿文を再生成しました！")
                        st.rerun()

                    except ValueError as e:
                        st.error(f"⚠️ {str(e)}")
                        st.info("💡 ANTHROPIC_API_KEYを環境変数に設定してください")
                    except Exception as e:
                        st.error(f"⚠️ 生成エラー: {str(e)}")

        with col2:
            if st.button("📋 プロンプトをコピー", key="copy_prompt_main", width="stretch"):
                try:
                    pyperclip.copy(edited_prompt)
                    st.toast("✅ プロンプトをコピー！", icon="📋")
                except:
                    st.error("⚠️ コピーに失敗しました")
