"""
Ankiカード: アンゾフのシナジー効果の4分類
科目: 中小企業診断士_企業経営理論
セクション: 03_成長戦略・国際経営
作成日: 2026-03-15
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1703020001
deck_id = 1703020002

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_シナジー効果',
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
    '中小企業診断士_企業経営理論::03_成長戦略・国際経営::シナジー効果の4分類'
)

# カード内容
question = '''アンゾフが提唱したシナジー効果の<span class="important">4分類</span>の定義と、多角化戦略との関係を答えよ'''

answer = '''<b>Synergy</b>（シナジー効果／相乗効果）

<p>アンゾフが提唱した、事業の組み合わせにより全体の価値が個別の総和を上回る効果（1+1&gt;2）。</p>

<div class="formula">
<table>
<tr><th>分類</th><th>定義</th><th>具体例</th></tr>
<tr><td><b>販売シナジー</b></td><td>流通経路・販売組織・倉庫等の共有</td><td>共通の販売チャネルで新製品を展開</td></tr>
<tr><td><b>生産シナジー</b></td><td>生産設備・要員・原材料調達の共有</td><td>一括購入によるコスト削減</td></tr>
<tr><td><b>投資シナジー</b></td><td>研究開発成果・技術・ノウハウの共有</td><td>R&amp;D費用の分散、技術の転用</td></tr>
<tr><td><b>経営シナジー</b></td><td>経営ノウハウ・問題解決手法の共有</td><td>経営管理能力の新事業への適用</td></tr>
</table>
</div>

<div class="example">
<b>多角化戦略との関係:</b><br>
・<b>水平型多角化</b>: 販売シナジーが高い（既存の流通経路を活用）<br>
・<b>垂直型多角化</b>: 生産・投資シナジーが高い（バリューチェーン統合）<br>
・<b>集中型多角化</b>: 投資シナジーが高い（既存技術の転用）<br>
・<b>集成型多角化</b>: シナジーが最も低い（無関連分野への進出）
</div>

<p><b>注意</b>: 多角化の方向性を決定する際、シナジー効果の大きさとリスクはトレードオフの関係にある。シナジーが高い多角化ほどリスクは低く、集成型のようにシナジーが低い多角化ほどリスクが高い。</p>

<div class="source">出典: fundbook シナジー効果解説、カオナビ シナジー効果</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

# .apkg出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0302_シナジー効果の4分類_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
