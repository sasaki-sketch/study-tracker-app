import genanki
import sys
sys.path.insert(0, '/Users/sasaki/02_Personal/anki')
from anki_card_css_template import CARD_CSS

MODEL_ID = 1776237185
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
platform_revolution Ch1 Q3
</div>
パイプライン型の内部最適化とプラットフォーム型の外部インタラクション促進の違いを、価値創造メカニズムの観点から説明せよ。"""

answer_html = """<b>価値創造メカニズムの比較:</b>
<table border="1" cellpadding="6" cellspacing="0" style="border-collapse:collapse; margin:10px 0;">
<tr><th></th><th>パイプライン型</th><th>プラットフォーム型</th></tr>
<tr><td><b>価値創造の源泉</b></td><td>バリューチェーン（主活動・支援活動）の<b>内部プロセス最適化</b></td><td>外部の作り手と買い手の<b>コア・インタラクション</b></td></tr>
<tr><td><b>主戦場</b></td><td>効率化・品質向上・コスト削減</td><td>マッチング・信頼・摩擦低減</td></tr>
<tr><td><b>管理対象</b></td><td>自社の人・モノ・プロセス</td><td>外部参加者の行動（直接命令不可）</td></tr>
<tr><td><b>経営者の能力</b></td><td>オペレーション管理・生産管理</td><td><b>エコシステム統治・ルール設計</b></td></tr>
<tr><td><b>代表例</b></td><td>Toyotaの生産方式、WalmartのSCM</td><td>Airbnbのマッチング、YouTubeの動画流通</td></tr>
</table>

<b>コア・インタラクション（Core Interaction）とは:</b><br>
プラットフォーム上で最も重要な生産者↔消費者の取引のこと。どの取引がプラットフォームの価値を生むかを特定し、<b>頻度高く・摩擦なく・質高く</b>起こすことが経営の主戦場となる。
<ul>
<li>Uber: 乗客↔運転手のマッチング</li>
<li>Airbnb: ゲスト↔ホストの宿泊取引</li>
<li>YouTube: 視聴者↔クリエイターの動画視聴</li>
</ul>

<div class="example">
<b>補足</b><br>
・パイプライン型では経営者は<b>従業員に命令</b>できるが、プラットフォーム型では参加者に命令できない。<b>インセンティブ設計・ルール設計・信頼メカニズム</b>で<b>間接的に誘導</b>する必要がある（統治が難しい理由）<br>
・KPIも根本変化する: 原価・在庫回転 → <b>マッチング成功率・取引完了率・NPS・エンゲージメント</b><br>
・内部最適化の知見（リーン、TQM等）はプラットフォーム型では中核的優位にならない
</div>

<div class="source">
出典: マーシャル・W・ヴァン・アルスタイン他『パイプライン型事業から脱却せよ_プラットフォーム革命』第1章「プラットフォームの新たな戦略ルール」§3 内部の最適化から外部とのインタラクションへ
</div>"""

my_note = genanki.Note(model=my_model, fields=[question_html, answer_html])
my_deck.add_note(my_note)

output_path = '/Users/sasaki/02_Personal/anki/anki/scripts/mba/ctg/platform_revolution/mba_ctg_platform_revolution_ch1q03_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
