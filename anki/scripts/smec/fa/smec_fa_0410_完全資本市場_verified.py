"""
完全資本市場 - 中小企業診断士 財務会計
Perfect Capital Market

作成日: 2026-03-01
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1740825201
DECK_ID = 1740825202

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_完全資本市場',
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

# デッキ定義
deck = genanki.Deck(
    DECK_ID,
    '中小企業診断士_財務会計::04_ファイナンス::完全資本市場'
)

# カード内容
question = """完全資本市場の定義・仮定条件・関連理論を答えよ"""

answer = """<b>Perfect Capital Market</b>（完全資本市場 / 完全市場）

<b>定義</b>: 市場の摩擦的要因が存在せず、競争的市場の条件を満たす<b>理想的な市場</b>。ファイナンス理論のベンチマーク（基準点）として用いられる。

<b>仮定条件</b>:
<table>
<tr><th>条件</th><th>内容</th></tr>
<tr><td>税金なし</td><td>法人税・所得税が存在しない</td></tr>
<tr><td>取引コストなし</td><td>手数料・発行費用がゼロ</td></tr>
<tr><td>情報の対称性</td><td>すべての参加者が同じ情報を持つ（完全情報）</td></tr>
<tr><td>プライステイカー</td><td>個々の投資家の売買が価格に影響を与えない</td></tr>
<tr><td>資金の自由な調達</td><td>企業も個人も同一条件で借入可能</td></tr>
</table>

<b>完全市場を前提とする主な理論</b>:
<table>
<tr><th>理論</th><th>完全市場での結論</th></tr>
<tr><td>MM理論（通常版）</td><td>資本構成は企業価値に無関連</td></tr>
<tr><td>配当無関連命題</td><td>配当政策は企業価値に影響しない</td></tr>
<tr><td>配当落ち</td><td>株価は1株当たり配当額だけ正確に下落</td></tr>
</table>

<b>試験での読み方</b>:
問題文に「完全市場」「税金・取引コストは存在しない」と書かれたら:
<ul>
<li>株価は企業価値を<b>正確に反映</b>する</li>
<li>配当・資本構成の変化は<b>理論通りに</b>株価へ反映される</li>
</ul>

<div class="important">注意:</div>
現実には税金・取引コスト・情報の非対称性が存在するため、完全市場は成り立たない。MM理論の修正版（法人税あり）やトレードオフ理論は、完全市場の仮定を緩めた理論である。

<div class="source">出典: みずほ証券ファイナンス用語集、スタディング中小企業診断士、Wikipedia</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0410_完全資本市場_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
