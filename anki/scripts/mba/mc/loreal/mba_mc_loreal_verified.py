"""
NUCB EMBA マーケティング・コミュニケーション (GMP105 / 齊木乃里子先生)
Day1 ケース① ロレアル「ブランドを受け皿とした一貫性」
出典: クラス討議板書 08_ロレアル + 講義PDF p10 (マーケティングコミュニケーション2026.pdf) + 認識合わせ
方針: 補完禁止（板書・PDFにある事実のみ。3レンズはユーザーの学びの核として明示）
"""
import genanki
import sys
sys.path.insert(0, '/Users/sasaki/02_Personal/anki')
from anki_card_css_template import CARD_CSS

MODEL_ID = 1980630010
DECK_ID = 1980630011

SOURCE = '板書08_ロレアル + 講義PDF p10 (マーケティングコミュニケーション2026.pdf) + 認識合わせ'

my_model = genanki.Model(
    MODEL_ID,
    'NUCB_EMBA MktgComm Loreal',
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
    'NUCB_EMBA::Marketing_Communication::01_ロレアル'
)


def make_card(no, q_body, a_body):
    q = f"""<div style="font-size:14px; color:#888; margin-bottom:8px;">
NUCBマーコム / Day1 ロレアル / カード{no}
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
    """ロレアルのケースが示す「ブランドを受け皿としたコミュニケーション（一貫性）」とは何か。要点を述べよ。""",
    """<b>Brand-anchored consistency（ブランドを受け皿とした一貫性）</b>
<ul>
<li>すべての活動（製品ライン・チャネル・メディア・人材育成）を<b>ブランドに従属</b>させる。軸は <span class="important">ブランドアイデンティティ＝「バラのシンボル」≠個別商品</span>。</li>
<li>市場ごとに取り組みは変えるが、一貫性は譲らない＝標準化と適応化（本部で「型」、現地に裁量[価格]、アイデンティティ/デザインは「ランコム」で統一）。</li>
<li><b>アートから仕組みへ → PDCA</b>。強いブランド＝明確なアイデンティティとそれを守り強化する連続（＝命）。</li>
</ul>
<div class="example">
<b>適用場面:</b> 多品種・多支店・多従業員を抱え、現場任せだとブランドの一貫性が崩れやすい組織（グローバル大企業に限らず国内の多店舗・多人数組織にも応用可）。逆に単一商品・少人数の小規模企業では論点になりにくい。
</div>"""
))

# ---- カード2: ロレアルの強さ＝3要素 ----
cards.append(make_card(
    "2",
    """ロレアルの「強い」ブランドを支えた3要素を述べよ。""",
    """<b>ロレアルの強さ＝3要素</b>（冷静な分析による経営判断／人間総合力／弾み）
<ol>
<li><b>冷静な分析による経営判断</b><br>
…事業の集中（製品ライン縮小・赤字商品の絞り込み）／R&Dの積極投資／アートから仕組みへ → PDCA</li>
<li><b>人間総合力</b>（熱意・勤勉さ・忍耐・想像力 など）<br>
→ その結果、<span class="important">ブランドを語れる人（BA）が育つ・増える</span>（トップのコミュニケーション、創業者とガバナンスも下支え）</li>
<li><b>弾み</b>（PDF太字キーワード）<br>
…勢い・連続性・好循環。①の冷静な判断＋熱意で地盤を築き、跳ねるタイミングが必然に起こるよう設計する</li>
</ol>
<b class="important">要点:</b> ①(仕組み)が③(弾み)の必然性を設計し、②(人の資質)がブランドを語れる人を生んで現場で体現・伝達する。"""
))

# ---- カード3: 「弾み」の意味 ----
cards.append(make_card(
    "3",
    """ロレアルの文脈における「弾み」とは何か。（講義PDF p10「『強い』ブランド：定義と弾み」の太字キーワード）""",
    """<b>弾み（momentum）</b><br>
<span style="font-size:13px; color:#888;">※PDFは「定義と弾み」と並記するのみで定義は明記なし。以下は文脈上の理解。</span>
<ul>
<li>「勢い・連続性・好循環」のすべてを含む。</li>
<li><b>冷静な判断（事業の集中・R&Dの積極投資）と熱意で地盤を築き、跳ねるタイミングが必然に起こるよう設計する</b>。</li>
<li>実例: ヘアダイの収益 → 化粧品へ投下／高級路線の成功体験を次へ活かす連続〔板書②〕。</li>
<li>「強いブランド＝明確なアイデンティティとそれを守り強化する連続（＝命）」の"連続"が弾みを生む。</li>
</ul>"""
))

# ---- カード4: 標準化と適応化 ----
cards.append(make_card(
    "4",
    """ロレアルのグローバル展開における「標準化と適応化」の考え方を述べよ。""",
    """<b>標準化と適応化（Standardization &amp; Adaptation）— ロレアル</b>
<ul>
<li><b>本部で「型」をつくり、現地に裁量を持たせる</b>（裁量の代表＝価格）〔板書⑤〕。</li>
<li>市場ごとに取り組みは違うが一貫性はある〔PDF p10〕。「変える／変えない」に意図を持つ。</li>
<li><span class="important">アイデンティティ・デザインは「ランコム」としてグローバルで統一＝一貫性は譲らない</span>〔板書⑤〕。</li>
<li>現地化の実務: 現地での商品テスト／流通・メディアの現地化／買収ブランドの技術転用〔板書⑤〕。</li>
</ul>
<div class="example">
<b>関連原則（国際展開・PDF p12）:</b> 標準化⇔適応化は「戦略・メッセージ・媒体」の軸で考え、「戦略と手段を間違えない」。
</div>"""
))


for q, a in cards:
    my_deck.add_note(genanki.Note(model=my_model, fields=[q, a]))

OUT = '/Users/sasaki/02_Personal/anki/anki/scripts/mba/mc/loreal/mba_mc_loreal_verified.apkg'
genanki.Package(my_deck).write_to_file(OUT)
print(f'OK: {len(cards)} cards -> {OUT}')
