"""
Ankiカード: 特許ライセンス戦略（プロパテント・クロスライセンス・パテントプール）
科目: 中小企業診断士_企業経営理論
セクション: 04_技術経営・イノベーション
作成日: 2026-03-16
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1704160001
deck_id = 1704160002

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_特許ライセンス戦略',
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
    '中小企業診断士_企業経営理論::04_技術経営・イノベーション::特許ライセンス戦略'
)

# カード内容
question = '''プロパテント政策の定義と歴史的背景、および<span class="important">クロスライセンス・パテントプール・オープンライセンス</span>の違いと使い分けを答えよ'''

answer = '''<b>Patent Licensing Strategy</b>（特許ライセンス戦略）

<p>特許をどう活用するかは、知財戦略の中核。独占するだけでなく、ライセンス形態を使い分けて事業優位を築く。</p>

<div class="formula">
<b>プロパテント（Pro-Patent）の2つのレベル:</b><br>
① <b>国家政策</b>: 国（政府・司法・特許庁）が特許権者に有利な法制度・司法判断・行政運用を整える政策スタンス。対義語はアンチパテント。<br>
② <b>企業戦略</b>: 企業が特許を積極的に取得・行使し、訴訟（差止請求権・損害賠償請求権）等の法的手段で特許を守る戦略姿勢。ただし知財戦略の「一つのアプローチ」であり、守るだけでなく活用（ライセンス・標準化）も知財戦略の柱。

<table>
<tr><th></th><th>アンチパテント時代</th><th>プロパテント転換後</th></tr>
<tr><td><b>特許訴訟</b></td><td>権利者の敗訴率<b>90%近く</b></td><td>権利者が勝ちやすくなった</td></tr>
<tr><td><b>賠償額</b></td><td>低額</td><td>数百億〜数千億円規模に</td></tr>
<tr><td><b>米国の契機</b></td><td>大恐慌で独占排除</td><td><b>ヤングレポート</b>（1985）＋<b>CAFC設立</b>（1982・特許専門裁判所）</td></tr>
<tr><td><b>日本</b></td><td>―</td><td>2002年<b>知的財産基本法</b>制定で転換</td></tr>
<tr><td><b>副作用</b></td><td>イノベーション成果を保護できない</td><td><b>パテントトロール</b>の横行</td></tr>
</table>
<br>
<b>パテントトロール（PAE: Patent Assertion Entity）:</b><br>
自ら製品を製造せず、特許を買い集めて大企業を訴え、和解金で稼ぐ企業。<br>
例: VirnetX社がAppleを提訴 → FaceTime等の特許侵害で約500億円の賠償命令
</div>

<div class="example">
<b>3つのライセンス形態:</b>
<table>
<tr><th>形態</th><th>定義</th><th>具体事例</th></tr>
<tr><td><b>クロスライセンス</b></td><td>2社以上が互いの特許を<b>相互に許諾</b></td><td>サムスンとAppleが特許紛争を経て相互ライセンスで和解</td></tr>
<tr><td><b>パテントプール</b></td><td>複数企業が特許を持ち寄り<b>一括ライセンス</b></td><td><b>MPEG-LA</b>: 25社がMPEG-2特許を持ち寄り、約1500社に一括ライセンス。FRAND条件（公正・合理的・非差別的）で料金設定</td></tr>
<tr><td><b>オープンライセンス</b></td><td>特許を<b>無償 or 低額で広く公開</b></td><td>テスラがEV特許を無償公開 → EV市場全体を拡大し、充電規格で主導権を握る</td></tr>
</table>
</div>

<p><b>注意</b>: パテントプールは独占禁止法の規制を受ける。プロパテント政策が強すぎるとパテントトロールを生むため、近年は米国でも揺り戻しがある。「国の政策スタンス」が企業の知財戦略の前提条件を決める関係にある。</p>

<div class="source">出典: 特許庁 パテントプールテキスト、知財タイムズ パテントトロール、Wikipedia パテントプール</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

# .apkg出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0416_特許ライセンス戦略_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
