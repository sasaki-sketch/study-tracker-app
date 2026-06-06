"""
Ankiカード: 両利きの経営
科目: 中小企業診断士_企業経営理論
セクション: 04_技術経営・イノベーション
作成日: 2026-03-16
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1704050001
deck_id = 1704050002

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_両利きの経営',
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
    '中小企業診断士_企業経営理論::04_技術経営・イノベーション::両利きの経営'
)

# カード内容
question = '''オライリーとタッシュマンが提唱した「両利きの経営」の定義、<span class="important">知の探索と知の深化の違い</span>、<span class="important">サクセストラップ</span>、および実現のための組織設計を答えよ'''

answer = '''<b>Ambidextrous Management</b>（両利きの経営）

<p>オライリー（C.A. O'Reilly）とタッシュマン（M.L. Tushman）が提唱。<b>知の探索（Exploration）と知の深化（Exploitation）を同時に行う</b>経営手法。</p>

<div class="formula">
<table>
<tr><th></th><th>知の深化（Exploitation）</th><th>知の探索（Exploration）</th></tr>
<tr><td><b>内容</b></td><td>既存の知識・事業を磨き込む</td><td>既存の認知を超えて新領域を開拓</td></tr>
<tr><td><b>目的</b></td><td>効率性向上、既存事業の収益最大化</td><td>イノベーション、新規事業の創出</td></tr>
<tr><td><b>リスク</b></td><td>過剰適応 → <span class="important">サクセストラップ</span></td><td>短期的には成果が出にくい</td></tr>
<tr><td><b>企業例</b></td><td>トヨタの生産方式改善</td><td>Googleの20%ルール</td></tr>
</table>
</div>

<div class="example">
<b>サクセストラップ（コンピテンシートラップ）:</b><br>
成功体験に囚われ深化に偏りすぎた結果、探索が疎かになり、長期的にイノベーションが起こせなくなる罠。前カードの<b>コア・リジディティ</b>と同じ構造。<br><br>

<b>実現のための組織設計（3つのアプローチ）:</b><br>
1. <b>構造的分離</b>: 深化と探索を別ユニットに分け、探索側を既存組織から完全に切り離す（最も一般的）<br>
2. <b>連続的切替</b>: 時期によって深化と探索を切り替える<br>
3. <b>文脈的</b>: 個人レベルで深化と探索の時間配分を柔軟に設計
</div>

<p><b>注意</b>: 最大のポイントは「探索をいかに社内で擁護・育成するか」。深化は短期成果が出やすく資源が集中しがちなため、経営トップが意図的に探索を保護する必要がある。DCの「感知・捕捉・変革」と対応する概念。</p>

<div class="source">出典: C.A. O'Reilly &amp; M.L. Tushman『Lead and Disrupt』、CULTIBASE 3つのアプローチ、DHBR 入山章栄</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

# .apkg出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0405_両利きの経営_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
