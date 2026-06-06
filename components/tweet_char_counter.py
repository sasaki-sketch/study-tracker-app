"""
X投稿文の文字数カウンター共通コンポーネント
"""
import streamlit as st

# 定数（X Premium Basic対応：4,000文字）
# 注意: X/Twitterの文字数制限
#   - 無料アカウント: 280文字
#   - Premium Basic: 4,000文字
#   - Premium+: 25,000文字
# 現在はPremium Basic想定で4,000文字に設定
TWEET_CHAR_LIMIT = 4000
WARNING_THRESHOLD = 3800  # 残り200文字で警告


def show_char_counter(tweet_text: str) -> None:
    """
    投稿文の文字数をカウントして表示する（X Premium Basic対応）

    Args:
        tweet_text: 投稿文のテキスト
    """
    char_count = len(tweet_text)
    char_percentage = min((char_count / TWEET_CHAR_LIMIT) * 100, 100)
    remaining = TWEET_CHAR_LIMIT - char_count

    st.markdown("**文字数チェック**")

    if char_count > TWEET_CHAR_LIMIT:
        st.progress(int(char_percentage))
        st.error(f"⚠️ {char_count - TWEET_CHAR_LIMIT}文字オーバー（{char_count:,}/{TWEET_CHAR_LIMIT:,}）")
    elif char_count > WARNING_THRESHOLD:
        st.progress(int(char_percentage))
        st.warning(f"⚠️ 残り{remaining}文字（{char_count:,}/{TWEET_CHAR_LIMIT:,}）")
    else:
        st.progress(int(char_percentage))
        st.success(f"✅ {char_count:,}/{TWEET_CHAR_LIMIT:,}文字（残り{remaining:,}文字）")
