"""
ドメインの定義方法（物理的定義と機能的定義） - 中小企業診断士 企業戦略論
Physical vs Functional Domain Definition (Levitt)

作成日: 2026-03-03
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

MODEL_ID = 1740928401
DECK_ID = 1740928402

model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_企業戦略論_ドメインの定義方法',
    fields=[{'name': 'Question'}, {'name': 'Answer'}],
    templates=[{
        'name': 'Card 1',
        'qfmt': '<div class="question">{{Question}}</div>',
        'afmt': '{{FrontSide}}<hr id="answer"><div class="answer">{{Answer}}</div>',
    }],
    css=CARD_CSS
)

deck = genanki.Deck(DECK_ID, '中小企業診断士_企業戦略論::01_ドメイン::ドメインの定義方法')

question = """ドメインの物理的定義と機能的定義の違い、およびレビットのマーケティング近視眼を答えよ"""

answer = """<b>Physical vs Functional Definition</b>（物理的定義と機能的定義）

<table>
<tr><th></th><th>物理的定義</th><th>機能的定義</th></tr>
<tr><td>視点</td><td>製品・サービスそのもの</td><td><b>顧客ニーズ</b></td></tr>
<tr><td>例</td><td>「映画会社」</td><td>「<b>娯楽</b>の提供」</td></tr>
<tr><td>利点</td><td>わかりやすい</td><td>将来の発展性が高い</td></tr>
<tr><td>欠点</td><td>事業拡大が困難</td><td>範囲が曖昧になりやすい</td></tr>
<tr><td>エーベルとの対応</td><td><b>技術</b>軸に近い</td><td><b>顧客機能</b>軸に近い</td></tr>
</table>

<b>Marketing Myopia</b>（マーケティング近視眼）:
<ul>
<li><b>提唱者</b>: セオドア・レビット（1960年）</li>
<li>物理的定義に固執し、製品視点でしかドメインを捉えられない状態</li>
<li>例: 米国鉄道会社が「鉄道業」と定義 → 「<b>輸送業</b>」と定義すべきだった</li>
</ul>

<div class="important">注意:</div>
<ul>
<li>機能的定義が常に優れているわけではない（広すぎると<b>経営資源の分散</b>を招く）</li>
<li>試験では「物理的定義のデメリット → 近視眼」の流れが頻出</li>
</ul>

<div class="source">出典: たかぴーの中小企業診断士試験 攻略ブログ、T. Levitt "Marketing Myopia" (1960)</div>
"""

note = genanki.Note(model=model, fields=[question, answer])
deck.add_note(note)

output_path = '/Users/sasaki/study_app/anki/scripts/smec/st/smec_st_0104_ドメインの定義方法_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
