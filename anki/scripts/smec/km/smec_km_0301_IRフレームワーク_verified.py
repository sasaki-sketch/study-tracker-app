"""
Ankiカード: I-Rフレームワーク（バートレット&ゴシャール）
科目: 中小企業診断士_企業経営理論
セクション: 03_成長戦略・国際経営
作成日: 2026-03-20
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1703010301
deck_id = 1703010302

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_IRフレームワーク',
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
    '中小企業診断士_企業経営理論::03_成長戦略・国際経営::IRフレームワーク'
)

# カード内容
question = '''バートレット&ゴシャールの<span class="important">I-Rフレームワーク</span>の4類型と各特徴を答えよ'''

answer = '''<b>Integration-Responsiveness Framework</b>（I-Rフレームワーク）

<p>バートレット&ゴシャール（Bartlett &amp; Ghoshal, 1989）が提唱。<br>
縦軸＝<b>グローバル統合</b>、横軸＝<b>ローカル適合</b>で4類型に分類。</p>

<div class="formula">
<table>
<tr><td colspan="2" rowspan="2"></td><td colspan="2" style="text-align:center"><b>ローカル適合 →</b></td></tr>
<tr><td style="text-align:center"><b>低</b></td><td style="text-align:center"><b>高</b></td></tr>
<tr><td rowspan="2" style="writing-mode:vertical-rl"><b>グローバル統合 ↑</b></td><td><b>高</b></td><td style="background-color:#e8f0fe">グローバル型</td><td style="background-color:#fce4ec">トランスナショナル型</td></tr>
<tr><td><b>低</b></td><td style="background-color:#f5f5f5">インターナショナル型</td><td style="background-color:#e8f5e9">マルチナショナル型</td></tr>
</table>
</div>

<div class="formula">
<table>
<tr><th>類型</th><th>統合</th><th>適合</th><th>特徴</th></tr>
<tr><td><b>グローバル型</b></td><td>高</td><td>低</td><td>世界を単一市場。本国集中。現地適応しない</td></tr>
<tr><td><b>トランスナショナル型</b></td><td>高</td><td>高</td><td>資源分散＋相互依存＋専門化。知識は共同開発・共有。<span class="important">理想的だが実現困難</span></td></tr>
<tr><td><b>インターナショナル型</b></td><td>低</td><td>低</td><td>中核は本国集中、他は分散。本国の能力を適用・活用。知識は本国→海外へ移転</td></tr>
<tr><td><b>マルチナショナル型</b><br>（ドメスティック）</td><td>低</td><td>高</td><td>世界を独立市場の集合体。現地へ権限委譲。現地ニーズにきめ細かく対応</td></tr>
</table>
</div>

<div class="mnemonic">
<b>覚え方:</b><br><br>
<b>語源でイメージ:</b><br>
・<b>グローバル</b>（Globe＝地球儀）→ 地球は1つ、本社が全部仕切る<br>
・<b>マルチナショナル</b>（Multi＝多数）→ たくさんの国がそれぞれ勝手にやる<br>
・<b>トランスナショナル</b>（Trans＝超える）→ 全部超える理想型、でも難しい<br>
・<b>インターナショナル</b>（Inter＝間）→ 本国のやり方を海外に渡すだけ<br><br>
<b>配置の暗記「グっと今（いま）！」:</b><br>
グ（ローバル）ト（ランスナショナル）<br>
イ（ンターナショナル）マ（ルチナショナル）<br><br>
<b>対角線で対比:</b><br>
・グローバル ↔ マルチナショナル: 本社集中 vs 現地分散（正反対）<br>
・インターナショナル ↔ トランスナショナル: どっちも中途半端 vs 両方達成
</div>

<div class="source">出典: Bartlett &amp; Ghoshal (1989)『Managing Across Borders』、中小企業診断士試験</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

# .apkg出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0301_IRフレームワーク_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
