"""
Ankiカード: イノベーションの進化パターン
科目: 中小企業診断士_企業経営理論
セクション: 04_技術経営・イノベーション
作成日: 2026-03-16
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1704190001
deck_id = 1704190002

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_イノベーション進化パターン',
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
    '中小企業診断士_企業経営理論::04_技術経営・イノベーション::イノベーションの進化パターン'
)

# カード内容
question = '''イノベーションの進化に見られる特徴的パターンとして、<span class="important">技術のS字カーブ</span>、<span class="important">経路依存性</span>、<span class="important">セイリングシップ効果</span>の定義と具体例を答えよ'''

answer = '''<b>Innovation Evolution Patterns</b>（イノベーションの進化パターン）

<p>技術のイノベーションは特徴的な変化パターンをとりながら進化する。</p>

<div class="formula">
<table>
<tr><th>パターン</th><th>英語</th><th>定義</th></tr>
<tr><td><b>技術のS字カーブ</b></td><td>Technology S-curve</td><td>技術の性能向上が<b>緩やか→急速→頭打ち</b>のS字型を描く。知識の蓄積と資源投入の収斂が原因</td></tr>
<tr><td><b>経路依存性</b></td><td>Path Dependency</td><td>過去の技術選択が<b>将来の発展方向を制約</b>する。優れた技術でも社会システムとの相互依存により転換が困難</td></tr>
<tr><td><b>セイリングシップ効果</b></td><td>Sailing Ship Effect</td><td>新技術の脅威に対抗して<b>既存技術が改良・延命</b>される現象</td></tr>
</table>
</div>

<div class="example">
<b>具体例:</b><br>
・<b>S字カーブ</b>: HDDの記憶容量（初期は緩やか→磁気技術の成熟で急成長→物理限界で頭打ち → 次のS字カーブ=SSDへ移行）。フォスター（R. Foster）が提唱<br>
・<b>経路依存性</b>: QWERTY配列（タイプライター時代の制約で設計 → 非効率でも社会全体が慣れているため変更できない）。技術的に優れていても「ロックイン」される<br>
・<b>セイリングシップ効果</b>: 蒸気船の登場後、帆船が大幅に改良され性能向上した。ガラケーもスマホ登場後に高機能化が加速した<br><br>

<b>技術の不均衡と進化の駆動力:</b><br>
技術システムの<b>不均衡</b>（技術間の発展度合いのギャップ）がイノベーションを推進する力となる。均衡状態ではイノベーションの動機が生まれにくい。
</div>

<p><b>注意</b>: S字カーブの「頭打ち」は技術の限界だが、セイリングシップ効果により<b>予測より延命される</b>ことがある（要素部品の改良や使い手のレベルアップ）。また、経路依存性があるため、技術的に優れているだけでは事業の成功に結びつかない点は、補完的資産（前カード）の議論とも関連する。</p>

<div class="source">出典: R. Foster『Innovation: The Attacker's Advantage』、H30第9問</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

# .apkg出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0419_イノベーションの進化パターン_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
