import genanki
import sys
sys.path.insert(0, '/Users/sasaki/02_Personal/anki')
from anki_card_css_template import CARD_CSS

MODEL_ID = 1776237187
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
platform_revolution Ch1 Q5
</div>
ネットワーク効果がプラットフォーム型事業の核心とされる理由を、5forcesとの対比とWinner-Takes-All構造の観点から論じよ。"""

answer_html = """<b>結論:</b><br>
ネットワーク効果は<b>需要サイドの規模の経済</b>であり、参加者の増加そのものが価値を生む構造をもたらす。これは外部要因を「脅威」と見る5forces理論の前提を覆し、強く働いた場合はWinner-Takes-Allの寡占を引き起こすため、プラットフォーム型事業の競争戦略の核心となる。
<br><br>
<b>理由1: 価値創造構造の根本転換（需要サイドの規模の経済）</b>
<table border="1" cellpadding="6" cellspacing="0" style="border-collapse:collapse; margin:10px 0;">
<tr><th></th><th>供給側の規模の経済（伝統的）</th><th>需要側の規模の経済（ネットワーク効果）</th></tr>
<tr><td><b>メカニズム</b></td><td>生産量↑ → 単位コスト↓</td><td>利用者↑ → 1人あたりの価値↑</td></tr>
<tr><td><b>優位性の源泉</b></td><td>製造規模・設備投資</td><td>参加者集積・マッチング精度・データ</td></tr>
<tr><td><b>代表</b></td><td>製造業（パイプライン型）</td><td>プラットフォーム型</td></tr>
</table>

<b>理由2: 5forcesとの根本的対立</b>
<table border="1" cellpadding="6" cellspacing="0" style="border-collapse:collapse; margin:10px 0;">
<tr><th>観点</th><th>5forces（1979）</th><th>プラットフォーム型</th></tr>
<tr><td><b>外部要因の捉え方</b></td><td>サプライヤー・買い手・新規参入・代替品・競合 = <b>すべて自社利益を奪う脅威</b></td><td>供給サイド・顧客 = <b>ネットワーク参加者＝価値創出資産</b></td></tr>
<tr><td><b>戦略の方向性</b></td><td>障壁を築き、外部から自社を防衛</td><td>参加者を引き寄せ、エコシステムを繁栄させる</td></tr>
<tr><td><b>不適合の理由</b></td><td>障壁を築くと参加者を排除 → ネットワーク効果が働かず<b>逆効果</b></td><td>&mdash;</td></tr>
</table>
<b>例:</b> 楽天が出店者に厳しい条件を課す（5forces的発想）→ 出店者離脱 → 商品多様性↓ → 利用者離脱という負のスパイラル
<br><br>
<b>理由3: Winner-Takes-All（WTA）構造を生む</b><br>
強いネットワーク効果は<b>ティッピング・ポイント</b>を境に勝者総取りの寡占を引き起こす:
<ul>
<li>参加者↑ → 価値↑ → さらに参加者↑（正のフィードバック・ループ）</li>
<li>一度規模で先行されると、後発企業は「価値で劣る」状態に陥り逆転困難</li>
<li>例: Facebook、LinkedIn、Visa/Mastercard、Microsoft Windows</li>
</ul>
<b>WTAにならない条件（例外）:</b>
<ul>
<li><b>マルチホーミング</b>が容易（Uber と Lyft を併用、配達アプリ複数併用）</li>
<li><b>地理的制約</b>がある（地域別タクシー、地域別フリマ）</li>
<li><b>ニッチの差別化余地</b>がある</li>
</ul>

<div class="example">
<b>補足</b><br>
・ネットワーク効果はデータ蓄積と結合して<b>フライホイール</b>化する: 参加者↑ → データ↑ → AI精度↑ → マッチング↑ → 価値↑ → 参加者↑<br>
・例: Netflixのレコメンド、Google検索精度、Amazonの商品提案<br>
・<b>戦略示唆</b>: 競争の主戦場は「機能・品質」ではなく「<b>ティッピング・ポイントを誰が先に超えるか</b>」になる<br>
・新規参入企業の参入障壁は技術ではなく<b>ネットワーク規模そのもの</b>
</div>

<div class="source">
出典: マーシャル・W・ヴァン・アルスタイン他『パイプライン型事業から脱却せよ_プラットフォーム革命』第1章「プラットフォームの新たな戦略ルール」§5 ネットワーク効果の威力
</div>"""

my_note = genanki.Note(model=my_model, fields=[question_html, answer_html])
my_deck.add_note(my_note)

output_path = '/Users/sasaki/02_Personal/anki/anki/scripts/mba/ctg/platform_revolution/mba_ctg_platform_revolution_ch1q05_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
