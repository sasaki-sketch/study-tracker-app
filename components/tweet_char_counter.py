"""
X投稿文の文字数カウンター共通コンポーネント
"""
import streamlit as st

# 定数
TWEET_CHAR_LIMIT = 140


def show_char_counter(tweet_text: str) -> None:
    """
    投稿文の文字数をカウントして表示する

    Args:
        tweet_text: 投稿文のテキスト
    """
    char_count = len(tweet_text)
    char_percentage = min((char_count / TWEET_CHAR_LIMIT) * 100, 100)

    st.markdown("**文字数チェック**")

    if char_count > TWEET_CHAR_LIMIT:
        st.progress(int(char_percentage))
        st.error(f"⚠️ {char_count - TWEET_CHAR_LIMIT}文字オーバー（{char_count}/{TWEET_CHAR_LIMIT}）")
    elif char_count > 120:
        st.progress(int(char_percentage))
        st.warning(f"⚠️ 残り{TWEET_CHAR_LIMIT - char_count}文字（{char_count}/{TWEET_CHAR_LIMIT}）")
    else:
        st.progress(int(char_percentage))
        st.success(f"✅ {char_count}/{TWEET_CHAR_LIMIT}文字")
