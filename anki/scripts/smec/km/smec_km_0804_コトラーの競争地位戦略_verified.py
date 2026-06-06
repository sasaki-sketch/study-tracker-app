"""
Ankiカード: コトラーの競争地位別戦略
科目: 中小企業診断士_企業経営理論
セクション: 08 マーケティング概論・戦略
作成日: 2026-03-14
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# --- モデル定義 ---
MODEL_ID = 1710390804
DECK_ID = 1610390804

model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_企業経営理論_コトラーの競争地位戦略',
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
deck = genanki.Deck(DECK_ID, '中小企業診断士_企業経営理論::08_マーケティング概論::コトラーの競争地位戦略')

# --- カード ---
question = """コトラーの競争地位別戦略における4つの類型と、各類型の戦略定石を答えよ"""

answer = """<b>Kotler's Competitive Position Strategy</b>（コトラー）

市場シェアと経営資源から企業を4類型に分類し、各地位に応じた戦略を提示するフレームワーク。

<b>① リーダー（Leader）</b> — シェア: 最大 / 資源: 量・質ともに豊富
<ul>
<li>戦略目標: <b>シェア維持・市場全体の拡大</b></li>
<li><b>周辺需要拡大</b>: 市場全体を拡大し、最大シェア保有者として最も恩恵を受ける</li>
<li><b>同質化政策</b>: 競合の差別化を素早く模倣し無効化する</li>
<li><b>非価格対応</b>: むやみに値下げしない（業界全体の利益縮小を防止）</li>
<li><b>最適シェア維持</b>: 過度なシェア拡大を抑制（独占禁止法リスク回避）</li>
</ul>

<b>② チャレンジャー（Challenger）</b> — シェア: 2〜3位 / 資源: 量は大きいが質でリーダーに劣る
<ul>
<li>戦略目標: <b>シェアNo.1を目指す</b></li>
<li>4P（製品・価格・流通・促進）での<b>差別化戦略</b></li>
<li>リーダーと異なるポジションを築く</li>
</ul>

<b>③ フォロワー（Follower）</b> — シェア: 中〜下位 / 資源: 量・質ともに限定的
<ul>
<li>戦略目標: <b>生存利潤の確保</b></li>
<li>リーダーやチャレンジャーの戦略を<b>模倣</b></li>
<li><b>低コスト化</b>で効率的に利益を確保</li>
</ul>

<b>④ ニッチャー（Nicher）</b> — シェア: 低い / 資源: 量は少ないが質的に独自性あり
<ul>
<li>戦略目標: <b>特定市場での利潤最大化</b></li>
<li><b>集中・差別化戦略</b>（閉鎖型流通チャネル等）</li>
<li>大企業が参入しない小規模・専門市場に特化</li>
</ul>

<div class="important">試験頻出ポイント（R4第4問）:<br>同質化政策は<b>リーダーの戦略</b>（チャレンジャーではない）。規模の経済・経験曲線効果は<b>リーダーの強み</b>。相対市場シェア = 自社シェア ÷ 1位企業シェア。</div>

<div class="source">出典: Kotler『Marketing Management』, 中小企業診断士R4第4問</div>"""

note = genanki.Note(model=model, fields=[question, answer])
deck.add_note(note)

# --- パッケージ出力 ---
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0804_コトラーの競争地位戦略_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
