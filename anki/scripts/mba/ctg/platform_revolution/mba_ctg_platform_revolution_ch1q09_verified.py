import genanki
import sys
sys.path.insert(0, '/Users/sasaki/02_Personal/anki')
from anki_card_css_template import CARD_CSS

MODEL_ID = 1776237191
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
platform_revolution Ch1 Q9
</div>
プラットフォーム事業を立ち上げる際に「量より質、狭く始めて広げる」が定石とされる理由を説明せよ。"""

answer_html = """<b>定石: 量より質、狭く始めて広げる</b><br>
PF事業の核心は作り手と買い手の<b>インタラクション</b>であり、立ち上げ期はその<b>質を最大化</b>することが最優先。量を先に追うと失敗する。
<br><br>
<b>なぜ「質が先」か:</b>
<ol>
<li><b>マッチング精度</b> &mdash; 参加者が少ない初期は、特定ユーザー群に絞ることで高精度なマッチングが可能</li>
<li><b>体験の好循環</b> &mdash; 質の高いインタラクション → 満足 → 定着 → 口コミ → 自然成長</li>
<li><b>負のスパイラル回避</b> &mdash; 量を追う → マッチング精度低下 → 体験悪化 → 離脱 → PF崩壊</li>
</ol>

<b>なぜ「狭く始める」か:</b><br>
特定のユーザー群に対して確実に価値提供できるPFを作り、ティッピング・ポイントを超えてから隣接市場へ拡張する。
<br><br>
<b>Facebookの例:</b><br>
ハーバード大学のみ → Ivy League → 全米大学 → 一般公開
<ul>
<li>初期は「ハーバード学生同士」という極めて狭いコミュニティで高密度のインタラクションを実現</li>
<li>各段階で十分なネットワーク効果を確立してから次の市場へ</li>
</ul>

<b>LinkedInの例:</b>
<ul>
<li>求人↔求職者の人脈マッチングに集中 → プロフィール充実 → ショーケース → コンテンツPFへ段階的に拡張</li>
</ul>

<div class="example">
<b>補足</b><br>
・この定石はQ4（エコシステム価値）・Q5（ネットワーク効果）の実践的応用<br>
・「誰を補助するか」（Q4）→ 初期は特定ユーザー群に集中投資<br>
・「ティッピング・ポイント」（Q5）→ 狭い市場で先に超えてから拡張<br>
・<b>逆の失敗例</b>: Google+ は最初から全ユーザーに開放 → インタラクションが希薄 → 定着せず終了
</div>

<div class="source">
出典: マーシャル・W・ヴァン・アルスタイン他『パイプライン型事業から脱却せよ_プラットフォーム革命』第1章「プラットフォームの新たな戦略ルール」重点を置くべきところ
</div>"""

my_note = genanki.Note(model=my_model, fields=[question_html, answer_html])
my_deck.add_note(my_note)

output_path = '/Users/sasaki/02_Personal/anki/anki/scripts/mba/ctg/platform_revolution/mba_ctg_platform_revolution_ch1q09_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
