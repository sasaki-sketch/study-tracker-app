"""
Ankiカード: 企業間連携戦略（水平的/垂直的M&A、JV vs M&A、CVC）
科目: 中小企業診断士_企業経営理論
セクション: 03_成長戦略・国際経営
作成日: 2026-03-21
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1703050301
deck_id = 1703050302

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_連携戦略',
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
    '中小企業診断士_企業経営理論::03_成長戦略・国際経営::連携戦略'
)

question = '''企業間の<span class="important">連携戦略</span>（水平的/垂直的M&amp;A、JV vs M&amp;A、CVC）の違いを答えよ'''

answer = '''<b>Corporate Alliance &amp; M&amp;A Strategy</b>（企業間連携戦略）

<div class="formula">
<b>水平的M&amp;A vs 垂直的M&amp;A:</b>
<table>
<tr><th></th><th>水平的M&amp;A</th><th>垂直的M&amp;A</th></tr>
<tr><td><b>方向</b></td><td>ヨコ（＝同じ段階）</td><td>タテ（＝バリューチェーンの上下）</td></tr>
<tr><td><b>対象</b></td><td><b>同業者</b>同士</td><td><b>仕入先や販売先</b></td></tr>
<tr><td><b>目的</b></td><td>市場シェア拡大、規模の経済</td><td>バリューチェーンの変革、内製化</td></tr>
<tr><td><b>例</b></td><td>ビール会社同士の合併</td><td>自動車メーカーが部品メーカーを買収</td></tr>
</table>
</div>

<div class="mnemonic">
<b>覚え方:</b> 水平＝ヨコ＝同業、垂直＝タテ＝川上・川下
</div>

<div class="formula">
<b>Joint Venture（JV） vs M&amp;A:</b>
<table>
<tr><th></th><th>JV（合弁）</th><th>M&amp;A（買収）</th></tr>
<tr><td><b>関係</b></td><td><b>連携</b>するだけ</td><td>自社内に<b>取り込む</b></td></tr>
<tr><td><b>相手の法人格</b></td><td><b>維持される</b></td><td>消滅or子会社化</td></tr>
<tr><td><b>共有できる情報の範囲</b></td><td><b>狭い</b>（別法人のまま）</td><td><b>広い</b>（自社内に統合）</td></tr>
<tr><td><b>範囲の経済</b></td><td>限定的</td><td><b>M&amp;Aの方が大きい</b></td></tr>
</table>
</div>

<div class="formula">
<b>CVC（Corporate Venture Capital）:</b>
<table>
<tr><th>項目</th><th>内容</th></tr>
<tr><td><b>定義</b></td><td><b>事業会社</b>がベンチャー企業に投資すること</td></tr>
<tr><td><b>目的</b></td><td>ベンチャーの革新的な技術・ビジネスモデルを取り込み、自社の既存事業との<b>シナジーを発現</b></td></tr>
<tr><td><b>通常のVCとの違い</b></td><td>VC＝財務リターンが主目的、CVC＝<b>戦略的リターン（シナジー）</b>が主目的</td></tr>
</table>
</div>

<div class="example">
<b>試験での引っかけ:</b><br>
・「仕入先の買収は水平的M&amp;A」→ <b>×</b> 仕入先はバリューチェーンの上流なので<b>垂直的</b><br>
・「JVはM&amp;Aより情報共有範囲が広い」→ <b>×</b> <b>M&amp;Aの方が広い</b>（自社内に取り込むため）<br>
・「TOBは公開市場で株式を買い付ける」→ <b>×</b> 市場の<b>外</b>で株主に直接呼びかける<br>
・「MBOは非上場企業では起こらない」→ <b>×</b> 非上場企業でも<b>起こり得る</b>
</div>

<div class="source">出典: 中小企業診断士試験 R7第6問</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0305_連携戦略_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
