import genanki
import sys
sys.path.insert(0, '/Users/sasaki/02_Personal/anki')
from anki_card_css_template import CARD_CSS

MODEL_ID = 1776237189
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
platform_revolution Ch1 Q7
</div>
従来のアウトソーシングとプラットフォーム型の外部志向はどう異なるか。段階的な変化を説明せよ。"""

answer_html = """<b>3段階の変化:</b>
<table border="1" cellpadding="6" cellspacing="0" style="border-collapse:collapse; margin:10px 0;">
<tr><th>段階</th><th>内容</th><th>目的</th><th>例</th></tr>
<tr><td><b>&①従来のアウトソーシング</b></td><td>コスト削減目的で一部業務を外注（管理は社内）</td><td>コスト削減</td><td>コールセンター外注、IT保守委託</td></tr>
<tr><td><b>&②外部ネットワークの組織化</b></td><td>外部参加者が自律的に職能活動を担う仕組みを設計</td><td>価値創造・イノベーション</td><td>Apple Support Communities、P&amp;G Connect+Develop</td></tr>
<tr><td><b>&③完全な肩代わり</b></td><td>かつて企業が自前でこなしていた職能を外部が主導</td><td>エコシステム自体が機能する</td><td>Wikipedia（編集＝ユーザー）、YouTube（制作＝クリエイター）</td></tr>
</table>

<b>本質的な違い:</b>
<ul>
<li><b>アウトソーシング</b>: 業務の<b>委託</b>（企業が管理主体、指示→実行の関係）</li>
<li><b>プラットフォーム型外部志向</b>: 外部ネットワークの<b>組織化</b>（参加者が自律的に動く仕組みを設計）</li>
</ul>

<b>具体的な職能の外部化:</b>
<table border="1" cellpadding="6" cellspacing="0" style="border-collapse:collapse; margin:10px 0;">
<tr><th>職能</th><th>内部志向（従来）</th><th>外部志向（プラットフォーム型）</th></tr>
<tr><td><b>R&amp;D</b></td><td>自社研究所で開発</td><td>オープンイノベーション</td></tr>
<tr><td><b>マーケティング</b></td><td>自社広告部門</td><td>ユーザー生成コンテンツ（UGC）・口コミ</td></tr>
<tr><td><b>顧客サポート</b></td><td>自社コールセンター</td><td>ユーザーコミュニティが相互に解決</td></tr>
<tr><td><b>品質管理</b></td><td>自社検査部門</td><td>レビュー・評価システム</td></tr>
<tr><td><b>IT</b></td><td>社内システム管理</td><td>クラウド＋API＋外部開発者</td></tr>
</table>

<div class="example">
<b>補足</b><br>
・原文では「パイプライン型企業はかねてからアウトソーシングしてきたが、現在ではさらに踏み込んで外部ネットワークを組織化し、職能活動を完全に肩代わりしてもらう方向へ進んでいる」と指摘<br>
・IBM、インテル、JPモルガン等の大企業も分散型組織への転換を進めている<br>
・この転換を可能にするのがプラットフォームの設計力（インセンティブ・ルール・信頼メカニズム）であり、単なる「外注先を増やす」こととは根本的に異なる
</div>

<div class="source">
出典: マーシャル・W・ヴァン・アルスタイン他『パイプライン型事業から脱却せよ_プラットフォーム革命』第1章「プラットフォームの新たな戦略ルール」§7 ネットワークが促す外部志向への転換
</div>"""

my_note = genanki.Note(model=my_model, fields=[question_html, answer_html])
my_deck.add_note(my_note)

output_path = '/Users/sasaki/02_Personal/anki/anki/scripts/mba/ctg/platform_revolution/mba_ctg_platform_revolution_ch1q07_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
