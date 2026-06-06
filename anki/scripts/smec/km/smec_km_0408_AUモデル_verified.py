"""
Ankiカード: イノベーションの種類（A-Uモデル）
科目: 中小企業診断士_企業経営理論
セクション: 04_技術経営・イノベーション
作成日: 2026-03-16
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1704080001
deck_id = 1704080002

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_AUモデル',
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
    '中小企業診断士_企業経営理論::04_技術経営・イノベーション::A-Uモデル'
)

# カード内容
question = '''アバナシーとアッターバックのA-Uモデルにおける<span class="important">2種類のイノベーション</span>と<span class="important">3つの段階</span>、およびドミナントデザインの役割を答えよ'''

answer = '''<b>Abernathy-Utterback Model</b>（A-Uモデル）

<p>アバナシーとアッターバック（1975）が提唱。産業のイノベーションは2種類のイノベーションが3段階を経て推移するパターンを示した。</p>

<div class="formula">
<b>2種類のイノベーション:</b><br>
・<b>プロダクトイノベーション</b>: 製品の機能・性能・デザインの革新（何を作るか）<br>
・<b>プロセスイノベーション</b>: 生産工程・製造方法の革新（どう作るか）<br><br>

<b>3つの段階:</b>
<table>
<tr><th>段階</th><th>プロダクト革新</th><th>プロセス革新</th><th>競争の焦点</th></tr>
<tr><td><b>流動期</b>（Fluid）</td><td><span class="important">高い</span></td><td>低い</td><td>製品の機能・性能</td></tr>
<tr><td><b>移行期</b>（Transitional）</td><td>低下↓</td><td><span class="important">上昇↑</span></td><td>ドミナントデザインの確立</td></tr>
<tr><td><b>固定期</b>（Specific）</td><td>低い</td><td>低い</td><td>コスト・品質の効率化</td></tr>
</table>
</div>

<div class="example">
<b>ドミナントデザイン（Dominant Design）:</b><br>
市場の支配を勝ちとった製品の<b>標準的な設計・構造・基本仕様</b>。流動期の多様な競争の中から移行期に確立される。<br><br>

・<b>形成メカニズム</b>: 流動期に多数の企業が異なる設計で参入 → 市場・技術・規制などの要因により1つのデザインに収斂 → 業界標準となる<br>
・<b>確立後の影響</b>: 競争の焦点が「製品の革新性」から「コスト・効率」に移行。新規参入が困難になり、既存企業の寡占化が進む。部品のモジュール化・標準化も加速する<br>
・<b>従わないとどうなるか</b>: ドミナントデザインに準拠しない企業は市場から淘汰される<br><br>

<b>具体例:</b><br>
・<b>スマートフォン</b>: タッチスクリーン＋アプリストア型 → キーボード型（BlackBerry等）は淘汰<br>
・<b>自動車</b>: 流動期（蒸気・電気・ガソリンが競争）→ ガソリン＋T型フォードの大量生産がドミナントデザインに → 固定期（基本設計は固定、コスト・品質改善が中心）
</div>

<p><b>注意</b>: 破壊的イノベーション（クリステンセン）は固定期のドミナントデザインを根本から覆す概念として対比される。EV（電気自動車）はガソリン車のドミナントデザインに対する破壊的イノベーションの例。</p>

<div class="source">出典: Abernathy &amp; Utterback (1978) "Patterns of Industrial Innovation"、Frontier Eyes ドミナントデザイン解説、明治大学 佐野研究室</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

# .apkg出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0408_AUモデル_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
