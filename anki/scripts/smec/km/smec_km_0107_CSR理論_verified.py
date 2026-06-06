"""
Ankiカード: CSR理論（キャロル・フリードマン・ドラッカー・フリーマン）
科目: 中小企業診断士_企業経営理論
セクション: 01_経営戦略（ドメイン・全社戦略）
作成日: 2026-03-21
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1701070101
deck_id = 1701070102

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_CSR理論',
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
    '中小企業診断士_企業経営理論::01_経営戦略::CSR理論'
)

question = '''企業の社会的責任（CSR）に関する<span class="important">主要学者の理論</span>（キャロル・フリードマン・ドラッカー・フリーマン）を答えよ'''

answer = '''<b>CSR Theories by Key Scholars</b>

<div class="formula">
<b>キャロルのCSRピラミッド（A. Carroll, 1991）:</b><br><br>
<table>
<tr><td style="text-align:center; background-color:#fff3cd; color:#856404">△ <b>フィランソロピー的責任</b>（あれば望ましい）</td></tr>
<tr><td style="text-align:center; background-color:#d4edda; color:#155724"><b>倫理的責任</b>（社会が期待する行動）</td></tr>
<tr><td style="text-align:center; background-color:#cce5ff; color:#004085"><b>法的責任</b>（社会が要求するルール）</td></tr>
<tr><td style="text-align:center; background-color:#f0f4f8; color:#1a1a1a"><b>経済的責任</b>（利益を上げる）← <span class="important">土台。すべての基盤</span></td></tr>
</table>
</div>

<div class="mnemonic">
<b>覚え方:</b> 下から「<b>けほりふ</b>」（経→法→倫→フィランソロピー）
</div>

<div class="formula">
<table>
<tr><th>学者</th><th>主張</th><th>試験での引っかけ</th></tr>
<tr><td><b>A.キャロル</b></td><td>CSRを4層のピラミッドで整理。<b>経済的責任が土台</b></td><td>「社会貢献が土台」→ <b>×</b> 土台は経済的責任</td></tr>
<tr><td><b>M.フリードマン</b></td><td>企業のCSR＝<b>株主利益の最大化</b>。ただし<b>法律・社会規範の遵守が前提</b></td><td>「法律無視で利益追求」→ <b>×</b> ルール遵守が前提</td></tr>
<tr><td><b>P.ドラッカー</b></td><td>CSRは<b>新しい課題ではない</b>。19世紀の企業家（カーネギー等）も意識していた</td><td>「CSRは現代の新しい課題」→ <b>×</b> 昔からあった</td></tr>
<tr><td><b>R.フリーマン</b></td><td>ステークホルダー理論。企業とSHは<b>協力的・相互依存的関係</b></td><td>「企業とSHは対立関係」→ <b>×</b> 協力関係を重視</td></tr>
</table>
</div>

<div class="source">出典: 中小企業診断士試験 R5第13問</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0107_CSR理論_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
