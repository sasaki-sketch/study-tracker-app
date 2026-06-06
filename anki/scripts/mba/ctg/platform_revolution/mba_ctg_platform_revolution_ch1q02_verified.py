import genanki
import sys
sys.path.insert(0, '/Users/sasaki/02_Personal/anki')
from anki_card_css_template import CARD_CSS

MODEL_ID = 1776237184
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
platform_revolution Ch1 Q2
</div>
パイプライン型とプラットフォーム型の違いを、エコシステムと経営資源との関わり方の観点から説明せよ。"""

answer_html = """<b>エコシステムの観点:</b>
<table border="1" cellpadding="6" cellspacing="0" style="border-collapse:collapse; margin:10px 0;">
<tr><th></th><th>パイプライン型</th><th>プラットフォーム型</th></tr>
<tr><td><b>構造</b></td><td>線形バリューチェーン（原料→製造→販売→消費者）</td><td><b>4層エコシステム</b>（所有者・提供者・作り手・買い手）</td></tr>
<tr><td><b>価値の流れ</b></td><td>一方向</td><td>多方向インタラクション</td></tr>
</table>

<b>プラットフォームの4層構造（iPhoneの例）:</b>
<ul>
<li><b>所有者（Owner）</b> &mdash; Apple：<b>ガバナンス（統治）・IP管理・基本ルール設計</b></li>
<li><b>提供者（Provider）</b> &mdash; iPhone デバイス：ユーザーと作り手を繋ぐインターフェース</li>
<li><b>作り手（Producer）</b> &mdash; アプリ開発者：価値を生み出す</li>
<li><b>買い手（Consumer）</b> &mdash; ユーザー：価値を消費する</li>
</ul>

<b>経営資源との関わり方の観点:</b>
<table border="1" cellpadding="6" cellspacing="0" style="border-collapse:collapse; margin:10px 0;">
<tr><th></th><th>パイプライン型</th><th>プラットフォーム型</th></tr>
<tr><td><b>資源のあり方</b></td><td><b>内部資源を所有・管理</b>（工場・在庫・従業員）</td><td><b>外部資源を編成（orchestrate）</b>（作り手・買い手のネットワーク）</td></tr>
<tr><td><b>成長モデル</b></td><td>内部投資で規模拡大</td><td>ネットワーク参加者の増加で自動的に拡大</td></tr>
<tr><td><b>例</b></td><td>Nokia（端末製造・販売を垂直統合）</td><td>Uber（車を持たない）、Airbnb（不動産を持たない）</td></tr>
</table>

<div class="example">
<b>補足</b><br>
・iPhone <b>単体</b>はモノとしてはパイプライン型製品（Appleが設計・製造・販売）だが、<b>iOS + App Store と組み合わさることで「Provider」として機能</b>し、プラットフォーム型事業全体を支えている<br>
・「所有せず編成する」ことにより、<b>資産軽量（asset-light）</b> と <b>急速なスケーラビリティ</b> を両立できる<br>
・これが「プラットフォーム型事業への移行が市場支配の主要トレンドになる」理由の構造的基盤
</div>

<div class="source">
出典: マーシャル・W・ヴァン・アルスタイン他『パイプライン型事業から脱却せよ_プラットフォーム革命』第1章「プラットフォームの新たな戦略ルール」
</div>"""

my_note = genanki.Note(model=my_model, fields=[question_html, answer_html])
my_deck.add_note(my_note)

output_path = '/Users/sasaki/02_Personal/anki/anki/scripts/mba/ctg/platform_revolution/mba_ctg_platform_revolution_ch1q02_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
