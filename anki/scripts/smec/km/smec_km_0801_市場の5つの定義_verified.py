"""
Ankiカード: コトラーによる市場の5つの定義
科目: 中小企業診断士_企業経営理論
セクション: 08 マーケティング概論・戦略
作成日: 2026-03-14
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# --- モデル定義 ---
MODEL_ID = 1710390801
DECK_ID = 1610390801

model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_企業経営理論_市場の5つの定義',
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

# --- デッキ定義 ---
deck = genanki.Deck(DECK_ID, '中小企業診断士_企業経営理論::08_マーケティング概論::市場の5つの定義')

# --- カード ---
question = """コトラーによる市場の5つの定義（レベル）を答えよ"""

answer = """<b>Kotler's Five Levels of Market Definition</b>

市場は広い順に以下の5つのレベルで定義される（包含関係: ①⊃②⊃③⊃④⊃⑤）:

<b>① 潜在市場（Potential Market）</b>
<ul><li>その製品・サービスに<b>関心を持つ</b>消費者全体</li></ul>

<b>② 有効市場（Available Market）</b>
<ul><li>関心に加え、<b>所得・アクセス手段</b>がある消費者</li></ul>

<b>③ 適格有効市場（Qualified Available Market）</b>
<ul><li>有効市場のうち、<b>法的・資格的条件</b>を満たす消費者</li></ul>

<b>④ 対象市場（Target Market）</b>
<ul><li>適格有効市場から企業が<b>ターゲットとして選択</b>した消費者</li></ul>

<b>⑤ 浸透市場（Penetrated Market）</b>
<ul><li>実際に<b>購入済み</b>の消費者</li></ul>

<div class="example">
<b>具体例（ビール市場）:</b><br>
① 潜在市場: ビールに興味がある人全体<br>
② 有効市場: 購入できる所得があり、販売店にアクセスできる人<br>
③ 適格有効市場: ②のうち飲酒可能年齢（20歳以上）の人<br>
④ 対象市場: ③のうち自社が狙う層（例: 30代男性のプレミアム志向）<br>
⑤ 浸透市場: 実際に自社ビールを購入した人
</div>

<div class="important">潜在市場が最も広く、浸透市場が最も狭い。試験では各レベルの定義の入れ替え問題に注意。「適格」は法的・年齢的制約がポイント。</div>

<div class="source">出典: Kotler『Marketing Management』</div>"""

note = genanki.Note(model=model, fields=[question, answer])
deck.add_note(note)

# --- パッケージ出力 ---
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0801_市場の5つの定義_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
