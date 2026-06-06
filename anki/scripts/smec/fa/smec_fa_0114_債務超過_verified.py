"""
債務超過 - 中小企業診断士 財務会計
Insolvency / Negative Net Worth

作成日: 2026-03-01
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1740824201
DECK_ID = 1740824202

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_債務超過',
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
    '中小企業診断士_財務会計::01_経営分析::債務超過'
)

# カード内容
question = """債務超過の定義・判定方法・赤字との違い・解消方法を答えよ"""

answer = """<b>Insolvency / Negative Net Worth</b>（債務超過）

<b>定義</b>: 企業の<b>負債総額が資産総額を上回り、純資産がマイナス</b>になっている状態

<div class="formula">
\\[\\text{純資産} = \\text{資産合計} - \\text{負債合計} &lt; 0 \\implies \\text{債務超過}\\]
</div>

<b>判定方法</b>: 貸借対照表（B/S）の純資産の部がマイナスかどうかを確認。簿価ベースだけでなく<b>実態B/S</b>（時価評価）での判定も重要。

<b>赤字との違い</b>:
<table>
<tr><th>項目</th><th>債務超過</th><th>赤字</th></tr>
<tr><td>基準</td><td>貸借対照表（B/S）</td><td>損益計算書（P/L）</td></tr>
<tr><td>意味</td><td>負債 &gt; 資産（ストック）</td><td>費用 &gt; 収益（フロー）</td></tr>
<tr><td>即倒産？</td><td>しない（資金繰りが続けば存続可能）</td><td>しない</td></tr>
</table>

<b>影響</b>:
<ul>
<li>金融機関からの<b>新規融資が困難</b>に</li>
<li>上場企業は<b>1年以内に解消しないと上場廃止</b>（JPX基準）</li>
<li>取引先からの<b>信用低下</b></li>
</ul>

<b>主な解消方法</b>:
<table>
<tr><th>方法</th><th>内容</th></tr>
<tr><td>増資</td><td>新株発行で資本金を増加</td></tr>
<tr><td>DES（Debt Equity Swap）</td><td>債務を株式に転換（負債↓・資本↑）</td></tr>
<tr><td>利益改善</td><td>売上増加・コスト削減で利益を蓄積</td></tr>
<tr><td>資産売却</td><td>遊休資産等を売却して負債返済</td></tr>
</table>

<div class="important">注意:</div>
債務超過 ≠ 倒産。倒産は「支払不能（資金ショート）」であり、債務超過でもキャッシュフローがあれば事業継続可能。逆に債務超過でなくても資金繰りが詰まれば倒産する。

<div class="source">出典: M&Aキャピタルパートナーズ、マネーフォワード、日本M&Aセンター</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0114_債務超過_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
