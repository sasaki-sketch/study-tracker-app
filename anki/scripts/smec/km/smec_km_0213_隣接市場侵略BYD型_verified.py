"""
Ankiカード: 隣接市場侵略・BYD型（ヒエヒエ帝王）
科目: 中小企業診断士_企業経営理論
セクション: 02_競争戦略
作成日: 2026-04-23
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki/02_Personal/anki')
from anki_card_css_template import CARD_CSS

model_id = 1702130001
deck_id = 1702130002

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_隣接市場侵略BYD型',
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
    '中小企業診断士_企業経営理論::02_競争戦略::隣接市場侵略BYD型'
)

question = '''<span class="important">ヒエヒエ帝王</span>（隣接市場侵略）の武器は何か？<br><br>既存事業の<b>何</b>を武器に新市場へ侵略するか？<br><b>BYDが日本EV市場に至るまでの系譜（年表）</b>は？'''

answer = '''<b>Adjacent Market Invasion / Scale Economy Transfer</b>（隣接市場侵略）

<div class="formula">
<b>■ 戦略原理</b><br>
他市場で築いた<b>規模の経済</b>と<b>垂直統合</b>を武器に、<br>
新市場へ<b>低コスト</b>で一気に侵攻する。<br><br>
<b>武器の三点セット:</b><br>
① <b>垂直統合</b>（Vertical Integration）<br>
② <b>規模の経済</b>（Economies of Scale）<br>
③ <b>低コスト価格攻勢</b>
</div>

<div class="example">
<b>■ BYDの系譜（隣接市場侵略の教科書例）</b>
<table>
<tr><th>年</th><th>段階</th><th>製品</th></tr>
<tr><td><b>1995</b></td><td>起源</td><td>携帯電話用バッテリー製造</td></tr>
<tr><td><b>1999</b></td><td>日本市場へ</td><td>日本企業にバッテリー供給開始</td></tr>
<tr><td><b>2015</b></td><td>電動車両</td><td>電気バスを京都に納入</td></tr>
<tr><td><b>2023.7</b></td><td>★本丸侵攻★</td><td><b>日本で乗用車販売開始</b></td></tr>
<tr><td>2025</td><td>軽自動車市場</td><td>BYD RACCO（初の海外専用モデル）</td></tr>
</table>
</div>

<div class="example">
<b>■ 垂直統合の強み（BYDの事例）</b><br>
・<b>バッテリーを内製</b>（EV最大のコスト要素を支配）<br>
・原材料 → セル → パック → 車両まで一貫生産<br>
・外部サプライヤー依存を排除 → <b>原価を20〜30%低減</b>と推定<br>
・アグレッシブな価格戦略が可能（競合の利益率を削る）
</div>

<div class="example">
<b>■ 他の「ヒエヒエ帝王」例</b>
<table>
<tr><th>企業</th><th>元の市場</th><th>侵略先</th></tr>
<tr><td><b>ユニクロ</b></td><td>日本アパレルSPA</td><td>グローバル小売</td></tr>
<tr><td><b>Amazon</b></td><td>書籍EC</td><td>全商品 → AWS → 広告</td></tr>
<tr><td><b>トヨタ</b></td><td>織機（豊田自動織機）</td><td>自動車</td></tr>
<tr><td><b>富士フイルム</b></td><td>写真フィルム</td><td>医療・化粧品（Astalift）</td></tr>
</table>
</div>

<div class="example">
<b>■ シーン再生フック（フロンティア山）</b><br>
<b>ヒエヒエ帝王</b>が隣の山（他市場）から<b>橋を架けて</b>、<br>
既存事業で鍛えた<b>冷たい低コスト軍団</b>で侵攻してくる。<br>
既存プレイヤーは氷のような価格攻勢で<b>凍らされる</b>。
</div>

<div class="source">出典: BYD公式「BYD Enters Passenger Vehicle Market in Japan」(2023年7月発表); "Vertical Integration and Market Entry: BYD's Cost-Efficient Approach" (LinkedIn 2024); H.I.Ansoff『経営戦略論』多角化戦略</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

output_path = '/Users/sasaki/02_Personal/anki/anki/scripts/smec/km/smec_km_0213_隣接市場侵略BYD型_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
