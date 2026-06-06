"""
Ankiカード: アンゾフの成長ベクトルの概念
科目: 中小企業診断士_企業経営理論
セクション: 03_成長戦略・国際経営
作成日: 2026-03-15
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS_NO_TABLE

# モデル定義
model_id = 1703030001
deck_id = 1703030002

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_成長ベクトル',
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
    css=CARD_CSS_NO_TABLE
)

my_deck = genanki.Deck(
    deck_id,
    '中小企業診断士_企業経営理論::03_成長戦略・国際経営::成長ベクトルの概念'
)

# カード内容
question = '''アンゾフが成長の方向性を「ベクトル」と呼んだ意図と、成長ベクトル（製品・市場マトリクス）の<span class="important">企業戦略論における位置づけ</span>を答えよ'''

answer = '''<b>Growth Vector / Product-Market Matrix</b>（成長ベクトル／製品・市場マトリクス）

<p>アンゾフが著書『Corporate Strategy（企業戦略論）』（1965年）で提唱したフレームワーク。</p>

<div class="formula">
<b>「ベクトル」と呼んだ意図:</b><br>
企業の成長は静的な分類ではなく、<b>方向性を持った動的な移動</b>である。製品軸（既存→新規）と市場軸（既存→新規）の2軸において、企業がどの方向へ資源を投入するかという<b>戦略的移動の方向性</b>を示す概念。
</div>

<div class="example">
<b>企業戦略論における位置づけ:</b><br>
・<b>事業ドメインの決定ツール</b>: 自社の強みが「技術（製品）」か「顧客（市場）」かを把握し、成長の方向を定める<br>
・<b>全社戦略レベル</b>の資源配分方針を決定する根本的フレームワーク<br>
・4象限（市場浸透→新市場開拓→新製品開発→多角化）は、左上から右下に向かうほどリスクが高く、既存事業との距離が遠くなる
</div>

<p><b>注意</b>: 成長ベクトルはドメインの「方向性」を示すもので、ドメインの「範囲」を示すものではない。また、各象限の選択には<b>シナジー効果</b>（販売・生産・投資・経営）の評価が不可欠である。</p>

<div class="source">出典: I. Ansoff『Corporate Strategy』(1965)、経営を学ぶ、中小企業庁</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

# .apkg出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0303_成長ベクトルの概念_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
