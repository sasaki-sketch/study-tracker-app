"""
Ankiカード: 値引・戻り・割戻・割引の区別
科目: 中小企業診断士_財務会計
セクション: 01_経営分析
作成日: 2026-03-22
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1711010101
deck_id = 1711010102

my_model = genanki.Model(
    model_id,
    '中小企業診断士_財務会計_値引割戻割引',
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
    '中小企業診断士_財務会計::01_経営分析::値引割戻割引'
)

question = '''<span class="important">値引・戻り（返品）・割戻・割引</span>の定義・会計処理・勘定科目の違いを答えよ'''

answer = '''<b>値引・戻り・割戻・割引</b>

<div class="formula">
<table>
<tr><th></th><th>値引</th><th>戻り（返品）</th><th>割戻</th><th>割引</th></tr>
<tr><td><b>内容</b></td><td>不良品・見切り品などで<b>販売価格を下げる</b></td><td>売った商品が<b>送り返される</b></td><td><b>大量購入</b>による値引（ボリュームディスカウント）</td><td>支払期限<b>前に支払い</b>があった場合に代金を安くする</td></tr>
<tr><td><b>具体例</b></td><td>キズ物を定価1,000円→800円で販売</td><td>商品が不良品だったので返品</td><td>100個買ったら1個90円に（通常100円）</td><td>「30日後払いだが10日以内に払えば2%引き」</td></tr>
<tr><td><b>売上への影響</b></td><td>売上 = 通常価格 <b>- 値引額</b></td><td><b>売上勘定を減額</b></td><td>売上 = 通常価格 <b>- 割戻額</b></td><td>売上は<b>変わらない</b></td></tr>
<tr><td><b>P/L上の区分</b></td><td><b>売上の控除</b></td><td><b>売上の控除</b></td><td><b>売上の控除</b></td><td><span class="important">営業外費用</span></td></tr>
</table>
</div>

<div class="formula">
<b>最重要ポイント: 割引だけ仲間外れ</b><br><br>
売上に影響する（売上の控除）:<br>
　値引・戻り・割戻 → 商品の価格や数量に関する調整<br><br>
売上に影響しない（営業外費用）:<br>
　割引 → <b>利息の調整</b>（早く払った分の利息相当額を返す）
</div>

<div class="formula">
<b>勘定科目（売上側）:</b>
<table>
<tr><th>取引</th><th>勘定科目</th><th>P/L区分</th></tr>
<tr><td>売上戻り</td><td><b>売上</b>（減額）</td><td>売上高の控除</td></tr>
<tr><td>売上値引</td><td><b>売上</b>（減額）</td><td>売上高の控除</td></tr>
<tr><td>売上割戻</td><td><b>売上</b>（減額）</td><td>売上高の控除</td></tr>
<tr><td>売上割引</td><td><b>売上割引</b></td><td><span class="important">営業外費用</span></td></tr>
</table>
</div>

<div class="formula">
<b>勘定科目（仕入側）:</b>
<table>
<tr><th>取引</th><th>勘定科目</th><th>P/L区分</th></tr>
<tr><td>仕入戻し</td><td><b>仕入</b>（減額）</td><td>売上原価の控除</td></tr>
<tr><td>仕入値引</td><td><b>仕入</b>（減額）</td><td>売上原価の控除</td></tr>
<tr><td>仕入割戻</td><td><b>仕入</b>（減額）</td><td>売上原価の控除</td></tr>
<tr><td>仕入割引</td><td><b>仕入割引</b></td><td><span class="important">営業外収益</span></td></tr>
</table>
</div>

<div class="mnemonic">
<b>覚え方:</b><br>
・戻り・値引・割戻は<b>元の勘定（売上or仕入）を直接減額</b><br>
・割引だけ<b>独立した勘定科目</b>になる<br>
・なぜ？→ 割引は利息の性質（<b>財務的な取引</b>）なので営業外
</div>

<div class="example">
<b>試験での引っかけ:</b><br>
・「割引は営業費用として扱う」→ <b>×</b> <b>営業外費用</b>（利息の性質）<br>
・「割戻は早期支払いによる値引」→ <b>×</b> 早期支払いは<b>割引</b>。割戻は<b>大量購入</b><br>
・「値引と割戻は同じ」→ <b>×</b> 値引は品質等の理由、割戻は数量の理由
</div>

<div class="source">出典: 中小企業診断士試験 SHEET3簿記②第3問</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0101_値引割戻割引_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
