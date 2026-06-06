import genanki
import sys
sys.path.insert(0, '/Users/sasaki/02_Personal/anki')
from anki_card_css_template import CARD_CSS

MODEL_ID = 1776237190
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
platform_revolution Ch1 Q8
</div>
パイプライン型企業がプラットフォーム事業者から受ける3つの脅威パターンを説明せよ。"""

answer_html = """<b>3つの介入パターン:</b>
<table border="1" cellpadding="6" cellspacing="0" style="border-collapse:collapse; margin:10px 0;">
<tr><th>#</th><th>パターン</th><th>メカニズム</th><th>具体例</th></tr>
<tr><td><b>&①</b></td><td><b>既存PFが他業界から参入</b></td><td>既存のネットワーク効果を武器に隣接市場へ乗り込む</td><td>Google → スマホ（Android）、Amazon → クラウド（AWS）</td></tr>
<tr><td><b>&②</b></td><td><b>競合がPF事業を投入</b></td><td>顧客層の重複する競合がパイプライン型にPFモデルを追加</td><td>Nike → Nike+（ランニングコミュニティ）、John Deere → MyJohnDeere</td></tr>
<tr><td><b>&③</b></td><td><b>異業種PFが市場の垣根を超える</b></td><td>共通の顧客層を持つ異業種PFが市場を横断して参入</td><td>Apple（音楽PF）→ 決済（Apple Pay）、WeChat（メッセージ）→ 金融・EC・配車</td></tr>
</table>

<b>パイプライン型企業にとっての含意:</b>
<ul>
<li><b>脅威の発生源が予測困難</b>: 同業界だけでなく、業界外・異業種から脅威が来る</li>
<li>5forcesの「新規参入の脅威」の範囲が従来よりはるかに広い</li>
<li>特にパターン①③は、既にネットワーク効果を持つ巨大PFが参入するため、対抗が極めて困難</li>
</ul>

<div class="example">
<b>補足</b><br>
・パイプライン型のマネジャーは、一見無関係に思えるプラットフォーム事業者を脅威として認識すべき<br>
・ウォルマート vs Amazonの例: 小売の競合関係だったが、Amazonはマーケットプレイス（PF）＋AWS＋物流PFと多面展開し、パイプライン型では対抗不能な領域へ拡大<br>
・防衛策は「自らもPF要素を取り込む」か「PFが提供できないニッチ価値に集中する」
</div>

<div class="source">
出典: マーシャル・W・ヴァン・アルスタイン他『パイプライン型事業から脱却せよ_プラットフォーム革命』第1章「プラットフォームの新たな戦略ルール」エコシステムが発揮する力
</div>"""

my_note = genanki.Note(model=my_model, fields=[question_html, answer_html])
my_deck.add_note(my_note)

output_path = '/Users/sasaki/02_Personal/anki/anki/scripts/mba/ctg/platform_revolution/mba_ctg_platform_revolution_ch1q08_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
