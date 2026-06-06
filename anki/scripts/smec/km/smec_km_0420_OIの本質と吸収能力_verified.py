"""
Ankiカード: オープンイノベーションの本質と吸収能力
科目: 中小企業診断士_企業経営理論
セクション: 04_技術経営・イノベーション
作成日: 2026-03-16
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1704200001
deck_id = 1704200002

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_OIの本質と吸収能力',
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
    '中小企業診断士_企業経営理論::04_技術経営・イノベーション::OIの本質と吸収能力'
)

# カード内容
question = '''チェスブロウのオープンイノベーション（OI）の本質的特徴と<span class="important">よくある誤解</span>、およびコーエン＆レビンタールの<span class="important">吸収能力</span>の定義を答えよ'''

answer = '''<b>Open Innovation Essentials &amp; Absorptive Capacity</b>

<p>OIの本質を正しく理解し、類似概念との混同を避ける。</p>

<div class="formula">
<b>チェスブロウのOIの本質:</b><br>
・OIは基盤技術のR&amp;Dコラボではなく、<b>事業化レベル（ビジネスモデル）のコラボレーション</b>を促進する<br>
・外部の知識を社内に取り込み、社内の知識を外部に展開する<b>双方向の知識フロー</b><br><br>

<b>OIでないもの（よくある誤解）:</b>
<table>
<tr><th>誤解</th><th>正しい理解</th></tr>
<tr><td>OI = アウトソーシング</td><td>アウトソースは<b>効率化</b>が目的。OIは<b>イノベーション創出</b>が目的</td></tr>
<tr><td>OI = 自社R&amp;Dが不要になる</td><td>自社R&amp;Dは<b>引き続き必要</b>。外部知識を活用するには<b>吸収能力</b>が不可欠</td></tr>
<tr><td>OI = 共通規格の採用</td><td>標準化戦略とOIは別概念。OIに共通規格は必須要件ではない</td></tr>
</table>
</div>

<div class="example">
<b>吸収能力（Absorptive Capacity）:</b><br>
コーエン＆レビンタール（Cohen &amp; Levinthal, 1990）が提唱。<br><br>

<b>定義</b>: 外部の新しい情報の<b>価値を認識</b>し、それを<b>吸収（同化）</b>し、<b>商業目的に応用</b>する組織の能力。<br><br>

<b>3つの要素:</b><br>
1. <b>認識</b>: 外部知識の価値を見抜く<br>
2. <b>吸収</b>: 外部知識を社内に取り込み、自社技術と融合<br>
3. <b>応用</b>: 吸収した知識を新製品・サービスに活用<br><br>

<b>重要</b>: 吸収能力は<b>自社のR&amp;D投資の蓄積</b>によって形成される。つまりOIで外部知識を活用するには、自社でもR&amp;Dに投資し続ける必要がある。R&amp;Dを止めると吸収能力が失われ、外部の知識を活用できなくなる（<b>経路依存性</b>）。
</div>

<p><b>注意</b>: 「外部から取り込めば自社開発は不要」はOIの最大の誤解。吸収能力のない企業がOIを実践しても、外部知識の価値を認識できず、活用もできない。OIと自社R&amp;Dは<b>補完関係</b>であり、代替関係ではない。</p>

<div class="source">出典: H.W. Chesbrough (2003)、Cohen &amp; Levinthal (1990) "Absorptive Capacity"、H30第20問</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

# .apkg出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0420_OIの本質と吸収能力_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
