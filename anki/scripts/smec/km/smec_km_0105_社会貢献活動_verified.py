"""
Ankiカード: 企業の社会貢献活動の形態
科目: 中小企業診断士_企業経営理論
セクション: 01_経営戦略（ドメイン・全社戦略）
作成日: 2026-03-21
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1701050101
deck_id = 1701050102

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_社会貢献活動',
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
    '中小企業診断士_企業経営理論::01_経営戦略::社会貢献活動'
)

question = '''企業の<span class="important">社会貢献活動の形態</span>（マッチングギフト・企業市民・ボランティア支援・ISO26000等）の定義と違いを答えよ'''

answer = '''<b>Corporate Social Contribution Activities</b>（企業の社会貢献活動の形態）

<div class="formula">
<table>
<tr><th>形態</th><th>定義</th><th>ポイント</th></tr>
<tr><td><b>マッチングギフト</b><br>Matching Gift</td><td>従業員の寄付に企業が<b>一定比率の額を上乗せ</b>して寄付する仕組み</td><td>従業員と企業の善意を<b>組み合わせる</b>。企業単独の寄付とは異なる</td></tr>
<tr><td><b>企業市民</b><br>Corporate Citizenship</td><td>企業も地域社会の一員（市民）として社会的責任を果たすべきという考え方</td><td>利益追求と社会貢献の<b>両立</b>が前提。「経済的責任より奉仕を優先」ではない</td></tr>
<tr><td><b>フィランソロピー</b><br>Philanthropy</td><td>企業による慈善活動<b>全般</b></td><td>寄付・ボランティア・施設開放など<b>広い概念</b></td></tr>
<tr><td><b>メセナ</b><br>Mécénat（仏語）</td><td><b>文化・芸術</b>分野への支援活動</td><td>フィランソロピーの<b>一部</b>。スポーツ支援は含まない</td></tr>
<tr><td><b>ボランティア支援</b></td><td>企業が従業員のボランティア活動を<b>促進</b>する取り組み</td><td>促進はOK。<b>強制すると労働扱い</b>になる</td></tr>
<tr><td><b>ISO26000</b></td><td>組織の社会的責任に関する<b>国際規格</b>（ガイダンス文書）</td><td><b>企業だけでなくあらゆる組織</b>が対象。認証規格ではなく<b>ガイダンス</b>（認証審査なし）</td></tr>
</table>
</div>

<div class="formula">
<b>ISO26000の7つの中核主題:</b><br>
① 組織統治　② 人権　③ 労働慣行　④ 環境<br>
⑤ 公正な事業慣行　⑥ 消費者課題　⑦ コミュニティへの参画及び発展
</div>

<div class="formula">
<b>社会貢献活動に含まれるもの:</b><br><br>
企業の社会貢献活動<br>
　├─ 金銭的寄付<br>
　├─ 現物寄付（物品の提供）<br>
　├─ 施設開放（自社施設を地域に開放）<br>
　├─ マッチングギフト（従業員寄付+企業上乗せ）<br>
　├─ ボランティア派遣・支援<br>
　├─ メセナ（文化・芸術支援）<br>
　└─ プロボノ（専門スキルを活かした社会貢献）
</div>

<div class="example">
<b>試験での引っかけ:</b><br>
・「社会貢献活動に現物や施設開放による寄付は含まれない」→ <b>×</b> 金銭以外も<b>含まれる</b><br>
・「文化・芸術分野への社会貢献活動はフィランソロピー」→ <b>×</b> 文化・芸術は<b>メセナ</b><br>
・「企業市民とは社会への奉仕を経済的責任より優先させること」→ <b>×</b> 両立が前提<br>
・「企業がボランティア活動を強制することもCSRの一環」→ <b>×</b> 強制は<b>労働扱い</b><br>
・「ISO26000は企業のみを対象とした認証規格」→ <b>×</b> <b>あらゆる組織</b>が対象、<b>認証ではなくガイダンス</b>
</div>

<div class="source">出典: 中小企業診断士試験 R5再試第9問、R3第13問</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0105_社会貢献活動_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
