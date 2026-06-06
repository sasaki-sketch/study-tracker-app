"""
Ankiカード: BCGマトリクス（PPM）
科目: 中小企業診断士_企業経営理論
セクション: 01 経営戦略（ドメイン・全社戦略）
作成日: 2026-03-14
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# --- モデル定義 ---
MODEL_ID = 1710390111
DECK_ID = 1610390111

model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_企業経営理論_BCGマトリクス',
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

# --- デッキ定義 ---
deck = genanki.Deck(DECK_ID, '中小企業診断士_企業経営理論::01_経営戦略::BCGマトリクス')

# --- カード ---
question = """BCGマトリクス（PPM）の2軸・4象限の特徴と資源配分の考え方を答えよ"""

answer = """<b>BCG Growth-Share Matrix / PPM</b>（ボストン・コンサルティング・グループ, 1970）

<b>2軸</b>: 縦軸＝<b>市場成長率</b>（高/低）、横軸＝<b>相対的市場占有率</b>（高/低）

<b>4象限:</b>

<b>① 花形（Star）</b> — 成長率: 高 / シェア: 高
<ul>
<li>市場リーダーだが成長市場のため<b>投資も大きい</b></li>
<li>キャッシュイン大、キャッシュアウトも大 → 資金収支はほぼ均衡</li>
</ul>

<b>② 金のなる木（Cash Cow）</b> — 成長率: 低 / シェア: 高
<ul>
<li>成熟市場で安定的に<b>キャッシュを創出</b>、追加投資は少ない</li>
<li>余剰キャッシュを花形・問題児に配分する<b>資金源</b></li>
</ul>

<b>③ 問題児（Question Mark）</b> — 成長率: 高 / シェア: 低
<ul>
<li>成長市場だがシェアが低く<b>投資判断が最も難しい</b></li>
<li>選択と集中: 花形に育てるか、撤退するか</li>
</ul>

<b>④ 負け犬（Dog）</b> — 成長率: 低 / シェア: 低
<ul><li>成長性も競争力もない → <b>撤退・縮小</b>の候補</li></ul>

<div class="example">
<b>資源配分の流れ:</b><br>
金のなる木で稼いだキャッシュ → 花形（リーダー維持の投資）・問題児（シェア拡大の投資）に配分<br>
問題児のうち見込みのないものは → 撤退（負け犬化を防ぐ）
</div>

<div class="formula">
<b>市場成長率のしきい値:</b> 一般的に<b>年率10%</b>が高/低の標準的な基準。ただし業界により異なり、自社ポートフォリオの加重平均成長率を基準にする方法もある。
</div>

<div class="important">PPMの限界として、①2軸のみで事業の魅力度を判断、②事業間のシナジーを考慮しない、③新規事業の評価が困難、という点が試験で問われることがある。</div>

<div class="source">出典: Henderson, BCG(1970), Funda Navi</div>"""

note = genanki.Note(model=model, fields=[question, answer])
deck.add_note(note)

# --- パッケージ出力 ---
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0111_BCGマトリクス_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
