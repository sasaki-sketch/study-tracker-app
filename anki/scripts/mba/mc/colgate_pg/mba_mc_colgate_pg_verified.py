"""
NUCB EMBA マーケティング・コミュニケーション (GMP105 / 齊木乃里子先生)
Day1 ケース② P&G vs コルゲート「競争ポジションとコミュニケーション」
出典: クラス討議板書 07_コルゲート_P&G + 講義PDF p11(+p5) (マーケティングコミュニケーション2026.pdf) + 認識合わせ
方針: 補完禁止（板書・PDFにある事実のみ。学びの核はユーザー認識合わせを明示）
"""
import genanki
import sys
sys.path.insert(0, '/Users/sasaki/02_Personal/anki')
from anki_card_css_template import CARD_CSS

MODEL_ID = 1980630020
DECK_ID = 1980630021

SOURCE = '板書07_コルゲート_P&G + 講義PDF p11/p5 (マーケティングコミュニケーション2026.pdf) + 認識合わせ'

my_model = genanki.Model(
    MODEL_ID,
    'NUCB_EMBA MktgComm ColgatePG',
    fields=[{'name': 'Question'}, {'name': 'Answer'}],
    templates=[{
        'name': 'Card 1',
        'qfmt': '<div class="question">{{Question}}</div>',
        'afmt': '{{FrontSide}}<hr id="answer"><div class="answer">{{Answer}}</div>'
    }],
    css=CARD_CSS
)

my_deck = genanki.Deck(
    DECK_ID,
    'NUCB_EMBA::Marketing_Communication::02_コルゲートvsP&G'
)


def make_card(no, q_body, a_body):
    q = f"""<div style="font-size:14px; color:#888; margin-bottom:8px;">
NUCBマーコム / Day1 P&G vs コルゲート / カード{no}
</div>
{q_body}"""
    a = f"""{a_body}

<div class="source">
出典: {SOURCE}
</div>"""
    return q, a


cards = []

# ---- カード1: ケースの核 ----
cards.append(make_card(
    "1",
    """「競争ポジションとコミュニケーション」（P&G vs コルゲート）のケースが示す要点を述べよ。""",
    """<b>競争ポジションとコミュニケーション（Competitive Positioning）</b>
<ul>
<li>競争の型＝リーダー／チャレンジャー／フォロワー／ニッチャー。「勝負の仕方」と差別化の程度。</li>
<li><b>新たなカテゴリーをつくる＝競争ポジションを崩す・再編する</b>（市場の軸・新しいルール）→ 結果として <span class="important">「競争しない」</span>（＝線・陣地の引き方）。</li>
<li>競争 ⇔ コミュニケーション ⇔ 収益の三位一体。差別化は「程度」でなく「<b>軸</b>」をずらす。</li>
</ul>
具体: P&G＝新カテゴリー創出で土俵を作る／コルゲート＝否定せず土俵を変えて応戦（詳細は別カード）。"""
))

# ---- カード2: P&Gの一手 ----
cards.append(make_card(
    "2",
    """P&Gはホワイトニング市場でどんな一手を打ったか。（クレスト・ホワイトストリップス）""",
    """<b>クレスト・ホワイトストリップス＝新カテゴリー創出</b>
<ul>
<li>従来3手段（①医者の施術②医者の処方③歯磨ペースト）の隙間を突き、<b>自宅で手軽にホワイトニング</b>。</li>
<li><b>健康・予防 → 美容</b>へ転換。コモディティからの脱却（急成長カテゴリー）。</li>
<li><b>40弗</b>。自分で購入・継続使用＝<b>継続的利益</b>。</li>
<li>訴求は「<b>10倍の効果（b値）</b>」＝効果のデータ表現。</li>
</ul>
<div class="example">
前提（市場構造）: コルゲートNo.1／P&G No.2の寡占。P&Gの体力＝R&D・特許。
</div>"""
))

# ---- カード3: コルゲートの反撃 ----
cards.append(make_card(
    "3",
    """コルゲートはP&Gの新カテゴリーにどう応戦したか。（シンプリーホワイト）""",
    """<b>シンプリーホワイト＝土俵を変えて応戦</b>
<ul>
<li><b>P&Gを否定せず</b>、簡便性・手軽さ・安さで次の市場へ → <span class="important">土俵を変えた</span>。</li>
<li><b>15弗</b>。効能の表現は「<b>同等</b>」という<b>知覚</b>で訴求。</li>
<li>スピード感／（P&Gの）理由（データ）にのらずに。</li>
<li>シーン違い＝<b>生活への定着</b>。ベネフィット・消費者心情に訴える。</li>
</ul>"""
))

# ---- カード4: 学びの核（顧客の知覚の観点） ----
cards.append(make_card(
    "4",
    """P&G vs コルゲートの競争を「顧客の知覚」の観点で説明せよ。<br>─ P&Gの「10倍の効果（b値）」という数字と、コルゲートの「手軽さ・同等」という知覚は、それぞれ顧客にどう届いたか。そこから言える学びは何か。""",
    """<b>学びの核（顧客の知覚の観点）</b>
<ul>
<li>顧客には「10倍の効果（b値）」という<b>数字</b>より、<span class="important">「手軽さ・安さ」と「同等の効果」という知覚</span>のほうが適切に届いた → 幹「<b>知覚されないと意味がない</b>」(PDF p5)の実例。</li>
<li>差別化は「程度」でなく「<b>軸</b>」をずらす。</li>
<li>新カテゴリー創出＝競争ポジションを崩す → 結果<b>「競争しない」</b>（線・陣地の引き方）。</li>
<li>競争 ⇔ コミュニケーション ⇔ 収益の三位一体。「<b>誰が何を感じるか</b>」まで設計して伝え切る。</li>
</ul>"""
))


for q, a in cards:
    my_deck.add_note(genanki.Note(model=my_model, fields=[q, a]))

OUT = '/Users/sasaki/02_Personal/anki/anki/scripts/mba/mc/colgate_pg/mba_mc_colgate_pg_verified.apkg'
genanki.Package(my_deck).write_to_file(OUT)
print(f'OK: {len(cards)} cards -> {OUT}')
