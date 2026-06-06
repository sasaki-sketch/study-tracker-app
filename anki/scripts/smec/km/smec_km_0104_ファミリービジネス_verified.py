"""
Ankiカード: ファミリービジネス（スリーサークルモデル）
科目: 中小企業診断士_企業経営理論
セクション: 01_経営戦略（ドメイン・全社戦略）
作成日: 2026-03-20
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1701040101
deck_id = 1701040102

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_ファミリービジネス',
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
    '中小企業診断士_企業経営理論::01_経営戦略::ファミリービジネス'
)

question = '''<span class="important">ファミリービジネス</span>の定義・スリーサークルモデル・特徴を答えよ'''

answer = '''<b>Family Business</b>（ファミリービジネス）

<p>同族（ファミリー）が所有・経営に関与する企業。日本企業の約97%が該当。</p>

<div class="formula">
<b>スリーサークルモデル（Tagiuri &amp; Davis, 1982）:</b><br>
<b>ファミリー</b>（Family）・<b>オーナーシップ</b>（Ownership）・<b>ビジネス</b>（Business）の3つの円が重なり、7つの領域を形成。<br><br>
<table>
<tr><th>領域</th><th>立場</th><th>例</th></tr>
<tr><td>①</td><td>オーナーのみ</td><td>株を持つだけの外部投資家</td></tr>
<tr><td>②</td><td>ビジネスのみ</td><td>非同族の従業員</td></tr>
<tr><td>③</td><td>ファミリーのみ</td><td>経営に関与しない親族</td></tr>
<tr><td>④</td><td>オーナー＋ビジネス</td><td>株を持つ非同族の経営幹部</td></tr>
<tr><td>⑤</td><td>ファミリー＋ビジネス</td><td>株を持たず働く親族</td></tr>
<tr><td>⑥</td><td>ファミリー＋オーナー</td><td>株を持つが働かない親族</td></tr>
<tr><td><b>⑦</b></td><td><b>3つ全て</b></td><td><b>株を持ち経営する創業家一族</b></td></tr>
</table>
</div>

<div class="formula">
<b>ファミリービジネスの特徴:</b>
<table>
<tr><th>強み</th><th>弱み</th></tr>
<tr><td>長期的視点での経営</td><td>経営の閉鎖性・属人化</td></tr>
<tr><td>迅速な意思決定</td><td>後継者問題</td></tr>
<tr><td>強い企業文化・理念</td><td>公私混同のリスク</td></tr>
<tr><td>ステークホルダーとの信頼関係</td><td>ファミリー間の対立</td></tr>
</table>
</div>

<div class="example">
<b>試験での問われ方:</b><br>
・スリーサークルの各領域に該当する<b>人物の分類</b><br>
・「ファミリービジネスは少数派」→ <b>×</b> 日本企業の<b>大多数</b><br>
・各領域間の<b>利害対立</b>（例: ⑥の株主 vs ②の従業員）
</div>

<div class="source">出典: Tagiuri &amp; Davis (1982)、中小企業診断士試験</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0104_ファミリービジネス_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
