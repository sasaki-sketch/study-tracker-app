"""
NUCB EMBA マーケティング・コミュニケーション (GMP105 / 齊木乃里子先生)
Day1 ケース③ ダイソン「異質市場の理解 / 提供価値の改革」(+ 国際展開枠組み p12)
出典: クラス討議板書 06_ダイソン + 講義PDF p13/p12 (マーケティングコミュニケーション2026.pdf) + 認識合わせ
方針: 補完禁止（板書・PDFにある事実のみ。D&B=Different&Better/インナーブランディングはユーザー認識合わせ。刺身理論は先生の比喩で詳細未説明＝補足注記のみ）
"""
import genanki
import sys
sys.path.insert(0, '/Users/sasaki/02_Personal/anki')
from anki_card_css_template import CARD_CSS

MODEL_ID = 1980630030
DECK_ID = 1980630031

SOURCE = '板書06_ダイソン + 講義PDF p13/p12 (マーケティングコミュニケーション2026.pdf) + 認識合わせ'

my_model = genanki.Model(
    MODEL_ID,
    'NUCB_EMBA MktgComm Dyson',
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
    'NUCB_EMBA::Marketing_Communication::03_ダイソン'
)


def make_card(no, q_body, a_body):
    q = f"""<div style="font-size:14px; color:#888; margin-bottom:8px;">
NUCBマーコム / Day1 ダイソン / カード{no}
</div>
{q_body}"""
    a = f"""{a_body}

<div class="source">
出典: {SOURCE}
</div>"""
    return q, a


cards = []

# ---- カード1: D&B（Different & Better）＝インナーブランディング ----
cards.append(make_card(
    "1",
    """ダイソンの学びの核「D&B（Different &amp; Better）」とは何か。なぜ「インナーブランディング」として機能するのか。""",
    """<b>D&amp;B（Different &amp; Better）</b>
<ul>
<li>ただ「違う」だけ／ただ「良い」だけでなく、<b>違いを際立たせ、かつ優れている</b>こと。</li>
<li>〔PDF p13〕重要なのは「<b>違い</b>」であって「程度」ではない／市場起点ならスペックでなく<b>ベネフィット</b>が基本。</li>
<li><span class="important">インナーブランディングとして機能</span>：社内の<b>エンジニア集団とアート（デザイン）集団</b>を、D&amp;Bという共通の判断基準・合言葉で<b>育て・束ねる</b>軸になっている（デザイン→エンジニアリングまで一貫内製〔板書⑨〕）。</li>
<li>ベネフィットの見える化：「<b>ゴミが見える</b>」「<b>吸引力が衰えない</b>」。</li>
</ul>
<div style="font-size:13px; color:#888;">※「刺身理論」＝違いを"伝えられる形"にする、という先生の比喩（詳細説明なし・一般理論ではない）。</div>"""
))

# ---- カード2: 市場をベネフィットから知る ----
cards.append(make_card(
    "2",
    """ダイソンは日本市場をどう理解し、どう知覚を作ったか。（市場をベネフィットから知る）""",
    """<b>市場をベネフィットから知る</b>
<ul>
<li>日本独自調査「<b>掃除って？</b>」を問う → ターゲット設定。技術者が<b>現地訪問</b>（家のスペース課題・使われ方を観察）。</li>
<li><b>FGI</b>（一般ユーザー vs ダイソンユーザー[満足]）: 有名メーカー志向＝受動的／こだわり・情報収集＝積極的。</li>
<li>新しいニーズ＝<b>アレルギー・花粉・ペット</b> → ダイソンの技術が活きる（排気がキレイ）。</li>
<li><b>量販店配荷↑ → デモ・実演 → 理解／口コミの誘発</b>。</li>
</ul>
<b class="important">要点:</b> 市場を「知る方法」もベネフィットから整理する（スペックでなく、顧客のベネフィットを起点に調べる）。"""
))

# ---- カード3: 拡張のジレンマと国際展開 ----
cards.append(make_card(
    "3",
    """ダイソンが直面する「拡張のジレンマ」と、国際展開における標準化・適応化の原則を述べよ。""",
    """<b>拡張 ⇔ コモディティ化、そして国際展開</b>
<ul>
<li>ラインナップ拡充・他カテゴリー展開（空調・家電から脱却＝「生活軸のメーカー」へ）⇔ <span class="important">コモディティ化・競合登場リスク</span>（独自性の希薄化）。</li>
<li>対処＝<b>原点（D&amp;B・体験）に立ち戻る</b>＝「ダイソンを売る」。</li>
</ul>
<b>国際展開の原則:</b>
<ul>
<li>〔PDF p12〕標準化⇔適応化は「<b>戦略・メッセージ・媒体</b>」の軸で考え、「戦略と手段を間違えない」。</li>
<li>〔PDF p13〕標準化・適応化は<b>表現方法に過ぎず、主体は整合性・一貫性・ストーリー性</b>。「何を変えて何を変えないか」に意図を持つ。</li>
</ul>"""
))


for q, a in cards:
    my_deck.add_note(genanki.Note(model=my_model, fields=[q, a]))

OUT = '/Users/sasaki/02_Personal/anki/anki/scripts/mba/mc/dyson/mba_mc_dyson_verified.apkg'
genanki.Package(my_deck).write_to_file(OUT)
print(f'OK: {len(cards)} cards -> {OUT}')
