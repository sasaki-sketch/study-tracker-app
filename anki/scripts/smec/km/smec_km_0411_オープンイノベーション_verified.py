"""
Ankiカード: オープンイノベーション
科目: 中小企業診断士_企業経営理論
セクション: 04_技術経営・イノベーション
作成日: 2026-03-16
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1704110001
deck_id = 1704110002

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_オープンイノベーション',
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
    '中小企業診断士_企業経営理論::04_技術経営・イノベーション::オープンイノベーション'
)

# カード内容
question = '''チェスブロウが提唱したオープンイノベーションの定義、<span class="important">クローズドイノベーションとの違い</span>、および<span class="important">インバウンド型・アウトバウンド型</span>の分類と具体例を答えよ'''

answer = '''<b>Open Innovation</b>（オープンイノベーション）

<p>チェスブロウ（H.W. Chesbrough, 2003）が提唱。企業の内部と外部の技術・アイデアの流動性を意図的に高め、イノベーションを加速するモデル。</p>

<div class="formula">
<b>クローズド vs オープン:</b>
<table>
<tr><th></th><th>クローズド（Closed）</th><th>オープン（Open）</th></tr>
<tr><td><b>知識の流れ</b></td><td>社内で完結（自前主義）</td><td>社内外を双方向に流通</td></tr>
<tr><td><b>前提</b></td><td>優秀な人材は自社にいる</td><td>優秀な人材は社外にもいる</td></tr>
<tr><td><b>R&amp;D</b></td><td>自社で研究→開発→製品化</td><td>外部の知識も活用、自社技術も外部に展開</td></tr>
<tr><td><b>典型的時代</b></td><td>1980〜90年代</td><td>2000年代〜</td></tr>
</table>
<br>
<b>2つの方向:</b><br>
・<b>インバウンド型</b>（Outside-In）: 外部の技術・知識を<b>社内に取り込む</b><br>
・<b>アウトバウンド型</b>（Inside-Out）: 自社の技術・知識を<b>外部に展開</b>する
</div>

<div class="example">
<b>具体例:</b><br>
・<b>インバウンド型</b>: P&amp;Gの「Connect + Develop」（外部発明家の技術を製品に採用）、大企業によるスタートアップへの出資・M&amp;A<br>
・<b>アウトバウンド型</b>: IBMのLinuxへの特許開放、自社で事業化しない特許のライセンス供与、スピンオフ・カーブアウト<br><br>

<b>クローズドの限界:</b><br>
自前主義では、研究開発コストの増大・開発スピードの遅延・技術の陳腐化リスクに対応できなくなった。人材の流動性が高まり、一社に知識を囲い込むことが困難に。
</div>

<p><b>注意</b>: オープンイノベーション ≠ 技術のタダ乗り。外部から取り込むだけでなく、自社技術を外部に提供して収益化する「アウトバウンド型」も重要な柱。また、自社のコア技術まで公開する必要はなく、<b>何を開き、何を閉じるか</b>の戦略的判断が鍵となる。</p>

<div class="example">
<b>試験頻出の引っかけポイント（R5第30問）:</b><br>
・消費者との共同開発製品は新奇性・評価は高いが、<b>PLCが短い</b>傾向がある<br>
・クラウド<b>ソーシング</b>（業務の外部委託）≠ クラウド<b>ファンディング</b>（資金調達）→ 混同注意<br>
・市場ニーズ重視で自社単独開発 = <b>ニーズ志向</b>（シーズ志向ではない）
</div>

<div class="source">出典: H.W. Chesbrough (2003)『Open Innovation』、JMAC 用語集、Sony Acceleration Platform、企業経営理論 R5第30問</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

# .apkg出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0411_オープンイノベーション_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
