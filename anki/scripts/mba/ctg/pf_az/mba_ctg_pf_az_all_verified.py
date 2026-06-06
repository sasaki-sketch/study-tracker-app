"""
Changing the GAME - プラットフォーム競争戦略キーワード解説A-Z (全26キーワード)
出典: 加藤和彦『プラットフォーム競争戦略キーワード解説A-Z』(Changing The GAME / Driving DX 講義資料, 2022-9-20)
"""
import genanki
import sys
sys.path.insert(0, '/Users/sasaki/02_Personal/anki')
from anki_card_css_template import CARD_CSS

MODEL_ID = 1704140100
DECK_ID = 2704140100

SOURCE = '加藤和彦『プラットフォーム競争戦略キーワード解説A-Z』(Changing The GAME 講義資料, 2022-9-20)'

my_model = genanki.Model(
    MODEL_ID,
    'NUCB_EMBA CTG PF A-Z',
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
    'NUCB_EMBA::Changing_the_Game::プラットフォーム競争戦略キーワード解説A-Z'
)


def make_card(letter, topic_jp, topic_en, stars, body_html):
    """カードのQ/Aを生成"""
    q = f"""<div style="font-size:14px; color:#888; margin-bottom:8px;">
PF戦略A-Z / {letter} / 重要度 {stars}
</div>
<b>{letter}: {topic_jp}</b><br>
（{topic_en}）の定義・本質・具体例を答えよ"""

    a = f"""<b>{topic_en}</b>（{topic_jp}）　{stars}

{body_html}

<div class="source">
出典: {SOURCE}
</div>"""
    return q, a


# ==================== 26 cards ====================
cards = []

# A: プラットフォーム競争戦略 ★★★★★
cards.append(make_card(
    "A", "プラットフォーム競争戦略", "Platform Competition Strategy", "★★★★★",
    """<ul>
<li><b>定義:</b> プラットフォーム製品を中心としたエコシステムを成長させるため、プラットフォーム提供者（主に企業）がとる戦略</li>
<li><b>本質:</b> 補完製品（サービス）の提供が促される施策を行い、補完製品の多様性を生み出すことで、ユーザーのプラットフォーム選択を促進し市場普及を図る</li>
<li><b>好循環:</b> OS（PF）でシェア獲得 → 補完製品（アプリ）増加 → ユーザー増 → さらなるPF普及</li>
</ul>

<div class="example">
<b>プラットフォームの定義（本書）</b><br>
各種の補完製品・サービスや補完コンテンツとあわさって顧客の求める機能を実現する基盤になり、プレイヤーグループ間の意識的相互作用の場となる製品やサービス。
</div>

<b>具体例:</b> OS/アプリ、SNS、検索エンジン、オークション、クレジットカード、ショッピングセンター、シェアリングエコノミー

<b class="important">注意:</b> パイプライン型（ポーターの戦略論）とは相対する戦略モデル"""
))

# B: デファクト・スタンダード競争 ★★★
cards.append(make_card(
    "B", "デファクト・スタンダード競争", "De Facto Standard Competition", "★★★",
    """<ul>
<li><b>De Facto = 「事実上の」</b>（ラテン語）</li>
<li><b>定義:</b> 公的な標準化機関からの認証ではなく、<span class="important">市場競争によって業界標準と認められた規格</span></li>
<li><b>例:</b> 検索エンジンのGoogle、OSのWindows、日本の無料通信アプリLINE、USB端子、QWERTY配列、DVD規格</li>
</ul>

<b>戦略的意義:</b> 新しい市場の創成期にPF提供者がデファクトスタンダードを獲得すると、ユーザーの製品選択の必然性を高め、PF提供者に大きな恩恵をもたらす。そのため獲得競争が激化する。

<div class="example">
<b>反対概念: デジュールスタンダード（De Jure Standard）</b><br>
ISO（国際標準化機構）等の公的機関が認証する規格。<br>
例: JIS（日本産業規格）、ISO規格。<br>
※ De Jure = ラテン語「法の」
</div>"""
))

# C: クリティカルマス ★★★
cards.append(make_card(
    "C", "クリティカルマス", "Critical Mass", "★★★",
    """<ul>
<li><b>定義:</b> <span class="important">商品・サービスの市場普及が加速度的に増加する分岐点となる普及率</span></li>
<li><b>提唱者:</b> Everett Rogers（スタンフォード大）『Diffusion of Innovations』(1962)</li>
<li>クリティカルマスを超えると、それまでの普及率の伸びが一気に跳ね上がる</li>
</ul>

<b>普及の順序（ロジャース）:</b>
<ul>
<li>イノベーター（革新者）</li>
<li>アーリーアダプター（初期採用者）</li>
<li>マジョリティ（多数者）</li>
</ul>

<div class="example">
<b>PF戦略上の意義</b><br>
チキンエッグ問題を乗り越えても市場で存続できるとは限らない。他PFとの競争があるため、<b>クリティカルマスを超えられるか</b>が市場での普及の分かれ目となる。
</div>

<b>失敗例:</b> LD（レーザーディスク）、MD（ミニディスク）はクリティカルマスを超えられず消えた。"""
))

# D: パイプラインからプラットフォームへ ★★★
cards.append(make_card(
    "D", "パイプラインからプラットフォームへ", "From Pipeline to Platform", "★★★",
    """<ul>
<li><b>パイプラインビジネス:</b> <span class="important">片側に生産者、もう一方に消費者がいる一方通行のビジネス</span>。価値は段階的に左→右に移転し消費者に届く。各工程の入口・出口にゲートキーパーがいる</li>
<li><b>プラットフォーム:</b> <span class="important">生産者と消費者のインタラクションによって価値が創造されるビジネス</span>。ゲートキーパーは存在せず、PF提供者がマッチングルールを整備しガバナンスを担う</li>
</ul>

<div class="example">
<b>戦略モデルとしての対立</b><br>
パイプラインとプラットフォームは相対する概念。プラットフォームは、これまで主流だった<b>ポーターの戦略論とはまったく異なる戦略モデル</b>と言える。
</div>

<b class="important">市場の現実:</b> 既存のパイプライン型企業が、新興のプラットフォームによって自社の力を弱められたり、ディスラプト（崩壊）させられたりしている。"""
))

# E: ネットワーク効果 ★★★★★
cards.append(make_card(
    "E", "ネットワーク効果", "Network Effect", "★★★★★",
    """<ul>
<li><b>定義:</b> <span class="important">より多くの顧客が製品・サービスを利用するにつれて、その製品・サービスを利用する顧客の便益が増加（もしくは減少）する効果</span></li>
<li>製品・サービスの価値が既存顧客数に依存する</li>
</ul>

<b>ネットワーク効果の分類:</b>
<table>
<tr><th>軸</th><th>分類</th><th>説明</th></tr>
<tr><td rowspan="2">方向</td><td>正（ポジティブ）</td><td>便益が増加</td></tr>
<tr><td>負（ネガティブ）</td><td>便益が減少（例: 輻輳、渋滞）</td></tr>
<tr><td rowspan="2">経路</td><td>直接（direct）</td><td>電話・FAXのような直接接続</td></tr>
<tr><td>間接（indirect）</td><td>補完関係の製品同士</td></tr>
<tr><td rowspan="2">ツーサイドPF</td><td>グループ内（same-side）</td><td>同じユーザーグループ内</td></tr>
<tr><td>グループ間（cross-side）</td><td>2つのユーザーグループ間</td></tr>
</table>"""
))

# F: 補完製品 ★★
cards.append(make_card(
    "F", "補完製品", "Complementary Products", "★★",
    """<ul>
<li><b>定義:</b> <span class="important">ある製品・サービスと互いに補完し合うことで、ユーザーの効用が満たされたり高まったりする製品</span></li>
<li><b>例:</b> ゲームソフトとゲーム機本体、DVDとDVDレコーダー、スマホと専用ケース</li>
</ul>

<b>PF戦略上の重要性:</b> 補完製品は戦略の成否を左右する重要要素。補完製品の売上を伸ばすことで、自らのPF製品の売上も伸ばせる。

<div class="example">
<b>補完 vs 競合</b><br>
<b>補完関係</b>（製品A ↔ 製品B）: Aの売上↑ → Bの売上↑<br>
<b>競合関係</b>（製品B ↔ 製品C）: Bの売上↑ → Cの売上↓
</div>"""
))

# G: エコシステム ★★★★
cards.append(make_card(
    "G", "エコシステム", "Ecosystem", "★★★★",
    """<ul>
<li><b>本来の意味:</b> 自然界の「生態系」を表す科学用語</li>
<li><b>ビジネスでの意味:</b> <span class="important">「産業生態系」</span>として用いられる</li>
<li><b>PF戦略における定義:</b> コアとなるプラットフォーム提供者とその補完業者、ユーザーが結びつき、共に成長していく1つのシステム</li>
</ul>

<b>例:</b> スマホOS（iOS / Android）の上で動くアプリ開発者、ハードウェア提供者、関連補完品の提供業者の結びつきで1つのシステムが形成される。

<div class="example">
<b>エコシステム形成の要諦</b><br>
<b>プラットフォーム提供者が自社だけでなく、自社をとりまく様々な補完業者との協業体制を構築し、互いの力を生かして全体の利益を考えながら製品・サービスを普及・発展させていくこと</b>が大切。競争しつつ協業し合う産業として生態系を成す。
</div>"""
))

# H: ツーサイド・プラットフォーム理論 ★★★★★
cards.append(make_card(
    "H", "ツーサイド・プラットフォーム理論", "Two-Sided Platform Theory", "★★★★★",
    """<ul>
<li><b>定義:</b> <span class="important">異なる二種類のユーザーグループが存在し、ある共通の取引基盤を提供し、ユーザーグループに参加資格を与える仲介業者のような役割</span></li>
<li><b>理論体系化:</b> Eisenmann, Parker & Alstyne (2006)</li>
<li><b>例:</b> メルカリ（フリマ）、Uber、Airbnb</li>
</ul>

<b>一面市場 vs 二面市場:</b>
<table>
<tr><th>観点</th><th>一面市場</th><th>ツーサイドPF</th></tr>
<tr><td>モデル</td><td>仕入れて売る</td><td>2グループを仲介</td></tr>
<tr><td>規模の経済</td><td>収穫逓減</td><td>収穫逓増（NW効果）</td></tr>
</table>

<b>ネットワーク効果（2種類）:</b>
<ul>
<li><b>グループ内NW効果（same-side）:</b> ユーザーグループ内で発生</li>
<li><b>グループ間NW効果（cross-side）:</b> 2グループを跨いで発生</li>
</ul>

<div class="example">
<b>戦略的課題</b><br>
チキンエッグ問題を解消するため、各ユーザーグループに<b>優遇される側 / 課金される側</b>などのNW効果促進策が求められる。短期間で市場普及を図り、クリティカルマスを確保することが重要課題。
</div>"""
))

# I: チキン・エッグ問題 ★★★
cards.append(make_card(
    "I", "チキン・エッグ問題", "Chicken and Egg Problem", "★★★",
    """<ul>
<li><b>定義:</b> 「鶏が先か卵が先か」問題。<span class="important">PF創業期において、PF製品のユーザーが少ないため補完業者から見たPF価値が低く、補完製品が少ないためユーザーから見たPF価値も低いという状況</span></li>
<li>PF提供者が成長のために必ず越えなければならない経営課題の1つ</li>
</ul>

<div class="example">
<b>打開策: 優遇される側 / 課金される側</b><br>
2つのユーザーグループに対し、<b>片方の参加料を無料にする等で優遇</b>し、ユーザーを集めやすくする。もう一方（課金される側）には上乗せ料金を課金。優遇側にユーザーが多く集まることで、サイド間NW効果により課金側にもユーザーが集まる仕組み。
</div>"""
))

# J: プラットフォーム包囲 ★★★★
cards.append(make_card(
    "J", "プラットフォーム包囲", "Platform Envelopment", "★★★★",
    """<ul>
<li><b>文献:</b> Eisenmann, Parker & Alstyne (2007)。Eisenmann et al. (2006)の3課題（プライシング / 1人勝ちの力学 / 包囲の危機）の3番目を独立発展</li>
<li><b>定義:</b> <span class="important">PF提供者が、PF製品のコンポーネントの共通部分と重なり合うユーザー関係をテコ（leverage）にして、自分自身の機能にターゲットPFの機能をバンドルの状態で結合させ、ターゲットPFの市場に入っていく戦略</span></li>
</ul>

<div class="example">
<b>戦略的意義</b><br>
飛躍的イノベーションやシュンペーターの創造的破壊を<b>必要としない</b>PFリーダーシップ交代のメカニズム。強いNW効果と高いスイッチングコストで参入から隔離されている支配的企業も、隣接PFの複数階層を結合する包囲攻撃には脆弱な場合がある。
</div>

<b>有名事例:</b> PC上のリアルネットワークスに対する、マイクロソフトのWindowsによる包囲"""
))

# K: 情報の非対称性 ★★
cards.append(make_card(
    "K", "情報の非対称性", "Information Asymmetry", "★★",
    """<ul>
<li><b>定義:</b> <span class="important">売り手と買い手のどちらかが、一方よりも少ない情報しか持っていないこと</span></li>
<li><b>典型例:</b> 中古車市場。売り手は過去のエンジントラブル等を知るが、買い手は知ることができない</li>
</ul>

<div class="example">
<b>レモン市場</b><br>
購入後にはじめて品質や本当の価値がわかる商品が取引される市場。<b>レモン</b>は中古車を表すスラングで、厚い皮に覆われ外から鮮度・品質の判断が難しいことに由来。
</div>

<b>緩和する仕組み:</b>
<ul>
<li>第三者による品質鑑定・修理保証（例: トヨタのT-Value、ヤナセ認定中古車）</li>
<li>オークション/eコマースの相互レビューシステム</li>
</ul>"""
))

# L: マルチホーミング ★★★
cards.append(make_card(
    "L", "マルチホーミング", "Multi-homing", "★★★",
    """<ul>
<li><b>定義:</b> <span class="important">ユーザーが同じ目的のために異なるプラットフォームを同時に使用すること</span></li>
<li><b>マルチホーミングコスト:</b> 金銭以外にも、時間・労力なども含む</li>
</ul>

<div class="example">
<b>アナロジー</b><br>
家（Home）= プラットフォーム。利用する家の数が増えればユーザーの総コストは増える。一方で複数のサークルに加入すれば多くの出会いが得られるようにメリットもある。
</div>

<b>ドミナント化との関係:</b>
<ul>
<li>マルチホーミングコストが<b>低い</b> → マルチホーミングしやすい → PFの1社独占は起きにくい</li>
<li>マルチホーミングコストが<b>高い</b> → <span class="important">1社が市場を独占する傾向が強くなる</span></li>
</ul>

PF提供者にとって、ユーザーのマルチホーミングをいかに防げるかがドミナント化の鍵。"""
))

# M: プラットフォームの収斂（コンバージェンス）★★
cards.append(make_card(
    "M", "プラットフォームの収斂（コンバージェンス）", "Platform Convergence", "★★",
    """<ul>
<li><b>定義:</b> 複数のPFが1つのPFに統合されることで、多くのコンテンツやサービスの提供が可能になるプロセス</li>
<li><b>条件:</b> <span class="important">マルチホーミングコストが高い場合、かつプラットフォーム包囲が市場で繰り返される場合、PFは収斂（コンバージェンス）していく傾向が強い</span></li>
</ul>

<b>具体例:</b>
<ul>
<li>GAFA、中国のBATH、日本の楽天が様々な分野に進出</li>
<li>Uber → Uber Eats（2014年、米サンフランシスコ発、2016年日本開始）へ拡張</li>
</ul>

<div class="example">
<b>山田 (2000) の指摘</b><br>
「全部繋げるときは、一つしか残らないメカニズムが働き収斂する」
</div>"""
))

# N: オープンとクローズド ★★★
cards.append(make_card(
    "N", "オープンとクローズド", "Open and Closed", "★★★",
    """<ul>
<li><b>オープン戦略:</b> 手伝ってくれる仲間の補完業者が多ければ、急速な普及を図れる</li>
<li><b>クローズド戦略:</b> 利益を独り占めしやすい</li>
<li>PF製品では階層単位でインターフェイスをオープン / クローズドにする意思決定が可能であり、その決定こそが戦略の成否を分ける</li>
</ul>

<div class="example">
<b>ハイブリッド設計</b><br>
どこかの階層を<b>オープン</b>（多くの企業にインターフェイス公開し製品を作ってもらえる状態）、どこかの階層を<b>クローズド</b>（一社または限られた少数の企業のみで提供される状態）にする。<br>
隣接する階層では多くの参加者を集めるためオープンにするが、全階層オープンだと収益確保が難しいため、一部はクローズドで収益を生む構造にする。
</div>

<b>クローズド = プロプライエタリ（Proprietary）</b>"""
))

# O: プラットフォーム化（階層化）★★★
cards.append(make_card(
    "O", "プラットフォーム化（階層化）", "Platformization / Layering", "★★★",
    """<ul>
<li><b>定義:</b> <span class="important">クローズドだった階層が上位層または下位層に向けてインターフェイスを公開しオープンにすることで、PF上で活躍するプレーヤーを集められるようになる</span></li>
<li>これにより階層が一階層増えて、プラットフォーム化（複数階層化）する</li>
</ul>

<b>メカニズム:</b> 階層をオープンにする → 補完業者が自社PF上（または下）で活躍できる環境を提供 → 多くの補完業者が集まり活躍 → 隣接するPFが繁栄できる状況が生まれる

<b>事例:</b> Facebookによる「Facebook Platform」の提供"""
))

# P: 階層介入戦略 ★★★★
cards.append(make_card(
    "P", "階層介入戦略", "Layer Intervention Strategy", "★★★★",
    """<b>階層介入の特徴:</b>
<ul>
<li>階層数が増える</li>
<li>それまで階層がなかった所（隣接）に新しく階層ができる</li>
<li><b>介在なので、最初からあったのではなく後から介在（後発）してくる</b></li>
</ul>

<div class="example">
<b>具体例: 製品のIoT化</b><br>
これまで階層が存在しなかったところに新たな階層が介在することで、<b>新たな競争環境</b>が生じる。IoTを含むインターネットプロトコルの階層によってネットワークが可能となる階層が介入する場合、製品の価値が介入前に比べて大きく変わることが予想できる。
</div>

<b class="important">プラットフォーム化（階層化）との違い:</b>
<ul>
<li><b>プラットフォーム化:</b> 共通PFが先にあり、後発として補完業者を募る</li>
<li><b>階層介入:</b> 先発の複数の補完業者を、後発のPFが隣接する状態</li>
</ul>"""
))

# Q: IoTの階層介入による相互接続 ★★
cards.append(make_card(
    "Q", "IoTの階層介入による相互接続", "IoT Layer Intervention", "★★",
    """<ul>
<li><b>IoT:</b> Internet of Things（モノのインターネット）。<span class="important">あらゆるモノがインターネットに接続する可能性をもつ状態</span></li>
<li>世の中のモノに通信機能を持たせ、インターネット経由で相互通信することで、これまで困難だったことが実現容易になる</li>
</ul>

<b>用途例:</b>
<ul>
<li>モノに取り付けられたセンサーが人手を介さずデータ収集</li>
<li>自動認識、自動制御、遠隔計測</li>
<li>機器監視、スマートアグリ、ヘルスケア</li>
</ul>

<div class="example">
<b>戦略的含意</b><br>
今後、<b>製造業を含む全ての業種で、IoTによる階層介入が生じる</b>。近年、DX（デジタル・トランスフォーメーション）は、IoTの活用と連携したものが多く生まれると考えられる。
</div>"""
))

# R: ドミナント ★★★★
cards.append(make_card(
    "R", "ドミナント", "Dominant", "★★★★",
    """<ul>
<li><b>語義:</b> 「支配的な」「優勢な」「優位に立った」</li>
<li><b>ドミナント・プラットフォーム製品の定義:</b> PF提供者と補完業者によって形成されるエコシステム内で、<span class="important">高いシェア（目安としては70%以上）</span>を有し、稼働台数で他に大きな差をつけ、強い市場支配力をもつ、階層毎に存在し得る1つのPF製品</li>
</ul>

<b>ドミナントPFの力:</b>
<ul>
<li>他階層への支配力</li>
<li>価格コントロール力</li>
<li>業界団体・業界標準化プロセスでの発言力</li>
<li>販売チャネルへの影響力</li>
</ul>

<div class="example">
<b>ドミナント化とマルチホーミングの関係</b><br>
ユーザーのマルチホーミングが少ない → PFはドミナント化しやすい。<br>
PF提供者にとって、<b>ユーザーのマルチホーミングをいかに防げるかがドミナント化の課題</b>となる。
</div>"""
))

# S: ドミナント化とコモディティ化 ★★★
cards.append(make_card(
    "S", "ドミナント化とコモディティ化", "Dominance and Commoditization", "★★★",
    """<ul>
<li><b>原則:</b> PFの隣接階層において、ドミナント化とコモディティ化は<span class="important">表裏一体の関係</span></li>
<li>ある階層でドミナント化が進行すると、上下の隣接階層ではコモディティ化が進行しやすくなる</li>
</ul>

<div class="example">
<b>メカニズム: Only one → One of them</b><br>
ユーザーがPFを選んでくれる「選択の必然性を発生させるクローズドな状況（= Only one状態）」が、補完製品によって「多くの中のひとつの選択肢（= One of them状態）」にさせられてしまうリスクが生じる。<br>
同一階層上の補完製品同士は競争し合い、マージンを減らし、類似機能を持ち、コモディティ化が進行する。
</div>

<b>事例（2010年4月）:</b> Apple社が自社モバイル端末で米AdobeのFlashを採用しなかった理由 → iTunes+iOS+内製デバイスの抱き合わせで目論むドミナントの地位を、補完製品であるFlash playerに奪われ、iPhoneがコモディティ化してしまうリスクをジョブズは避けたかった"""
))

# T: API ★★
cards.append(make_card(
    "T", "API", "Application Programming Interface", "★★",
    """<ul>
<li><b>定義:</b> <span class="important">APIを使用することで、他の製品・サービスの実装方法を知らなくても、利用中の製品・サービスをそれらと通信することが可能になる</span></li>
<li>APIは、インターフェイスをオープンにする際の手段の1つ</li>
</ul>

<div class="example">
<b>戦略的意義</b><br>
APIの使用により、補完業者である開発者が新しいアプリケーション・コンポーネントを<b>既存のアーキテクチャに統合する方法が単純化</b>される。PF提供者と補完業者間のコミュニケーションが迅速・円滑になり、<b>エコシステムの形成が容易</b>になる。
</div>

<b>例:</b> Twitter API、Windows API、YouTube API、Google Maps API、LINE Messaging API

<b>関連用語:</b> クローリングとスクレイピング"""
))

# U: シェアリングエコノミー ★★★★★
cards.append(make_card(
    "U", "シェアリングエコノミー", "Sharing Economy", "★★★★★",
    """<ul>
<li><b>定義:</b> <span class="important">個人や企業が持つモノ・場所・スキルなどの有形・無形資産を、インターネット上のプラットフォームを介して取引する新しいビジネス形態</span></li>
<li>別名: 共有経済</li>
</ul>

<b>構造:</b>
<ul>
<li>貸主: 遊休資産の活用による収入</li>
<li>借主: 所有することなく利用できる</li>
<li>PF: 円滑な情報交換・信頼関係構築・コミュニティ機能を提供</li>
</ul>

<div class="example">
<b>5つの領域（一般社団法人シェアリングエコノミー協会）</b>
<ol>
<li>空間（Space）</li>
<li>スキル（Skill）</li>
<li>移動（Mobility）</li>
<li>お金（Money）</li>
<li>モノ（Goods）</li>
</ol>
</div>"""
))

# V: 相互評価システム ★★★
cards.append(make_card(
    "V", "相互評価システム", "Mutual Rating System", "★★★",
    """<ul>
<li><b>対象:</b> シェアリングエコノミー、フリマ、各種マッチングサービス</li>
<li><b>定義:</b> <span class="important">売り手と買い手がお互いを評価するシステム</span></li>
</ul>

<b>目的:</b>
<ul>
<li>レビューにより潜在顧客の購入を後押し</li>
<li>商品・サービスの品質改善・向上</li>
<li>悪質なユーザーの排除</li>
</ul>

<div class="example">
<b>公正評価の工夫: 同時公開</b><br>
公正な評価を相互に促すため、<b>お互いの評価が出揃ってから公開</b>する仕組みをとることが多い（相手の評価内容を理由にリベンジ評価することを避けるため）。
</div>

<b>行動変容効果:</b> 例えばAirbnbでは、ゲストが部屋を荒らせばその人に悪い評価が付き、サービス利用できなくなる。ホスト・ゲスト双方が評価を気にして行動する。

<b>情報非対称性の緩和:</b> オークション/eコマースサイトの相互レビューも同じ機能を持つ。"""
))

# W: フィードバック効果 ★★
cards.append(make_card(
    "W", "フィードバック効果", "Feedback Effect", "★★",
    """<ul>
<li><b>定義:</b> ネットワーク効果が働く環境において、<span class="important">集積するデータをPFの「改善」に利用する点に着目した効果</span></li>
<li><b>フィードバックの本質:</b> 原因と結果の関係において、結果を原因側に知らせることにより、正の好循環を生み出すこと</li>
</ul>

<b>具体例:</b> 旅行サイトで予約宿泊した人が、宿泊先での満足度・改善点を口コミとして掲載 → ホテル側が評価に基づき改善 → 満足度向上

<div class="example">
<b>Mayer et al. (2019) の指摘</b><br>
フィードバック効果は<b>市場の集中化に拍車</b>をかける。最も人気の製品・サービスは多くのデータが得られるため改善率も高くなる。<b>イノベーションとは、画期的なアイデアではなく、いかに多くのフィードバック・データを集めるかにかかっている</b>。
</div>"""
))

# X: デジタル・ディスラプター ★★★★★
cards.append(make_card(
    "X", "デジタル・ディスラプター", "Digital Disruptor", "★★★★★",
    """<ul>
<li><b>定義:</b> <span class="important">クラウド・ビッグデータ・IoT・AI等のデジタルテクノロジーを活用し、既存の業界秩序やビジネスモデルを破壊するプレイヤー（主に新興のベンチャー企業）</span></li>
<li>ディスラプター = 「破壊する者」。デジタル技術を駆使して急成長し、既存の枠組み・伝統にとらわれない柔軟なビジネスモデルで市場参入、驚くべきスピードで業界シェアを奪う</li>
</ul>

<b>代表事例:</b>
<ul>
<li><b>Uber:</b> タクシー業界の利用形態を変革</li>
<li><b>Airbnb:</b> 民泊の概念を広めた</li>
<li><b>Spotify:</b> 音楽ストリーミングで聴き方を変えた</li>
</ul>

<div class="example">
<b>既存企業の対抗策</b><br>
自社ビジネスを守るため、自らの事業に<b>デジタルテクノロジーを取り込み、新たな価値を創造するDX（デジタル・トランスフォーメーション）を推進</b>することが重要。
</div>"""
))

# Y: MaaS ★★★
cards.append(make_card(
    "Y", "MaaS", "Mobility as a Service", "★★★",
    """<ul>
<li><b>定義:</b> <span class="important">バス・電車・タクシーからライドシェア・シェアサイクルといったあらゆる公共交通機関を、ITを用いてシームレスに結びつけ、人々が効率よく便利に使えるようにするシステム</span></li>
<li><b>読み:</b> マース</li>
</ul>

<b>先進国: フィンランド</b>
<ul>
<li>鉄道・道路・輸送の法規制を一元化</li>
<li>位置・遅延・運賃・運行情報をオープンデータ化</li>
<li>予約・販売・決済の一元化</li>
<li>MaaS Global社のアプリ「Whim」をヘルシンキで実施（レベル3相当）</li>
</ul>

<div class="example">
<b>Sochor et al. (2017) 普及レベル</b>
<table>
<tr><th>レベル</th><th>段階</th><th>内容</th></tr>
<tr><td>4</td><td>政策の統合</td><td>都市計画・インフラ政策が一体</td></tr>
<tr><td>3</td><td>サービス提供の統合</td><td>定額制等の一元化パッケージ</td></tr>
<tr><td>2</td><td>予約/決済の統合</td><td>アプリで一括予約・発券・決済</td></tr>
<tr><td>1</td><td>情報の統合</td><td>利用料金・経路情報の一元表示</td></tr>
<tr><td>0</td><td>統合なし</td><td>交通手段が独立・分離</td></tr>
</table>
</div>"""
))

# Z: 都市OS ★★★
cards.append(make_card(
    "Z", "都市OS", "City OS / Urban OS", "★★★",
    """<ul>
<li><b>定義:</b> スーパーシティによって物流・医療・福祉・防災など様々な新サービスを提供するための基盤</li>
<li><b>本質:</b> <span class="important">都市に存在する膨大なデータを蓄積・分析するとともに、他の自治体・企業・研究機関などと連携するためのプラットフォーム</span></li>
<li>都市OSをコンピュータのOSに置き換えて考えるとわかりやすい</li>
</ul>

<div class="example">
<b>事例1: サイドウォークラボ（アルファベット傘下）</b><br>
2017年、トロントの再開発プロジェクトとしてスマートシティ計画を発表。都市を<b>インフラ・公共・モビリティ・建物の4層のリアルレイヤー</b>と、それらを情報で繋ぐ<b>デジタルレイヤーの1層</b>からなる<b>5層構造</b>としてPFと捉えた（実現せず）。
</div>

<div class="example">
<b>事例2: トヨタ Woven City</b><br>
2020年1月、米CESで発表。2021年着工。都市を平面的なものから<b>立体的な階層構造</b>へと捉え方を変化させ、<b>都市を1つのプラットフォームと捉える</b>。
</div>"""
))

# =================== assemble deck ====================
assert len(cards) == 26, f"Expected 26 cards, got {len(cards)}"

for q_html, a_html in cards:
    note = genanki.Note(model=my_model, fields=[q_html, a_html])
    my_deck.add_note(note)

output_path = '/Users/sasaki/02_Personal/anki/anki/scripts/mba/ctg/pf_az/mba_ctg_pf_az_all_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
print(f"Total cards: {len(cards)}")
