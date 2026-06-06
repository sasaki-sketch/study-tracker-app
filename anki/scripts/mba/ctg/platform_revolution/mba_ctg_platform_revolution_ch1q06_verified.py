import genanki
import sys
sys.path.insert(0, '/Users/sasaki/02_Personal/anki')
from anki_card_css_template import CARD_CSS

MODEL_ID = 1776237188
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
platform_revolution Ch1 Q6
</div>
プラットフォーム型事業では、5forcesの各要因の境界がなぜ曖昧になるのか。パイプライン型との対比で説明せよ。"""

answer_html = """<b>パイプライン型:</b><br>
5forces（競合・買い手・サプライヤー・新規参入・代替品）の各要因の<b>境界が明確で安定的</b>。セメントメーカーや航空会社は、顧客・競争相手・納入業者の区分が固定されており、戦略分析の前提が揺らがない。
<br><br>
<b>プラットフォーム型:</b><br>
5forcesの各要因の<b>境界が目まぐるしく変化</b>する。同じプレイヤーが「競合」「協力者」「顧客」「サプライヤー」の複数の役割を同時に、または時期によって担うため。
<br><br>
<b>境界曖昧化の具体例:</b>
<table border="1" cellpadding="6" cellspacing="0" style="border-collapse:collapse; margin:10px 0;">
<tr><th>企業関係</th><th>協力者としての顔</th><th>競合としての顔</th></tr>
<tr><td><b>Samsung &harr; Apple</b></td><td>iPhoneの部品サプライヤー</td><td>スマホ市場の直接競合</td></tr>
<tr><td><b>Amazon &harr; 出版社</b></td><td>販売チャネル（流通パートナー）</td><td>Kindleで自社出版の競合</td></tr>
<tr><td><b>Uber &harr; 運転手</b></td><td>サプライヤー（供給側）</td><td>アプリのユーザー（顧客側）</td></tr>
</table>

<b>エコシステム内部の力学:</b><br>
境界曖昧化は企業間だけでなく、<b>エコシステム内の参加者の役割自体が流動的</b>:
<ul>
<li><b>作り手↔買い手の入れ替わり</b> &mdash; プラットフォームを最も利用する売り手は、しばしば買い手にもなる（例: メルカリで売る人＝買う人）</li>
<li><b>参加者→競合への転換</b> &mdash; プラットフォーム上で成長した参加者が、自前のプラットフォームを構築して離脱・競合化する（例: Amazonマーケットプレイスの大手出品者がD2Cサイトへ移行）</li>
<li><b>統治の課題</b> &mdash; 参加者の役割が流動的であるがゆえに、ルール設計・インセンティブ設計・品質管理が繊細な経営課題となる</li>
</ul>

<b>なぜ曖昧になるか（構造的理由）:</b>
<ol>
<li><b>多サイド構造</b> &mdash; 参加者が複数の役割を兼ねる（供給者＝顧客＝競合）</li>
<li><b>エコシステムの動的変化</b> &mdash; プラットフォームの成長に伴い、参加者の役割が変わる</li>
<li><b>補完と競合の同居（Co-opetition）</b> &mdash; プラットフォーム上の参加者は協力しつつ競争する</li>
</ol>

<div class="example">
<b>補足</b><br>
・パイプライン型の「敵/味方」の二項対立は、プラットフォーム型では成立しない<br>
・5forcesに従って「障壁を築く」と、エコシステム参加者を排除してしまう危険がある（Q5で扱った論点）<br>
・プラットフォーム型の競争分析には、5forcesに代わる新しいフレームワーク（エコシステム分析、ネットワーク効果の強度分析等）が必要<br>
・エコシステム内部の力学（役割の流動性）を理解し、<b>統治の仕組み</b>で対応することが経営者の課題
</div>

<div class="source">
出典: マーシャル・W・ヴァン・アルスタイン他『パイプライン型事業から脱却せよ_プラットフォーム革命』第1章「プラットフォームの新たな戦略ルール」§6 プラットフォームはどう戦略を変化させるか / エコシステム内部の力学
</div>"""

my_note = genanki.Note(model=my_model, fields=[question_html, answer_html])
my_deck.add_note(my_note)

output_path = '/Users/sasaki/02_Personal/anki/anki/scripts/mba/ctg/platform_revolution/mba_ctg_platform_revolution_ch1q06_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
