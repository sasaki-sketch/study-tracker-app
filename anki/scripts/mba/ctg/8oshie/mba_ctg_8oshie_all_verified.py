"""
Changing the GAME - DX時代のプラットフォーム競争戦略 MBAのための8つの訓え (全8訓)
出典: 加藤和彦「DX時代のプラットフォーム競争戦略 — MBAのための8つの訓え」名古屋商科大学ビジネススクール
"""
import genanki
import sys
sys.path.insert(0, '/Users/sasaki/02_Personal/anki')
from anki_card_css_template import CARD_CSS

MODEL_ID = 1704140200
DECK_ID = 2704140200

SOURCE_BASE = '加藤和彦「DX時代のプラットフォーム競争戦略 — MBAのための8つの訓え」名古屋商科大学ビジネススクール'

my_model = genanki.Model(
    MODEL_ID,
    'NUCB_EMBA CTG 8Oshie',
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
    'NUCB_EMBA::Changing_the_Game::8つの訓え'
)


def make_card(number, title, article_no, body_html):
    q = f"""<div style="font-size:14px; color:#888; margin-bottom:8px;">
8つの訓え / {number} / 記事{article_no}
</div>
<b>{title}</b><br>
この訓えが示すプラットフォーム戦略の本質・具体例・教訓を答えよ"""

    a = f"""<b>「{title}」</b>（{number}つ目の訓え）

{body_html}

<div class="source">
出典: {SOURCE_BASE} 記事{article_no}
</div>"""
    return q, a


cards = []

# 1: こっちの水は甘いぞ♪ (記事②)
cards.append(make_card(
    "1", "こっちの水は甘いぞ♪", "②",
    """<ul>
<li><b>対応するPF戦略概念:</b> <span class="important">デファクトスタンダード競争における勝ち馬バンドワゴン効果</span></li>
<li><b>訓えの本質:</b> 「自分たちは勝ち組になるから敵陣から逃げてこちらにおいでよ」と<b>敵前逃亡を誘う</b>。あたかも自陣が勝ち組で甘い水が飲めるかのように思わせる「<b>勝ち組を装った振る舞い</b>」をすることで、結果的に多くの参加者を集め、本当に勝ち組になる</li>
</ul>

<b>具体例:</b>
<ul>
<li>VHS vs ベータマックス（ビクターが逆転勝利）</li>
<li>MD（MiniDisc）の消滅</li>
</ul>

<div class="example">
<b>戦略的教訓</b><br>
プラットフォーム競争では、<b>参加者の心理操作</b>が戦略成否を決める重要要素。技術的優劣ではなく「勝ち馬に乗ろうとする心理」を利用する。
</div>"""
))

# 2: 情けは人のためならず (記事③)
cards.append(make_card(
    "2", "情けは人のためならず", "③",
    """<ul>
<li><b>対応するPF戦略概念:</b> <span class="important">プラットフォーム提供者による補完業者への支援投資</span></li>
<li><b>訓えの本意:</b> 情けを人にかけると、それが<b>巡り巡って自分にも良いことが還ってくる</b>という意味（「情けは他人のためにあるのではない＝自分のためになる」）</li>
</ul>

<b>具体例:</b>
<ul>
<li>ゲーム機上で動作するゲームアプリ開発業者への支援</li>
<li>クレジットカードの加盟店拡大支援</li>
</ul>

<div class="example">
<b>戦略的教訓</b><br>
PF戦略では、<b>積極的な情報提供などコミュニティ活性化のための支援</b>を通じて補完業者を育成する。補完業者が成功することで：<br>
- 大ヒット製品の誕生<br>
- 新規ユーザーの獲得<br>
につながる<b>相互的な成長メカニズム</b>が生まれる。
</div>

<b class="important">よくある誤解:</b> 「情けは人のためにならない（甘やかすな）」と誤用されがち。本来は<b>回り回って自分の得になる</b>という意味。"""
))

# 3: 蚊帳の外 (記事④)
cards.append(make_card(
    "3", "蚊帳の外", "④",
    """<ul>
<li><b>対応するPF戦略概念:</b> <span class="important">プラットフォーム競争戦略における隔離戦略</span></li>
<li><b>訓えの本質:</b> ターゲットを「蚊帳の外」に置くことで、<b>周りと同じ便益を得られない状況を創出する</b>。隔たれ・孤立させられることで、余分にコストを払わされる状況を作り出す</li>
</ul>

<div class="example">
<b>具体例: 映画『ソーシャルネットワーク』のFacebook</b><br>
ある大学を取り囲むように周辺大学でFacebookを普及させる → その大学の学生が他大学の学生とSNSでコミュニケーションを取ろうとする際に、<b>Facebookを使わざるを得ない状況</b>が生まれる。
</div>

<b>戦略的教訓:</b> この戦略はSNSだけでなく、<b>様々な場面で活用可能</b>。競合を孤立させ、参加しないことのコストを高める。マルチホーミングコストの意図的上昇の応用。"""
))

# 4: 世の中にタダのものはない (記事⑤)
cards.append(make_card(
    "4", "世の中にタダのものはない", "⑤",
    """<ul>
<li><b>原文:</b> No Such Thing As A Free Lunch</li>
<li><b>対応するPF戦略概念:</b> <span class="important">フリーミアム／ジレットモデルによる初期ユーザー確保</span></li>
<li><b>訓えの本質:</b> プラットフォーム価値は参加者によって創出される。<b>一見無料に見えても、利用者側には何らかの対価が存在する</b>という戦略的認識が重要</li>
</ul>

<div class="example">
<b>具体例: シリコンバレーVCのピッチコンテスト</b><br>
学生に無料のランチ（ピザとコーラ）を提供しながら、VCが新規ビジネスのプレゼンに対してシビアな質問を投げかける。ランチは無料だが、<b>学生はアイデア・時間・評価を対価として提供</b>している。
</div>

<b>戦略的教訓:</b>
<blockquote>「見た目は無料にしても初期ユーザーを早期に確保できるかどうかはプラットフォームの存続にとっての成否を左右する重要な要素」</blockquote>

チキンエッグ問題の打開・クリティカルマス到達のため、一方のユーザーグループを無料化し、もう一方から対価を回収する。"""
))

# 5: むすんで開いて♪ 覆水盆に返らず (記事⑥)
cards.append(make_card(
    "5", "むすんで開いて♪ 覆水盆に返らず", "⑥",
    """<ul>
<li><b>対応するPF戦略概念:</b> <span class="important">プラットフォーム階層におけるオープン・クローズ戦略</span></li>
<li><b>訓えの本質:</b> 特定階層を公開（API等）するか限定するかの意思決定は<b>一度決めたら戻せない</b>。こぼれた水は盆に戻らない</li>
</ul>

<b>具体例:</b>
<ul>
<li><b>Facebook vs MySpace:</b> 階層のオープン化でFacebookが競争勝利</li>
<li><b>Apple (iPod/iPad):</b> 開発者にはオープン、自社階層はクローズドな構造で成功</li>
</ul>

<div class="example">
<b>戦略的教訓: 非対称性に注意</b><br>
<b>「クローズをオープンにすることは容易であるが、逆にオープンをクローズにすることは容易ではない」</b><br>
したがって意思決定は「覆水盆に返らず」の教えのごとく、<b>慎重に</b>行う必要がある。
</div>"""
))

# 6: 漁夫の利 (記事⑦)
cards.append(make_card(
    "6", "漁夫の利", "⑦",
    """<ul>
<li><b>対応するPF戦略概念:</b> <span class="important">プラットフォーム間の相互接続を通じた、他プラットフォームが集めたユーザーネットワークの獲得戦略</span></li>
<li><b>訓えの原典:</b> 2人が争っている時に、第3者が「美味しいところ（利益）」を持っていく</li>
</ul>

<b>戦略メカニズム:</b>
<ul>
<li><b>成長段階のPFにとって:</b> 相互接続によって<b>相手方のもっているネットワーク効果を自分のものにしてしまう</b>手段として機能</li>
<li><b>既存大手PFにとって:</b> ネットワーク効果を奪われてしまう<span class="important">リスク</span></li>
</ul>

<b>具体例:</b> クレジットカード連携、ポイント、ペイメントシステム（〇〇ポイント、△△ペイなど）の相互接続

<div class="example">
<b>戦略的教訓</b><br>
日常生活に組み込まれたサービスがどのような競争戦略を展開しているかを認識することの重要性。自陣が争っている間に、第三者のPFに相互接続を許すとユーザーを持っていかれる可能性がある。
</div>"""
))

# 7: 軒を貸して母屋を取られる (記事⑧)
cards.append(make_card(
    "7", "軒を貸して母屋を取られる", "⑧",
    """<ul>
<li><b>対応するPF戦略概念:</b> <span class="important">プラットフォーム競争戦略における支配的地位の拡大（階層包囲）</span></li>
<li><b>訓えの原典:</b> 商人Aが軒先の一部を商人Bに貸したところ、Bの商売が繁盛し、その後Bが店全体を乗っ取る</li>
</ul>

<b>二重の意味:</b>
<ol>
<li><b>利益の量:</b> 一部を貸したら全部を奪い取られる</li>
<li><b>感情面:</b> 「こちらの善意に付け込まれる」という裏切り感情</li>
</ol>

<div class="example">
<b>PF戦略の文脈</b><br>
上下の階層が相互接続する際に、<b>補完業者として入ってきたプレイヤーがPF全体を支配するに至る</b>現象。プラットフォーム包囲（Platform Envelopment）のメカニズムとも重なる。
</div>

<b>業界での発生:</b> 製造業界、通信業界、医療業界、<b>様々な業界で</b>見られる現象。自らの業界での状況を考察する必要がある。"""
))

# 8: 流水は腐らず (記事⑨)
cards.append(make_card(
    "8", "流水は腐らず", "⑨",
    """<ul>
<li><b>対応するPF戦略概念:</b> <span class="important">プラットフォームのネットワーク効果を維持するためのノイズ除去・品質管理戦略</span></li>
<li><b>訓えの本質:</b> 流れている水は腐らない。プラットフォームも<b>継続的な浄化（ノイズ除去）</b>が必要</li>
</ul>

<blockquote>
「良い循環が生まれればユーザーがユーザーを呼ぶ状態になりますが、ネットワーク内に悪い物（ノイズ）が混入すると、それが循環し、加入ユーザーがプラットフォームから離れていってしまいます」
</blockquote>

<b>ノイズの具体例:</b>
<ul>
<li>SNS上のなりすまし、違法コンテンツ、アダルト系</li>
<li>物販サイトでの詐欺サイト</li>
<li>コミュニティサイトでの荒らし行為</li>
</ul>

<div class="example">
<b>ノイズ除去の実行方法</b>
<ul>
<li>ロボット・AI活用</li>
<li>ユーザー申告</li>
<li>人手による識別</li>
<li><b>相互評価システムの導入</b></li>
</ul>
PF提供者にとって、信頼構築のための継続的なノイズ除去が必須。
</div>"""
))

# assemble deck
assert len(cards) == 8, f"Expected 8 cards, got {len(cards)}"

for q_html, a_html in cards:
    note = genanki.Note(model=my_model, fields=[q_html, a_html])
    my_deck.add_note(note)

output_path = '/Users/sasaki/02_Personal/anki/anki/scripts/mba/ctg/8oshie/mba_ctg_8oshie_all_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
print(f"Total cards: {len(cards)}")
