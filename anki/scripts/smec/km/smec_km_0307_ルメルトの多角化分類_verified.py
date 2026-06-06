"""
Ankiカード: ルメルトの多角化分類
科目: 中小企業診断士_企業経営理論
セクション: 03_成長戦略・国際経営
作成日: 2026-03-15
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1703070001
deck_id = 1703070002

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_ルメルト多角化',
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
    '中小企業診断士_企業経営理論::03_成長戦略・国際経営::ルメルトの多角化分類'
)

# カード内容
question = '''ルメルトの多角化分類における<span class="important">3つの比率と判定基準</span>、および関連型多角化の<span class="important">集約型・拡散型の違いと業績との関係</span>を答えよ'''

answer = '''<b>Rumelt's Diversification Classification</b>（ルメルトの多角化分類）

<p>ルメルト（R.P. Rumelt, 1974）が『Strategy, Structure, and Economic Performance』で提唱。企業の多角化の「程度」と「パターン」を定量的に分類した。</p>

<div class="formula">
<b>3つの比率:</b><br>
・<b>特化比率（SR）</b>: 最大事業の売上高 ÷ 全社売上高<br>
・<b>垂直比率（VR）</b>: 垂直統合された事業群の売上高 ÷ 全社売上高<br>
・<b>関連比率（RR）</b>: 相互に関連する事業群の売上高 ÷ 全社売上高<br><br>

<b>判定基準と企業例:</b>
<table>
<tr><th>分類</th><th>条件</th><th>企業例</th></tr>
<tr><td><b>専業型</b></td><td>SR ≧ 95%</td><td>ヤクルト（乳酸菌飲料が大半）</td></tr>
<tr><td><b>垂直型</b></td><td>SR &lt; 95%, VR ≧ 70%</td><td>新日鉄（原料→製鉄→加工の一貫体制）</td></tr>
<tr><td><b>本業型</b></td><td>70% ≦ SR &lt; 95%</td><td>トヨタ（自動車が主力＋金融・住宅等）</td></tr>
<tr><td><b>関連型</b></td><td>SR &lt; 70%, RR ≧ 70%</td><td>富士フイルム（化学技術で医療・化粧品等に展開）</td></tr>
<tr><td><b>非関連型</b></td><td>SR &lt; 70%, RR &lt; 70%</td><td>GE（電機・金融・医療等を無関連に展開）</td></tr>
</table>
</div>

<div class="example">
<b>関連型多角化の2パターン:</b><br><br>
<b>集約型（Constrained）＝ ハブ型</b> → <span class="important">収益性が高い</span><br>
全事業が<b>同じコア資源</b>に紐づく。どの事業からもコアに戻れる構造。<br>
例: 花王（界面活性剤技術 → 洗剤・化粧品・トイレタリー・ヘアケア全てがコアを共有）<br><br>

<b>拡散型（Linked）＝ 数珠つなぎ型</b> → 収益性は集約型より低い<br>
隣の事業同士は関連するが、連鎖が進むと<b>最初のコアから離れていく</b>。<br>
例: ヤマハ（ピアノ→木工技術→家具→振動技術→電子楽器→電子技術→半導体）
</div>

<p><b>注意</b>: 拡散型は各ステップでは合理的に見えるが、気づくと元のコアから遠く離れ、全社的なシナジーが効きにくくなる。アンゾフが「方向性」で分類するのに対し、ルメルトは「関連度合い」を定量的比率で分類する点が異なる。</p>

<div class="source">出典: R.P. Rumelt (1974)、一発合格まとめシート R4第1問、スタディング 中小企業診断士</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

# .apkg出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0307_ルメルトの多角化分類_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
