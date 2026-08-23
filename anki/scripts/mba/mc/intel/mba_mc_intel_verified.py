"""
NUCB EMBA マーケティング・コミュニケーション (GMP105 / 齊木乃里子先生)
Day2 ケース② インテル「協業相手・取引先を動かす（産業財）/ B2B2C・Intel Inside」
出典: クラス討議板書 04_インテル + 講義PDF p.14「産業財のマーケティングコミュニケーション」/ p.15「協業相手・取引先を動かす（インテル）」+ 認識合わせ
方針: 補完禁止（板書・PDFにある事実のみ。学びの核はユーザーの視点として明示）
"""
import genanki
import sys
sys.path.insert(0, '/Users/sasaki/02_Personal/anki')
from anki_card_css_template import CARD_CSS

MODEL_ID = 1980630050
DECK_ID = 1980630051

SOURCE = '板書04_インテル + 講義PDF p.14-15 + 認識合わせ'

my_model = genanki.Model(
    MODEL_ID,
    'NUCB_EMBA MktgComm Intel',
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
    'NUCB_EMBA::Marketing_Communication::05_インテル'
)


def make_card(no, q_body, a_body):
    q = f"""<div style="font-size:14px; color:#888; margin-bottom:8px;">
NUCBマーコム / Day2 インテル / カード{no}
</div>
{q_body}"""
    a = f"""{a_body}

<div class="source">
出典: {SOURCE}
</div>"""
    return q, a


cards = []

# ---- カード1: 産業財の核＝誰を動かすか（B2B2C）＋ 慎重さ ----
cards.append(make_card(
    "1",
    """インテルのケースが示す「産業財コミュニケーション」の核は何か。要点を述べよ。""",
    """<b>産業財コミュニケーションの核 — 「誰を動かすか」の再設計（B2B2C）</b>
<ul>
<li>産業財 vs 消費財＝「<b>相手」を動かす条件と施策</b>（意思決定の構造／リーチすべき人・部署・機能／差別化／収益性／産業財ブランド＝「<span class="important">約束</span>」）〔PDF p.14〕。顧客＝<b>B2B／B2B2C／B2BのためのC</b>。</li>
<li>課題：<span class="important">386が普及しない</span>（486発売前・コモディティ化）。従来の伝達相手「<b>設計エンジニア」が採用しない</b>＝チャネルのパワー↓。</li>
<li>転換：<b>動かす相手を変える</b> → CIO/ITマネジャー（EU）・最終消費者へ。「<span class="important">直接の相手を飛び越える</span>」（B2B2Cの本質）。</li>
</ul>
<div class="example">
<b>学び〔自分の視点〕：</b>インテルは PR を<span class="important">慎重（控えめ）に</span>進めた — 直接の取引先である <b>PC メーカーを怒らせてはいけない</b>から（"飛び越える"リスク／レッドX看板＝控えめ訴求）。<b>一方でマネジャーはメンバーにエンドユーザー向け PR への"挑戦"を許した</b> ＝ 関係配慮と大胆な挑戦の両立。
</div>"""
))

# ---- カード2: Intel Inside＝見える化と「圧」の設計 ----
cards.append(make_card(
    "2",
    """Intel Inside キャンペーンは何を行い、どう「選ばれる構造」を作ったか。""",
    """<b>Intel Inside — 見える化と「圧」の設計</b>
<ul>
<li>「<span class="important">まる字は商標にならない</span>」（数字など単純な標章は商標登録できない＝独占不可）→ Intel Inside CP（ライセンスブランド・世界で統一）＝<b>所有できるブランド資産</b>。</li>
<li><b>共同広告（インセンティブ）</b>：EUに成分（インテル）を見てもらう／メディアミックス（音のシール）。</li>
<li><span class="important">スペックを説明しない＝感覚で伝える</span>（見える化）。Bに新たな発見をさせ動いてもらう<b>ストーリー → 「仕組み」に昇華</b>〔PDF p.15〕。</li>
<li>メーカーが「<b>入れざるをえない状況</b>」＝<span class="important">圧の設計</span>（買い替えサイクルにも介入）。</li>
</ul>"""
))

# ---- カード3: エンドユーザー戦略＝見えない部品をブランド化 ----
cards.append(make_card(
    "3",
    """インテルのエンドユーザー戦略の要点は何か。""",
    """<b>エンドユーザー戦略 — 見えない部品をブランド化</b>
<ul>
<li>最終消費者に PC のよさと「<span class="important">選ぶ理由</span>」を提供。</li>
<li>目に見えない部品を、性能を説明せず<b>感覚・イメージ</b>でブランド形成（<b>ブルーマン</b>素材／インテルが身近にある表現）。</li>
<li>独自イメージ＝<b>尖ったブランド</b>／価格・技術レベル以外での<span class="important">知覚</span>。</li>
<li>「相手が実現したいこと」だからこそ知覚が重要〔PDF p.15〕／産業財ブランド＝「約束」、共同広告という<b>仕組み</b>でストーリーを昇華。</li>
</ul>
<div class="example">
<b>学び〔自分の視点〕：</b>インテルはブランド価値（<span class="important">信頼性 reliability ＋ 先進性 innovativeness</span>）を、<b>ブルーマンに託して</b>届けた（性能を語らず、感覚・イメージで）。
</div>"""
))


for q, a in cards:
    my_deck.add_note(genanki.Note(model=my_model, fields=[q, a]))

OUT = '/Users/sasaki/02_Personal/anki/anki/scripts/mba/mc/intel/mba_mc_intel_verified.apkg'
genanki.Package(my_deck).write_to_file(OUT)
print(f'OK: {len(cards)} cards -> {OUT}')
