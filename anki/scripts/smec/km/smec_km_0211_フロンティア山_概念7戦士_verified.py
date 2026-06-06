"""
Ankiカード: フロンティア山の世界観＋7戦士早見表
科目: 中小企業診断士_企業経営理論
セクション: 02_競争戦略
作成日: 2026-04-23
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki/02_Personal/anki')
from anki_card_css_template import CARD_CSS

model_id = 1702110001
deck_id = 1702110002

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_フロンティア山_概念7戦士',
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
    '中小企業診断士_企業経営理論::02_競争戦略::フロンティア山_概念7戦士'
)

question = '''成長市場（導入期〜成長期）の勝ち筋を描いた<span class="important">「フロンティア山」</span>に棲む<b>7人の戦士</b>の名前・戦略原理・代表例を答えよ。<br><br>クープマン山（成熟）との決定的な違いは？'''

answer = '''<b>Frontier Mountain: 7 Warriors of Growth Market Strategy</b>（フロンティア山の7戦士）

<div class="formula">
<b>■ フロンティア山の特徴（成長市場）</b><br>
・パイ（山）自体が<b>拡大中</b><br>
・山の形（支配的技術）が変わる<br>
・先に登った者が勝つとは限らない<br>
・武器の違う7戦士が<b>乱戦中</b><br>
・成熟化 → <b>クープマン山に変貌</b>
</div>

<div class="formula">
<b>■ 7戦士早見表</b>
<table>
<tr><th>#</th><th>戦士名</th><th>戦略原理</th><th>代表例</th></tr>
<tr><td>1</td><td><b>ハタタテ開拓者</b></td><td>先発優位</td><td>iPhone, Tesla</td></tr>
<tr><td>2</td><td><b>マネマネ猿</b></td><td>ファストフォロワー</td><td>Google, Facebook</td></tr>
<tr><td>3</td><td><b>ヒエヒエ帝王</b></td><td>隣接市場侵略</td><td><b>BYD</b>, ユニクロ</td></tr>
<tr><td>4</td><td><b>ハカイ錬金術師</b></td><td>破壊的イノベーション</td><td>Netflix, Airbnb</td></tr>
<tr><td>5</td><td><b>アミハリ大司教</b></td><td>ネットワーク効果</td><td>Uber, Meta</td></tr>
<tr><td>6</td><td><b>アオウミ海賊</b></td><td>ブルーオーシャン</td><td>任天堂Wii, Cirque du Soleil</td></tr>
<tr><td>7</td><td><b>タニワタリ軍団★</b></td><td>キャズム越え（二重役）</td><td>Slack, Zoom, ChatGPT</td></tr>
</table>
</div>

<div class="example">
<b>■ クープマン山（成熟）との決定的な違い</b>
<table>
<tr><th></th><th>フロンティア山</th><th>クープマン山</th></tr>
<tr><td>市場</td><td>成長・導入期</td><td>成熟</td></tr>
<tr><td>パイ</td><td>拡大中</td><td>固定</td></tr>
<tr><td>勝ち筋</td><td>武器×タイミング</td><td>シェア階段戦略</td></tr>
<tr><td>主要理論</td><td>破壊的イノベ、BO、キャズム</td><td><b>クープマン目標値</b></td></tr>
<tr><td>頂点</td><td>流動的</td><td>73.9%（ナナサンキュー大王）</td></tr>
</table>
</div>

<div class="example">
<b>■ 既存カードとの連携</b><br>
・ハカイ錬金術師 → <b>0410 イノベーションのジレンマ</b><br>
・アミハリ大司教 → <b>0422 ネットワーク外部性</b><br>
・山全体 → <b>0802 PLC</b><br>
・両山の関係 → <b>0804 コトラーの競争地位戦略</b>
</div>

<div class="source">出典: 設計プラン /Users/sasaki/.claude/plans/tender-moseying-meteor.md、各戦略理論の原典は個別カード（0212〜0215）参照</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

output_path = '/Users/sasaki/02_Personal/anki/anki/scripts/smec/km/smec_km_0211_フロンティア山_概念7戦士_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
