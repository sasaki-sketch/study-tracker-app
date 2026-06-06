"""
EBITDA - 中小企業診断士 財務会計
Earnings Before Interest, Taxes, Depreciation and Amortization

作成日: 2026-03-02
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1740825701
DECK_ID = 1740825702

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_EBITDA',
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
    '中小企業診断士_財務会計::01_経営分析::EBITDA'
)

# カード内容
question = """EBITDAの定義・計算式・使われる場面を答えよ"""

answer = """<b>Earnings Before Interest, Taxes, Depreciation and Amortization</b>（EBITDA / イービットディーエー）

<b>定義</b>: 利払い前・税引前・減価償却前利益。金利・税金・減価償却の影響を除いた<b>企業の純粋な稼ぐ力</b>を示す。キャッシュフローに近い指標。

<b>計算式</b>（最も一般的）:
<div class="formula">
\\[EBITDA = \\text{営業利益} + \\text{減価償却費}\\]
</div>

<b>名前の分解</b>:
<table>
<tr><th>略語</th><th>英語</th><th>意味</th></tr>
<tr><td>E</td><td>Earnings</td><td>利益</td></tr>
<tr><td>B</td><td>Before</td><td>〜の前</td></tr>
<tr><td>I</td><td>Interest</td><td>支払利息</td></tr>
<tr><td>T</td><td>Taxes</td><td>税金</td></tr>
<tr><td>D</td><td>Depreciation</td><td>有形固定資産の減価償却費</td></tr>
<tr><td>A</td><td>Amortization</td><td>無形固定資産の償却費</td></tr>
</table>

<b>なぜ減価償却費を足し戻すか</b>:
<ul>
<li>減価償却費は<b>現金支出を伴わない費用</b></li>
<li>営業利益では差し引かれているが、実際にはキャッシュは流出していない</li>
<li>足し戻すことで<b>実際の現金ベースの稼ぐ力</b>に近づく</li>
</ul>

<b>主な使われ方</b>:
<table>
<tr><th>場面</th><th>内容</th></tr>
<tr><td>EV/EBITDA倍率</td><td>買収コストの回収年数（目安: 8〜10倍）</td></tr>
<tr><td>国際比較</td><td>税制・減価償却方法の違いを排除して比較可能</td></tr>
<tr><td>収益力の評価</td><td>設備投資の大きい業種で特に有用</td></tr>
</table>

<div class="important">注意:</div>
EBITDAは会計基準（IFRS・日本基準）で公式に定義された指標ではなく、企業によって計算方法が異なる場合がある。また設備投資の必要性を無視しているため、EBITDAだけで判断するのは危険。

<div class="source">出典: 松井証券、三井住友銀行、グロービス学び放題</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0120_EBITDA_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
