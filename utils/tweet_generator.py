"""
X投稿文生成ユーティリティ
"""
import os
from anthropic import Anthropic


def generate_improved_tweet(study_data: dict, cumulative_hours: float = 0) -> str:
    """学習データからエンゲージメントの高い投稿文を生成

    Args:
        study_data: {
            'date': 日付,
            'phase': フェーズ,
            'shindan_time': 診断士学習時間,
            'shindan_subject': 診断士科目,
            'shindan_content': 診断士内容,
            'shindan_issue': 診断士気づき,
            'toukei_time': 統計学習時間,
            'toukei_content': 統計内容,
            'toukei_issue': 統計気づき
        }
        cumulative_hours: 累計学習時間

    Returns:
        str: 改善された投稿文（140文字以内）
    """
    # API キー取得
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEYが設定されていません")

    client = Anthropic(api_key=api_key)

    # プロンプト作成
    prompt = f"""以下の学習記録をもとに、SNSコンサルタントの観点でエンゲージメントが高い投稿文を作成してください：

【学習情報】
日付: {study_data['date']}
フェーズ: {study_data['phase']}

診断士学習: {study_data['shindan_time']}h
科目: {study_data['shindan_subject']}
内容: {study_data['shindan_content']}
気づき: {study_data['shindan_issue']}

【フォーマット要件】
- タイトル: 「M月D日 / Day X：中小企業診断士への積み上げ」
- 成果を数値・%で強調（正答率、完了率など）
- ポジティブな気づきを1つピックアップ
- 絵文字で視覚的メリハリ（💪📊✨🎯など）
- 詳細は削除し、成果のみ残す
- ハッシュタグ: #中小企業診断士 #勉強垢
- 文字数: 140文字以内厳守（改行含む）
- 最後に累計時間を表示: 累計 {cumulative_hours:.1f}h

【重要】
- 投稿文のみを出力してください
- 説明や前置きは不要です
- 140文字を厳守してください"""

    # Claude API呼び出し
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=800,  # 長文投稿対応（4,000文字制限に対応）
        temperature=0.7,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    # 結果取得
    generated_text = message.content[0].text.strip()

    return generated_text
