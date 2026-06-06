"""
Ankiカード: コンティンジェンシープラン
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
model_id = 1709010102
model = genanki.Model(
    model_id,
    'SMEC_KM_コンティンジェンシープラン',
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
deck_id = 2709010102
deck = genanki.Deck(
    deck_id,
    '中小企業診断士_企業経営理論::01_経営戦略::コンティンジェンシープラン',
)

# カード作成
question = 'コンティンジェンシープランの定義・BCPとの違いを答えよ'

answer = '''<b>Contingency Plan</b>（コンティンジェンシープラン / 緊急時対応計画）

<ul>
<li><b>定義</b>: 不測の事態（自然災害、テロ、システム障害等）の発生に備え、被害を最小限に抑え迅速に通常業務へ復旧するための<b>行動指針・緊急対策マニュアル</b></li>
<li><b>語源</b>: Contingency =「偶発・不慮の事故」</li>
<li><b>位置づけ</b>: <b>クライシスマネジメント</b>（事後対応）の中の具体的な計画手法</li>
</ul>

<div class="mnemonic">
<b>階層関係</b><br>
リスクマネジメント（事前・予防）<br>
クライシスマネジメント（事後・対応）<br>
　├ <b>コンティンジェンシープラン</b>（短期・初動対応）<br>
　└ BCP（中長期・事業継続）
</div>

<div class="formula">
<b>BCPとの比較</b>
<table>
<tr><th></th><th>コンティンジェンシープラン</th><th>BCP</th></tr>
<tr><td><b>英語</b></td><td>Contingency Plan</td><td>Business Continuity Plan</td></tr>
<tr><td><b>重点</b></td><td>緊急時の<b>対応</b></td><td>事業の<b>継続</b></td></tr>
<tr><td><b>期間</b></td><td>短期（発生直後）</td><td>中長期（復旧まで）</td></tr>
<tr><td><b>BIA</b></td><td>実施<b>しない</b></td><td>実施<b>する</b></td></tr>
<tr><td><b>目的</b></td><td>被害最小化・初動対応</td><td>優先業務の継続・段階的復旧</td></tr>
</table>
</div>

<div class="example">
<b>BIA（Business Impact Analysis: 事業インパクト分析）</b><br>
業務停止による影響度を分析し、復旧の優先順位を決定する手法。BCPでは必須だがコンティンジェンシープランでは行わない点が最大の違い。
</div>

<b>注意</b>: コンティンジェンシープランは「緊急時の初動対応」、BCPは「事業継続の中長期計画」という対比が頻出。両者ともクライシスマネジメントの具体的手法である点を押さえること。

<div class="source">出典: FastAlert、カオナビ、NEC</div>'''

note = genanki.Note(
    model=model,
    fields=[question, answer],
)

deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0102_コンティンジェンシープラン_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f'Generated: {output_path}')
