"""
Ankiカード: ダニングのOLIパラダイム（折衷理論）
科目: 中小企業診断士_企業経営理論
セクション: 03_成長戦略・国際経営
作成日: 2026-03-20
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1703030301
deck_id = 1703030302

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_OLIパラダイム',
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
    '中小企業診断士_企業経営理論::03_成長戦略・国際経営::OLIパラダイム'
)

# カード内容
question = '''J.ダニングの折衷理論（<span class="important">OLIパラダイム</span>）の3つの優位性と、組み合わせによる海外進出形態の選択を答えよ'''

answer = '''<b>OLI Paradigm / Eclectic Theory</b>（折衷理論）

<p>J.ダニング（J.H. Dunning）が提唱。3つの優位性の組み合わせで最適な海外進出形態を決定。</p>

<div class="formula">
<table>
<tr><th>略称</th><th>優位性</th><th>内容</th></tr>
<tr><td><b>O</b></td><td><b>所有優位性</b>（Ownership）</td><td>技術・ブランド・ノウハウ等の企業固有の強み</td></tr>
<tr><td><b>L</b></td><td><b>立地優位性</b>（Location）</td><td>進出先の市場規模・コスト・制度等の魅力</td></tr>
<tr><td><b>I</b></td><td><b>内部化優位性</b>（Internalization）</td><td>ライセンス等で外部に任せるより自社で行う方が有利</td></tr>
</table>
</div>

<div class="formula">
<b>組み合わせと進出形態:</b>
<table>
<tr><th>O（所有）</th><th>L（立地）</th><th>I（内部化）</th><th>→ 最適な形態</th></tr>
<tr><td style="text-align:center">○</td><td style="text-align:center">○</td><td style="text-align:center">○</td><td><b>海外直接投資（FDI）</b></td></tr>
<tr><td style="text-align:center">○</td><td style="text-align:center">×</td><td style="text-align:center">○</td><td><b>輸出</b></td></tr>
<tr><td style="text-align:center">○</td><td style="text-align:center">×</td><td style="text-align:center">×</td><td><b>ライセンシング</b></td></tr>
<tr><td style="text-align:center">×</td><td style="text-align:center">-</td><td style="text-align:center">-</td><td><b>海外進出しない</b></td></tr>
</table>
</div>

<div class="mnemonic">
<b>覚え方:</b><br>
・<b>O（所有）は大前提</b>（なければ進出不可）<br>
・<b>L</b>＝「現地で<b>作る</b>理由があるか」→ あればFDI、なければ国内生産（輸出）<br>
・<b>I</b>＝「<b>自分で</b>やる理由があるか」→ あれば自社運営、なければライセンス
</div>

<div class="source">出典: J.H. Dunning、中小企業診断士試験 R7第12問</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

# .apkg出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0303_OLIパラダイム_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
