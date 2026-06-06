"""
情報的経営資源 - 中小企業診断士 企業戦略論
Information-based Management Resources (Invisible Assets)

作成日: 2026-03-03
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

MODEL_ID = 1740928501
DECK_ID = 1740928502

model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_企業戦略論_情報的経営資源',
    fields=[{'name': 'Question'}, {'name': 'Answer'}],
    templates=[{
        'name': 'Card 1',
        'qfmt': '<div class="question">{{Question}}</div>',
        'afmt': '{{FrontSide}}<hr id="answer"><div class="answer">{{Answer}}</div>',
    }],
    css=CARD_CSS
)

deck = genanki.Deck(DECK_ID, '中小企業診断士_企業戦略論::02_経営資源::情報的経営資源')

question = """情報的経営資源の定義・分類・特徴を答えよ"""

answer = """<b>Information-based Management Resources</b>（情報的経営資源 / 見えざる資産）

<b>提唱者</b>: 伊丹敬之（一橋大学名誉教授）

経営資源のうち、物理的実体を持たない<b>無形の資源</b>。「見えざる資産」とも呼ばれる。

<b>分類</b>:
<table>
<tr><th></th><th>内部蓄積</th><th>外部蓄積</th></tr>
<tr><td>例</td><td>技術、ノウハウ、顧客情報</td><td>ブランド、企業イメージ、信用</td></tr>
</table>

<b>3つの特徴</b>:
<table>
<tr><th>#</th><th>特徴</th><th>説明</th></tr>
<tr><td>1</td><td><b>同時多重利用</b></td><td>何度使っても減らず、複数分野で同時に活用可能</td></tr>
<tr><td>2</td><td><b>自然蓄積性</b></td><td>日常の事業活動で自然に蓄積される</td></tr>
<tr><td>3</td><td><b>消去困難性</b></td><td>一度獲得すると意識的に消すのが難しい</td></tr>
</table>

<div class="important">注意:</div>
<ul>
<li>ヒト・モノ・カネとの最大の違いは「使っても減らない」点（試験頻出）</li>
<li>汎用性が<b>低い</b>情報ほど競争優位性が<b>高い</b></li>
</ul>

<div class="source">出典: コトバンク「情報的経営資源」、経営学辞典</div>
"""

note = genanki.Note(model=model, fields=[question, answer])
deck.add_note(note)

output_path = '/Users/sasaki/study_app/anki/scripts/smec/st/smec_st_0201_情報的経営資源_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
