"""
Ankiカード: リエンジニアリング（BPR）
科目: 中小企業診断士_企業経営理論
セクション: 05_組織構造・組織論
作成日: 2026-03-17
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1705010001
deck_id = 1705010002

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_リエンジニアリング',
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
    '中小企業診断士_企業経営理論::05_組織構造・組織論::リエンジニアリング'
)

# カード内容
question = '''ハマーとチャンピーが提唱したBPR（ビジネスプロセス・リエンジニアリング）の<span class="important">定義と4つのキーワード</span>、および業務改善との違いを答えよ'''

answer = '''<b>Business Process Re-engineering（BPR）</b>（リエンジニアリング）

<p>ハマー＆チャンピー（M. Hammer &amp; J. Champy, 1993）が『Reengineering the Corporation』で提唱。</p>

<div class="formula">
<b>定義（原文の4つのキーワード）:</b><br>
「<b>コスト・品質・サービス・スピード</b>のような重大なパフォーマンス基準を<b>劇的に（Dramatically）</b>改善するために、ビジネスプロセスを<b>根本的に（Fundamental）</b>考え直し、<b>抜本的に（Radical）</b>デザインし直すこと」

<table>
<tr><th>キーワード</th><th>英語</th><th>意味</th></tr>
<tr><td><b>根本的</b></td><td>Fundamental</td><td>「なぜこの業務をやっているのか」から問い直す</td></tr>
<tr><td><b>抜本的</b></td><td>Radical</td><td>既存の改良ではなく、ゼロベースで再設計</td></tr>
<tr><td><b>劇的</b></td><td>Dramatic</td><td>微小な改善ではなく、飛躍的な成果を目指す</td></tr>
<tr><td><b>プロセス</b></td><td>Process</td><td>個別の業務ではなく、業務の流れ全体を対象</td></tr>
</table>
</div>

<div class="example">
<b>業務改善（カイゼン）との違い:</b>
<table>
<tr><th></th><th>BPR（リエンジニアリング）</th><th>業務改善（カイゼン）</th></tr>
<tr><td><b>対象</b></td><td>業務プロセス<b>全体</b></td><td>個別の業務・作業</td></tr>
<tr><td><b>アプローチ</b></td><td>ゼロベースで<b>再設計</b></td><td>既存プロセスの<b>改良</b></td></tr>
<tr><td><b>変化の度合い</b></td><td><b>劇的</b>・非連続</td><td><b>漸進的</b>・連続</td></tr>
<tr><td><b>頻度</b></td><td>一時的（プロジェクト型）</td><td>継続的</td></tr>
</table>
<br>
<b>具体例:</b><br>
フォード社の買掛金部門: 従来500人で行っていた業務を、プロセス全体を再設計して125人に削減（75%減）。個別業務の効率化ではなく、承認フロー・書類・システムをゼロから設計し直した。
</div>

<p><b>注意</b>: BPRは1990年代に大流行したが、「抜本的すぎて組織の抵抗が大きい」「人員削減の口実に使われた」等の批判もあり、その後は業務改善との組み合わせが主流に。インクリメンタル（漸進的改善）とラディカル（抜本的改革）の対比は、イノベーションの4分類と同じ構造。</p>

<div class="source">出典: M. Hammer &amp; J. Champy (1993)『Reengineering the Corporation』、NRI BPR用語解説、カオナビ BPR解説</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

# .apkg出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0501_リエンジニアリング_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
