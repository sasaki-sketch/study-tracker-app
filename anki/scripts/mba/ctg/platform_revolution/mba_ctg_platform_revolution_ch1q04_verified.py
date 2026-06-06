import genanki
import sys
sys.path.insert(0, '/Users/sasaki/02_Personal/anki')
from anki_card_css_template import CARD_CSS

MODEL_ID = 1776237186
DECK_ID = 2776237184

my_model = genanki.Model(
    MODEL_ID,
    'NUCB_EMBA Textbook QA',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    templates=[{
        'name': 'Card 1',
        'qfmt': '<div class="question">{{Question}}</div>',
        'afmt': '{{FrontSide}}<hr id="answer"><div class="answer">{{Answer}}</div>'
    }],
    css=CARD_CSS
)

my_deck = genanki.Deck(
    DECK_ID,
    'NUCB_EMBA::Changing_the_Game::プラットフォーム革命::Ch1_新たな戦略ルール'
)

question_html = """<div style="font-size:14px; color:#888; margin-bottom:8px;">
platform_revolution Ch1 Q4
</div>
なぜプラットフォーム型事業では個別顧客のLTV最大化ではなくエコシステム全体価値の最大化が必要なのか、多サイド構造とネットワーク効果の観点から説明せよ。"""

answer_html = """<b>結論:</b><br>
プラットフォーム型事業は<b>複数サイドの参加者が相互依存</b>して価値を生むため、個別顧客のLTVを最大化すると<b>他サイドの離脱を招き、結果的に全体価値が損なわれる</b>。ネットワーク効果を働かせるには「誰を補助し誰から利益を得るか」をエコシステム全体で設計する必要がある。
<br><br>
<b>理由1: 多サイド構造の相互依存性</b><br>
プラットフォームには買い手・作り手という複数サイドが存在し、片方の収益最大化は他方を離脱させる:
<ul>
<li>Amazonが買い手有利な価格統制を強めると作り手が離脱 → 品揃え減 → 買い手も離脱</li>
<li>Seller LTV と Buyer LTV は独立ではなく、クロスサイドで結合している</li>
</ul>

<b>理由2: ネットワーク効果が働く構造</b><br>
参加者が増えるほど他の参加者にとっての価値が指数的に増大する（正のフィードバック）:
<ul>
<li>作り手↑ → 買い手の選択肢↑ → 買い手↑ → 作り手の市場↑ → さらに作り手↑</li>
<li>個別のLTVが低いユーザーでも<b>ネットワーク全体の引力</b>として機能する</li>
<li>例: Uberの低価格需要層が運転手の定着を促し、供給側の厚みを生む</li>
</ul>

<b>理由3: 補助（Subsidize）戦略が必要</b><br>
エコシステム成長のため、<b>意図的に一方のサイドを補助</b>する判断が求められる:
<table border="1" cellpadding="6" cellspacing="0" style="border-collapse:collapse; margin:10px 0;">
<tr><th>事例</th><th>補助対象</th><th>目的</th></tr>
<tr><td>PayPal</td><td>新規ユーザーに現金ボーナス</td><td>ユーザー集積→売り手流入</td></tr>
<tr><td>Uber</td><td>運転手にサインアップボーナス</td><td>供給確保→サービス魅力向上</td></tr>
<tr><td>Microsoft Windows</td><td>開発者に無料SDK提供</td><td>アプリ集積→ユーザー価値向上</td></tr>
</table>
個別LTVだけを見ると「補助対象＝赤字顧客＝切るべき」という誤判断に至る。

<div class="example">
<b>補足</b><br>
・<b>低LTV顧客を切るべきか残すべきか</b>の判断は、両者で真逆になり得る:<br>
&nbsp;&nbsp;- パイプライン型: LTV &lt; CAC なら切る（正しい）<br>
&nbsp;&nbsp;- プラットフォーム型: 低LTVでもネットワーク引力として不可欠な場合、残す（補助する）<br>
・この発想は節8「重点を置くべきところ」および節10「業績指標」で深掘りされる<br>
・結局、プラットフォームの経営判断は<b>個別最適より全体最適</b>を優先する構造
</div>

<div class="source">
出典: マーシャル・W・ヴァン・アルスタイン他『パイプライン型事業から脱却せよ_プラットフォーム革命』第1章「プラットフォームの新たな戦略ルール」§4 顧客価値の重視からエコシステム価値の重視へ
</div>"""

my_note = genanki.Note(model=my_model, fields=[question_html, answer_html])
my_deck.add_note(my_note)

output_path = '/Users/sasaki/02_Personal/anki/anki/scripts/mba/ctg/platform_revolution/mba_ctg_platform_revolution_ch1q04_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
