"""
Ankiカード: M&Aのプロセス全体像とPMI（統合段階）
科目: 中小企業診断士_企業経営理論
セクション: 03_成長戦略・国際経営
作成日: 2026-03-21
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1703090301
deck_id = 1703090302

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_PMI',
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
    '中小企業診断士_企業経営理論::03_成長戦略・国際経営::PMI'
)

question = '''<span class="important">M&amp;Aのプロセス全体像</span>と統合段階（PMI）の内容を答えよ'''

answer = '''<b>M&amp;A Process &amp; Post Merger Integration（PMI）</b>

<div class="formula">
<b>M&amp;Aの全体プロセス:</b><br><br>
① 戦略策定（なぜM&amp;Aが必要か）<br>
　↓<br>
② ターゲット選定（どの企業を買うか）<br>
　↓<br>
③ デューデリジェンス（DD）（買う前の精密検査）<br>
　↓<br>
④ 交渉・契約（価格・条件の合意）<br>
　↓<br>
⑤ クロージング（契約締結・株式移転）<br>
　↓<br>
⑥ <b>PMI（統合段階）</b>← M&amp;Aの成否を決める<b>最重要フェーズ</b>
</div>

<div class="formula">
<b>デューデリジェンス（Due Diligence / DD）:</b>
<table>
<tr><th>種類</th><th>調査内容</th></tr>
<tr><td><b>財務DD</b></td><td>資産・負債・キャッシュフローの実態</td></tr>
<tr><td><b>法務DD</b></td><td>訴訟リスク・契約関係・知的財産</td></tr>
<tr><td><b>ビジネスDD</b></td><td>事業の将来性・市場環境・競争力</td></tr>
<tr><td><b>人事DD</b></td><td>人材・組織・労務問題</td></tr>
<tr><td><b>税務DD</b></td><td>税務リスク・繰越欠損金</td></tr>
</table>
</div>

<div class="formula">
<b>PMI（Post Merger Integration）の3つの統合:</b>
<table>
<tr><th>統合領域</th><th>内容</th><th>難易度</th></tr>
<tr><td><b>経営統合</b></td><td>ビジョン・戦略・マネジメント体制の統一</td><td>中</td></tr>
<tr><td><b>業務統合</b></td><td>システム・業務プロセス・制度の統合</td><td>中</td></tr>
<tr><td><b>意識統合</b></td><td>企業文化・組織風土・価値観の融合</td><td><span class="important">最も難しい</span></td></tr>
</table>
</div>

<div class="example">
<b>PMIの成功のカギ:</b><br>
・<b>100日プラン</b>: 統合後100日間の行動計画を事前に策定<br>
・<b>統合推進チーム（IMO）</b>の設置: Integration Management Office<br>
・<b>スピード</b>: 統合の遅れは従業員の不安・離職を招く<br>
・<b>コミュニケーション</b>: 両社の従業員への丁寧な説明
</div>

<div class="example">
<b>試験での問われ方:</b><br>
・「M&amp;Aは契約締結がゴール」→ <b>×</b> PMI（統合段階）が<b>最も重要</b><br>
・「PMIで最も難しいのはシステム統合」→ <b>×</b> <b>意識統合</b>（企業文化の融合）が最難関<br>
・「DDは買収後に行う」→ <b>×</b> 買収<b>前</b>に行う精密検査
</div>

<div class="source">出典: 中小企業診断士試験</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0309_PMI_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
