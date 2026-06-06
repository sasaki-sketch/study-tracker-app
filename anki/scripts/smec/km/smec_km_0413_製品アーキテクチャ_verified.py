"""
Ankiカード: 製品アーキテクチャ（モジュラー・インテグラル）
科目: 中小企業診断士_企業経営理論
セクション: 04_技術経営・イノベーション
作成日: 2026-03-16
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1704130001
deck_id = 1704130002

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_製品アーキテクチャ',
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
    '中小企業診断士_企業経営理論::04_技術経営・イノベーション::製品アーキテクチャ'
)

# カード内容
question = '''製品アーキテクチャにおける<span class="important">モジュラー型とインテグラル型の定義・違い</span>、日本企業の競争力との関係、および<span class="important">オープン・クローズドとの2×2分類</span>を答えよ'''

answer = '''<b>Product Architecture: Modular vs Integral</b>（製品アーキテクチャ）

<p>藤本隆宏が体系化。製品を構成部品にどう分割し、機能をどう配分するかという<b>基本的な設計思想</b>。</p>

<div class="formula">
<b>Modular（モジュラー型）= 組み合わせ型:</b><br>
部品と機能が<b>1対1</b>に対応。標準化された部品を組み合わせて製品を構成。<br><br>

<b>Integral（インテグラル型）= 擦り合わせ型:</b><br>
部品と機能が<b>多対多</b>に交錯。部品間の相互調整（擦り合わせ）が不可欠。

<table>
<tr><th></th><th>モジュラー型</th><th>インテグラル型</th></tr>
<tr><td><b>部品と機能</b></td><td>1対1（独立）</td><td>多対多（交錯）</td></tr>
<tr><td><b>設計の要点</b></td><td>インターフェースの標準化</td><td>部品間の微細な相互調整</td></tr>
<tr><td><b>開発スピード</b></td><td>速い（部品単位で並行開発）</td><td>遅い（全体最適が必要）</td></tr>
<tr><td><b>模倣のしやすさ</b></td><td>容易（部品を買えば作れる）</td><td>困難（暗黙知が必要）</td></tr>
<tr><td><b>具体例</b></td><td>デスクトップPC、レゴ</td><td>自動車、オートバイ</td></tr>
</table>
</div>

<div class="example">
<b>オープン・クローズドとの2×2分類:</b>
<table>
<tr><th></th><th>オープン（業界標準）</th><th>クローズド（自社標準）</th></tr>
<tr><td><b>モジュラー</b></td><td>デスクトップPC、USB</td><td>初期の任天堂ゲーム機</td></tr>
<tr><td><b>インテグラル</b></td><td>―（理論上は少ない）</td><td>自動車、精密機器</td></tr>
</table>
<br>
<b>日本企業の競争力との関係:</b><br>
・日本企業の強み = <b>統合能力（擦り合わせ力）</b> → インテグラル型に相性が良い<br>
・日本企業の弱み = <b>選択能力</b> → モジュラー型の組み合わせ競争では不利<br>
・自動車産業で日本が強く、PC・スマホでシェアを失った背景はこのアーキテクチャの違いで説明できる
</div>

<p><b>注意</b>: 製品アーキテクチャは固定的ではなく、技術の成熟とともにインテグラル→モジュラーへ移行する傾向がある（モジュラー化）。これはA-Uモデルの移行期→固定期の標準化と対応する。EV化により自動車もモジュラー化が進みつつあり、日本の擦り合わせ優位が脅かされている。</p>

<div class="source">出典: 藤本隆宏 RIETI DP 02-J-008、Koto Online 製品アーキテクチャ解説、コベルコシステム 擦り合わせ力</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

# .apkg出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0413_製品アーキテクチャ_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
