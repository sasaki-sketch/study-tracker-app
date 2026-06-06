"""
先行者優位と後発者優位（First-Mover / Second-Mover Advantage） - 中小企業診断士 企業戦略論
First-Mover Advantage, Second-Mover Advantage, Switching Cost, Patent

作成日: 2026-03-05
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1741185401
DECK_ID = 1741185402

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_企業戦略論_先行者優位と後発者優位',
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

# デッキ定義
deck = genanki.Deck(
    DECK_ID,
    '中小企業診断士_企業戦略論::03_競争戦略::先行者優位と後発者優位'
)

# カード内容
question = """先行者優位・後発者優位の定義、それぞれのメリット、および先行者優位が崩れる条件を答えよ"""

answer = """<b>First-Mover Advantage / Second-Mover Advantage</b>（先行者優位 / 後発者優位）

<table>
<tr><th></th><th>先行者優位</th><th>後発者優位</th></tr>
<tr><td><b>定義</b></td><td>早期参入により得られる競争上の有利性</td><td>先行者の投資から学び、市場確認後に参入する有利性</td></tr>
<tr><td><b>メリット</b></td><td>ブランド認知の先制構築、経験曲線効果、希少資源の優先確保、顧客ロイヤルティ</td><td>需要の不確実性を見極められる、開発・広告コスト削減、先行者の失敗から学習</td></tr>
</table>

<b>先行者優位が維持される条件</b>:
<ul>
<li><b>スイッチングコストが高い</b>（顧客が乗り換えにくい）</li>
<li>技術発展が漸進的で、後発者が差別化しにくい</li>
</ul>

<b>先行者優位が崩れる条件</b>:
<ul>
<li>非連続的な技術革新が頻繁に起こる場合</li>
<li>顧客嗜好が急速に変化する場合</li>
<li>後発者が先行者の投資に「ただ乗り」できる場合</li>
</ul>

<div class="important">注意（特許と先行者優位）:</div>
特許だけでは先行者優位は維持されにくい。研究によれば、特許の約60%は公開から約4年で特許権を侵害せずに模倣（回避設計）される。製薬等の例外を除き、多くの産業では競合は先行者コストの平均65%程度で模倣可能であり、特許単独では持続的な競争優位にならない（R5第6問で出題）

<div class="source">出典: 一発合格まとめシート R5第6問解説、バーニー『企業戦略論』</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/xx/smec_xx_0302_先行者優位と後発者優位_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
