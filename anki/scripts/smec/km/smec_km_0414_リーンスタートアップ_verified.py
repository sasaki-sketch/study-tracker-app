"""
Ankiカード: リーンスタートアップ
科目: 中小企業診断士_企業経営理論
セクション: 04_技術経営・イノベーション
作成日: 2026-03-16
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1704140001
deck_id = 1704140002

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_リーンスタートアップ',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '<div class="question">{{Question}}</div>',
            'afmt': '{{FrontSide}}<hr id="answer"><div class="answer">{{Answer}}</div>',
        },
    ],
    css=CARD_CSS
)

my_deck = genanki.Deck(
    deck_id,
    '中小企業診断士_企業経営理論::04_技術経営・イノベーション::リーンスタートアップ'
)

# カード内容
question = '''エリック・リースが提唱したリーンスタートアップの定義、<span class="important">BMLループ（構築・計測・学習）</span>、<span class="important">MVP</span>、および<span class="important">ピボット</span>の概念を答えよ'''

answer = '''<b>Lean Startup</b>（リーンスタートアップ）

<p>エリック・リース（E. Ries, 2011）が提唱。トヨタ生産方式の「ムダ取り」に着想を得た、<b>最小限のコストと短いサイクルで仮説検証を繰り返す</b>事業開発手法。</p>

<div class="formula">
<b>BMLループ（Build-Measure-Learn）:</b><br>
構築（Build）→ 計測（Measure）→ 学習（Learn）→ 再び構築へ…

<table>
<tr><th>ステップ</th><th>内容</th><th>要点</th></tr>
<tr><td><b>構築（Build）</b></td><td>仮説に基づき<b>MVP</b>を素早く作る</td><td>完璧を目指さない</td></tr>
<tr><td><b>計測（Measure）</b></td><td>MVPを顧客に提供し、反応を<b>データで計測</b></td><td>虚栄の指標ではなく行動指標を使う</td></tr>
<tr><td><b>学習（Learn）</b></td><td>データから仮説の正否を判断し、<b>続行 or ピボット</b>を決定</td><td>検証された学び（Validated Learning）</td></tr>
</table>
</div>

<div class="example">
<b>MVP（Minimum Viable Product）= 実用最小限の製品:</b><br>
顧客に価値を提供できる<b>最小限の機能</b>を持った試作品。完成品ではなく、仮説を検証するための「学習ツール」。<br><br>
・例: Dropbox（製品開発前に操作デモ動画だけ公開 → 需要を確認してから開発）<br>
・例: Zappos（在庫を持たず、靴屋の写真を撮ってサイトに掲載 → 注文が入ったら買いに行く）<br><br>

<b>ピボット（Pivot）= 方向転換:</b><br>
BMLループの学習段階で仮説が誤りと判明した場合、戦略の根本的な方向転換を行うこと。<br><br>
・例: Instagram（元は位置情報チェックインアプリ → 写真共有機能だけが人気 → 写真SNSにピボット）
</div>

<p><b>注意</b>: リーンスタートアップ ≠ 「安く作る」。本質は<b>不確実性の高い状況で、学習スピードを最大化する</b>こと。MVPは「最小限の製品」ではなく「仮説検証に最小限必要な製品」であり、目的は販売ではなく学習。従来型の事業計画（計画→実行）とは対照的に、仮説→検証→学習の反復で事業を構築する。</p>

<div class="example">
<b>試験頻出の引っかけポイント（R7第11問）:</b><br>
・ピボットの<b>「最適なタイミングを特定化する手法」は存在しない</b>（BMLループの結果から判断するもの）<br>
・<b>アーリーアダプター</b>を巻き込むことが推奨される<br>
・新規性が高く顧客の存在が不確実な製品に適しており、<b>幅広い産業に応用可能</b><br>
・「リーン」は<b>トヨタ生産方式</b>から影響を受けた考え方
</div>

<div class="source">出典: E. Ries (2011)『The Lean Startup』、カオナビ リーンスタートアップ解説、モンスターラボ、企業経営理論 R7第11問</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

# .apkg出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0414_リーンスタートアップ_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
