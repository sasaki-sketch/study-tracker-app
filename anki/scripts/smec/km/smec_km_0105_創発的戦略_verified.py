"""
Ankiカード: 創発的戦略
科目: 中小企業診断士_企業経営理論
セクション: 01_経営戦略
作成日: 2026-03-07
検証済み: Yes
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1709010105
model = genanki.Model(
    model_id,
    'SMEC_KM_創発的戦略',
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
    css=CARD_CSS,
)

# デッキ定義
deck_id = 2709010105
deck = genanki.Deck(
    deck_id,
    '中小企業診断士_企業経営理論::01_経営戦略::創発的戦略',
)

# カード作成
question = 'ミンツバーグの創発的戦略と意図的戦略の定義・違い・関係を答えよ'

answer = '''<b>Emergent Strategy / Deliberate Strategy</b>（創発的戦略 / 意図的戦略）

<ul>
<li><b>提唱者</b>: H.ミンツバーグ（Henry Mintzberg）</li>
<li><b>主張</b>: 戦略は計画的に策定されると同時に、創発的に形成されなければならない</li>
</ul>

<div class="formula">
<b>意図的戦略と創発的戦略の比較</b>
<table>
<tr><th></th><th>意図的戦略</th><th>創発的戦略</th></tr>
<tr><td><b>英語</b></td><td>Deliberate Strategy</td><td>Emergent Strategy</td></tr>
<tr><td><b>定義</b></td><td>事前に明確な目標・計画に基づき策定</td><td>偶発的な環境変化に対応し事後的に形成</td></tr>
<tr><td><b>性質</b></td><td>トップダウン・計画的</td><td>ボトムアップ・適応的</td></tr>
<tr><td><b>前提</b></td><td>環境予測が可能</td><td>環境は不確実で変化する</td></tr>
</table>
</div>

<div class="mnemonic">
<b>戦略の形成プロセス</b><br>
意図された戦略 → 一部は<b>実現</b>（意図的戦略）/ 一部は<b>未実現</b>で消滅<br>
偶発的な行動・学習 → <b>創発的戦略</b>として形成<br><br>
<b>実現された戦略</b> ＝ 意図的戦略 ＋ 創発的戦略
</div>

<b>注意</b>: アンゾフの<b>計画的戦略論</b>（事前に分析・計画）との対比で出題されやすい。ミンツバーグは「戦略は計画だけでなく、現場の行動や学習からも生まれる」と主張し、計画偏重を批判した。

<div class="source">出典: ミライオン、経営セカンドオピニオン協会、Study Journey</div>'''

note = genanki.Note(
    model=model,
    fields=[question, answer],
)

deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0105_創発的戦略_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f'Generated: {output_path}')
