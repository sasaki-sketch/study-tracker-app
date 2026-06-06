"""
Ankiカード: イノベーションの4分類（ヘンダーソン＝クラーク）
科目: 中小企業診断士_企業経営理論
セクション: 04_技術経営・イノベーション
作成日: 2026-03-16
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1704090001
deck_id = 1704090002

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_イノベーション4分類',
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
    '中小企業診断士_企業経営理論::04_技術経営・イノベーション::イノベーションの4分類'
)

# カード内容
question = '''ヘンダーソンとクラークによるイノベーションの<span class="important">4分類</span>（部品知識×構造知識）の定義と具体例を答えよ'''

answer = '''<b>Henderson-Clark Innovation Framework</b>（ヘンダーソン＝クラークの4分類）

<p>ヘンダーソンとクラーク（1990）が提唱。イノベーションを<b>部品（コンポーネント）の知識</b>と<b>構造（アーキテクチャ）の知識</b>の2軸で4つに分類した。</p>

<div class="formula">
<table>
<tr><th></th><th>部品の知識：<b>既存</b></th><th>部品の知識：<b>刷新</b></th></tr>
<tr><td>構造の知識：<b>既存</b></td><td><b>インクリメンタル</b>（漸進的）</td><td><b>モジュラー</b></td></tr>
<tr><td>構造の知識：<b>刷新</b></td><td><b>アーキテクチュラル</b></td><td><b>ラディカル</b>（急進的）</td></tr>
</table>
<br>
<b>英語の意味:</b><br>
・<b>Radical</b>（ラディカル）= 根本的な、急進的な → 部品も構造も<b>根こそぎ変える</b><br>
・<b>Incremental</b>（インクリメンタル）= 漸進的な、少しずつの → <b>少しずつ改良</b>する<br>
・<b>Architectural</b>（アーキテクチュラル）= 構造的な、設計思想の → <b>組み合わせ方を変える</b><br>
・<b>Modular</b>（モジュラー）= 部品単位の → <b>部品だけ入れ替える</b>
</div>

<div class="example">
<b>具体例:</b><br>
・<b>インクリメンタル</b>: デジカメの画素数向上、PCのCPU高速化 ― 部品も構造も既存の延長<br>
・<b>モジュラー</b>: ガラケーのアナログ→デジタル通信化 ― 通信部品は刷新、製品構造は同じ<br>
・<b>アーキテクチュラル</b>: ウォークマン（据置型→携帯型）― 部品は既存技術だが、組み合わせ方を根本的に変えた<br>
・<b>ラディカル</b>: ガソリン車→EV ― モーター・バッテリー（部品刷新）＋車体設計（構造刷新）の両方が変わる
</div>

<p><b>注意</b>: 既存企業にとって最も脅威なのは<b>アーキテクチュラルイノベーション</b>。<span class="important">ラディカルは明らかに全く新しいので認識自体は早いが、アーキテクチュラルは認識に時間がかかる</span>。気づいた時には手遅れになるのが最大の脅威。</p>

<p><b>なぜ認識が遅れるか:</b><br>
① 部品技術は既存のままなので、各部門は「自分の担当部品は変わっていない」と感じる<br>
② 変化は部品間の<b>組み合わせ方（＝部門間の連携構造）</b>にあるが、これは個人ではなく<b>組織の情報チャネルやルーティンに埋め込まれている</b><br>
③ 結果、組織の既存フィルターが変化を見落とす → 「大した変化ではない」と軽視 → 対応が遅れる<br>
（ラディカルは部品も構造も新しいので、誰が見ても「これは別物だ」と気づける）</p>

<p>クリステンセンの「破壊的イノベーション」とは別の分類軸であり混同しないこと。</p>

<div class="source">出典: Henderson &amp; Clark (1990) "Architectural Innovation"、一発合格まとめシート R5再試第7問</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

# .apkg出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0409_イノベーションの4分類_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
