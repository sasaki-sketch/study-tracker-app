"""
NUCB EMBA マーケティング・コミュニケーション (GMP105 / 齊木乃里子先生)
Day2 ケース① サムスン「異質市場の理解 / OEM脱却→ブランド経営・市場ドリブン」
出典: クラス討議板書 03_サムスン + 資料5 M-Net分析(Corstjens & Merrihue, "Optimal Marketing," HBR 2003.10 p.117) + 講義PDF p.12-13 + 認識合わせ
方針: 補完禁止（板書・PDF・資料5にある事実のみ。学びの核①②はユーザーの視点として明示）
"""
import genanki
import sys
sys.path.insert(0, '/Users/sasaki/02_Personal/anki')
from anki_card_css_template import CARD_CSS

MODEL_ID = 1980630040
DECK_ID = 1980630041

SOURCE = '板書03_サムスン + 資料5 M-Net分析(Corstjens &amp; Merrihue, Optimal Marketing, HBR 2003.10 p.117) + 講義PDF p.12-13 + 認識合わせ'

my_model = genanki.Model(
    MODEL_ID,
    'NUCB_EMBA MktgComm Samsung',
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
    'NUCB_EMBA::Marketing_Communication::04_サムスン'
)


def make_card(no, q_body, a_body):
    q = f"""<div style="font-size:14px; color:#888; margin-bottom:8px;">
NUCBマーコム / Day2 サムスン / カード{no}
</div>
{q_body}"""
    a = f"""{a_body}

<div class="source">
出典: {SOURCE}
</div>"""
    return q, a


cards = []

# ---- カード1: ケースの核＝旗を立てる（OEM短期→ブランド長期） ----
cards.append(make_card(
    "1",
    """サムスンのケースが示す「ブランドを軸とした転換」の核は何か。要点を述べよ。""",
    """<b>旗を立てる — OEM（短期目線）からブランド（長期経営）への転換</b>
<ul>
<li><b>出発点</b>：'80s <span class="important">OEM</span>（白黒TV）→低コスト・大量生産。OEM評価＝<b>短期目線</b>、ブランドの知名度・意識もうすい（ロゴがバラバラ）、「良い商品をつくれば売れる」＝売り込み型MKG。</li>
<li><b>転換</b>：'93 <span class="important">新経営方針</span>（アジア通貨危機・会長の路線発表）「<b>良いブランドで売る</b>」→ リストラ／選択統合・カスタマイズ／国際化／高付加価値化（B2Cへ）。</li>
<li>半導体への長期投資（'98–'03）＝<b>長期目線</b> → 株価↑。軸の転換：<span class="important">OEM＝短期 ⇔ ブランド＝長期</span>。</li>
</ul>
<div class="example">
<b>学び①〔自分の視点〕：</b>まず「グローバルリーダーになる」という<b>旗を立てる</b>（目標はソニー）。<span class="important">旗が先、変革が後</span> — 会長の宣言が一貫性の起点となり、転換を駆動した。
</div>"""
))

# ---- カード2: M-Net＝市場ドリブンを"測る"仕組み（顧客の感情＞売上） ----
cards.append(make_card(
    "2",
    """サムスンが市場ドリブンを実装した中核の仕組み「M-Net」とは何か。なぜ「顧客の感情 ＞ 売上」と言えるか。（資料5を含めて）""",
    """<b>M-Net — 市場ドリブンを"測る"仕組み</b>
<ul>
<li><b>体制</b>：<span class="important">市場ドリブン</span>へシフト（長期・ブランド・B2C）、投資を本部が管理、ブランド実態＝<b>調査</b>、教育で意識改革（'99–'03）、共通ガイドライン。</li>
<li><b>M-Net＝各市場の潜在的利益を計算するツール</b>（HBR "Optimal Marketing" 2003）。</li>
<li><b>資料5（バブル図）</b>：横軸＝<b>現在の配分（計画）</b>／縦軸＝<b>M-Netの理想配分の提言</b>／円の大きさ＝<span class="important">顧客の潜在的利益</span>。例：イタリアは計画<b>15%</b>→提言<b>22%</b>。<b>点線より上＝もっと配分すべき／下＝削減すべき</b>。</li>
<li><b>効果</b>：<span class="important">配分ミスを突きとめ</span>、影響を受けるマネジャーに変更を受け入れさせる<b>説得材料</b>になった。</li>
</ul>
<div class="example">
<b>学び②〔自分の視点〕：</b>売り込み（Sales）型を脱し、<b>顧客の感情・心のキョリ</b>（誰にどう思われたいか＝認知／内心／質）を売上より上位に置く。さらに<span class="important">感情と分析をスケール化（測れる形に）して、潜在市場（hidden market）を算出</span>する＝M-Netで「どこに張るか」に翻訳する。
</div>"""
))

# ---- カード3: 標準化と適応化（講義の枠組み）＋ DigitAll ----
cards.append(make_card(
    "3",
    """サムスンに見る「標準化と適応化」の正しい捉え方を、講義の枠組みで述べよ。""",
    """<b>標準化と適応化（Standardization &amp; Adaptation）</b>
<ul>
<li><b>行動の種類で標準化/適応化を分けない</b>〔PDF p.13〕。主体は<span class="important">「整合性・一貫性」＝ストーリー性</span>。標準化/適応化は<b>表現方法に過ぎない</b>。</li>
<li>軸は「<b>戦略・メッセージ・媒体</b>」で考える／「<b>戦略と手段を間違えない</b>」〔PDF p.12〕。</li>
<li>「何を変え、何を変えないか」に<b>意図</b>を持つ。</li>
<li><b>DigitAll CP（'02）</b>＝デジタル融合の象徴「みんな」と「すべて」／「先端」と「親しみやすさ」の両立＝ブランド統一の表現。</li>
</ul>
<div class="example">
市場起点なら<b>スペックでなくベネフィット</b>が基本、重要なのは「<b>違い</b>」であって程度ではない（D&amp;B・刺身理論）。＝ <span class="important">ダイソンと同節の学び</span>（異質市場の理解）。
</div>"""
))


for q, a in cards:
    my_deck.add_note(genanki.Note(model=my_model, fields=[q, a]))

OUT = '/Users/sasaki/02_Personal/anki/anki/scripts/mba/mc/samsung/mba_mc_samsung_verified.apkg'
genanki.Package(my_deck).write_to_file(OUT)
print(f'OK: {len(cards)} cards -> {OUT}')
