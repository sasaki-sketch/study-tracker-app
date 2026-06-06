"""
Ankiカード: アンゾフの戦略の定義と意思決定の3分類
科目: 中小企業診断士_企業経営理論
セクション: 01 経営戦略（ドメイン・全社戦略）
作成日: 2026-03-13
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# --- モデル定義 ---
MODEL_ID = 1710390110
DECK_ID = 1610390110

model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_企業経営理論_アンゾフの意思決定論',
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
deck = genanki.Deck(DECK_ID, '中小企業診断士_企業経営理論::01_経営戦略::アンゾフの意思決定論')

# --- カード ---
question = """アンゾフの戦略の定義と意思決定の3分類を答えよ"""

answer = """<b>Ansoff's Strategic Decision Theory</b>（アンゾフの意思決定論, 1965）

アンゾフは戦略を「<b>部分的無知（Partial Ignorance）</b>の状態における意思決定のためのルール」と定義した。

<ul><li><b>部分的無知</b>: 環境変化が激しく、どれだけ準備しても不確定要素が残る状態</li></ul>

また、アンゾフは企業の意思決定を以下の<b>3つに分類</b>した:

<b>① 戦略的意思決定（トップ）</b>
<ul>
<li>企業と<b>外部環境</b>との関係に関する決定</li>
<li>非定型的・長期的</li>
<li>例: 多角化、M&A、新市場への進出</li>
</ul>

<b>② 管理的意思決定（ミドル）</b>
<ul>
<li>戦略実現のための<b>経営資源の組織化</b></li>
<li>半定型的・中期的</li>
<li>例: 組織編制、権限配分、目標設定、資源調達</li>
</ul>

<b>③ 業務的意思決定（ロワー）</b>
<ul>
<li>日常の経営活動の<b>能率・収益性の最大化</b></li>
<li>定型的・短期的</li>
<li>例: 生産スケジュール、価格設定、在庫管理</li>
</ul>

<div class="important">戦略的意思決定は<b>外部環境</b>が中心（内部問題ではない）。トップが<b>意識的に</b>関与しないと明らかにならない。R2第2問等で出題。</div>

<div class="source">出典: Ansoff『Corporate Strategy』(1965), スタディング 過去問解説 R2第2問</div>"""

note = genanki.Note(model=model, fields=[question, answer])
deck.add_note(note)

# --- パッケージ出力 ---
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0110_アンゾフの意思決定論_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
