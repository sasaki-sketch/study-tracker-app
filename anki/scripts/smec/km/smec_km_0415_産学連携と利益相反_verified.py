"""
Ankiカード: 産学連携における利益相反
科目: 中小企業診断士_企業経営理論
セクション: 04_技術経営・イノベーション
作成日: 2026-03-16
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1704150001
deck_id = 1704150002

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_産学連携と利益相反',
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
    '中小企業診断士_企業経営理論::04_技術経営・イノベーション::産学連携と利益相反'
)

# カード内容
question = '''大学との共同研究における「利益相反」の定義、<span class="important">3つの分類</span>（狭義の利益相反・責務相反・組織としての利益相反）、およびマネジメントの考え方を答えよ'''

answer = '''<b>Conflict of Interest（COI）</b>（利益相反）

<p>産学連携において、研究者や大学が外部から得る利益と、教育・研究の公正性との間に生じる矛盾・対立のこと。</p>

<div class="formula">
<b>3つの分類:</b>
<table>
<tr><th>分類</th><th>定義</th><th>具体例</th></tr>
<tr><td><b>狭義の利益相反</b></td><td>産学連携で得る<b>金銭的利益</b>と教育・研究の責任が相反</td><td>企業から研究費を受け取り、その企業に有利な研究結果を出す疑い</td></tr>
<tr><td><b>責務相反</b></td><td>兼業等により<b>複数の職務責任</b>が存在し、本務が疎かになる状態</td><td>企業の技術顧問を兼任し、大学の教育・研究時間が削られる</td></tr>
<tr><td><b>組織としての利益相反</b></td><td><b>大学法人</b>が企業と利害関係を持つことで生じる</td><td>大学がTLOに出資、大学保有の株式がある企業と共同研究を実施</td></tr>
</table>
</div>

<div class="example">
<b>利益相反マネジメントの考え方:</b><br>
・利益相反そのものは<b>悪ではない</b>（産学連携を進めれば必然的に発生する）<br>
・問題は利益相反に<b>無関心であること</b>。第三者から「公正性が損なわれているのでは？」と疑われること（<b>アピアランスの問題</b>）が社会的信頼を毀損する<br>
・利益相反を<b>禁止するのではなく、適切に管理（マネジメント）する</b>ことが重要<br><br>

<b>マネジメントの仕組み:</b><br>
1. <b>情報開示</b>: 金銭的利益関係を大学に申告・開示<br>
2. <b>審査体制</b>: 利益相反委員会・アドバイザーの設置<br>
3. <b>個別判断</b>: 事例ごとに続行・条件付き承認・中止を判断
</div>

<p><b>注意</b>: TLO（Technology Licensing Organization／技術移転機関）は大学の研究成果を企業にライセンスする組織だが、TLO自体が利益相反の当事者になりうる。産学連携の推進とCOIマネジメントは表裏一体であり、前カードのオープンイノベーションを実践する上で避けて通れない論点。</p>

<div class="source">出典: 文部科学省 利益相反WG報告書、筑波大学 利益相反研修テキスト、大阪大学 COIマネジメント</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

# .apkg出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0415_産学連携と利益相反_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
