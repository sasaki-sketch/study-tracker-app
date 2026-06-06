import genanki
import sys
sys.path.insert(0, '/Users/sasaki/02_Personal/anki')
from anki_card_css_template import CARD_CSS

MODEL_ID = 1776237183
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
platform_revolution Ch1 Q1
</div>
プラットフォーム戦略は既存市場にどのような影響を与えるか。その理由を簡潔に述べよ。"""

answer_html = """<b>影響:</b><br>
既存のパイプライン型（垂直統合型）企業の競争優位が急速に失われる。<br>
例: AppleのiPhone + App Storeが、携帯電話市場で圧倒的地位にあったNokiaを駆逐した。
<br><br>
<b>理由（メカニズム）:</b>
<ol>
<li><b>価値創造の構造転換</b> &mdash; 線形のバリューチェーン（原料→製造→販売）から、生産者・プラットフォーム・消費者の<b>多方向インタラクション</b>へ</li>
<li><b>資産のシフト</b> &mdash; 工場・在庫などの有形資産から、取引・信頼・コミュニティといった<b>「インタラクション」自体</b>がコア資産になる</li>
<li><b>ネットワーク効果</b> &mdash; 参加者が増えるほど価値が増大する<b>正のフィードバック</b>が働き、個別企業の製品改良を凌駕する</li>
</ol>

<div class="example">
<b>補足</b><br>
・パイプライン型企業は「製品改良・コスト効率」に注力しがちだが、プラットフォーム企業は「場の設計・エコシステム成長」に注力する<br>
・既存企業がプラットフォーム型に転換できない最大の理由は、既存の物理的資産・販売チャネル・組織構造が逆に制約（負の遺産）となるため<br>
・Apple vs Nokia以外にも、Amazon vs 書店、Airbnb vs ホテル、Uber vs タクシー等、多くの業界で同じ転換が起きている
</div>

<div class="source">
出典: マーシャル・W・ヴァン・アルスタイン他『パイプライン型事業から脱却せよ_プラットフォーム革命』第1章「プラットフォームの新たな戦略ルール」§1 パイプラインからプラットフォームへ
</div>"""

my_note = genanki.Note(model=my_model, fields=[question_html, answer_html])
my_deck.add_note(my_note)

output_path = '/Users/sasaki/02_Personal/anki/anki/scripts/mba/ctg/platform_revolution/mba_ctg_platform_revolution_ch1q01_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
