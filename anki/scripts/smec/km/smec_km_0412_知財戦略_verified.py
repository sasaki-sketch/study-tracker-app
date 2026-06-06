"""
Ankiカード: 知財戦略（MOTの観点）
科目: 中小企業診断士_企業経営理論
セクション: 04_技術経営・イノベーション
作成日: 2026-03-16
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1704120001
deck_id = 1704120002

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_知財戦略',
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
    '中小企業診断士_企業経営理論::04_技術経営・イノベーション::知財戦略'
)

# カード内容
question = '''MOT（技術経営）における知財戦略の基本的考え方、<span class="important">オープン・クローズ戦略</span>の定義と使い分け、および<span class="important">標準化戦略</span>との関係を答えよ'''

answer = '''<b>Intellectual Property Strategy in MOT</b>（技術経営における知財戦略）

<p>技術を競争優位に変えるには、知的財産を「守る」だけでなく「攻めに使う」戦略が必要。中核はオープン・クローズ戦略。</p>

<div class="formula">
<b>オープン・クローズ戦略:</b><br>
自社技術を<b>公開する領域（オープン）</b>と<b>秘匿する領域（クローズ）</b>を戦略的に使い分け、市場拡大と利益確保を同時に実現する。
<table>
<tr><th></th><th>クローズ領域</th><th>オープン領域</th></tr>
<tr><td><b>対象</b></td><td>コア技術・差別化の源泉</td><td>インターフェース・周辺技術</td></tr>
<tr><td><b>手段</b></td><td>特許で独占 or ノウハウで秘匿（ブラックボックス化）</td><td>標準化・ライセンス供与・公開</td></tr>
<tr><td><b>目的</b></td><td>競争優位の<b>維持</b></td><td>市場の<b>拡大</b>・エコシステム形成</td></tr>
</table>
</div>

<div class="example">
<b>知的財産の保護手段の使い分け:</b><br>
・<b>特許出願</b>: 技術を公開する代わりに独占権を得る（最長20年）。他社の模倣を法的に排除<br>
・<b>ノウハウ秘匿</b>: 製造方法等を営業秘密として非公開に。期限なしだが、リバースエンジニアリングへの防御が困難<br>
・<b>ライセンス供与</b>: 特許を他社に有償で使用許諾し、ロイヤリティ収入を得る<br><br>

<b>標準化戦略との関係:</b><br>
・<b>デファクトスタンダード</b>（事実上の標準）: 市場競争の結果として標準に（例: Windows、USB）<br>
・<b>デジュールスタンダード</b>（公的標準）: 公的機関が定める規格（例: ISO、JIS）<br>
・オープン領域を<b>標準化</b>して市場を拡大しつつ、クローズ領域で<b>利益を独占</b>するのが理想形<br><br>

<b>企業例:</b><br>
インテル（CPUのコア設計はブラックボックス化 × PCアーキテクチャの規格はオープンに標準化 → Wintel体制で市場支配）
</div>

<p><b>注意</b>: コア技術まで公開すると差別化を失い、全てを秘匿すると市場が広がらない。「何を開き、何を閉じるか」の線引きが知財戦略の最重要判断。チェスブロウのオープンイノベーション（前カード）と表裏一体の概念。</p>

<div class="source">出典: 経産省 オープン&amp;クローズ戦略事例集、TechnoProducer 知財戦略解説、特許庁 知的財産戦略事例集</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

# .apkg出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0412_知財戦略_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
