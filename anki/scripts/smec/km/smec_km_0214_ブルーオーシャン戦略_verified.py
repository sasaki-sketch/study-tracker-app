"""
Ankiカード: ブルーオーシャン戦略（アオウミ海賊）
科目: 中小企業診断士_企業経営理論
セクション: 02_競争戦略
作成日: 2026-04-23
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki/02_Personal/anki')
from anki_card_css_template import CARD_CSS

model_id = 1702140001
deck_id = 1702140002

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_ブルーオーシャン戦略',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '<div class="question">{{Question}}</div>',
            'afmt': '{{FrontSide}}<hr id="answer"><div class="answer">{{Answer}}</div>',
        },
    ],
    css=CARD_CSS
)

my_deck = genanki.Deck(
    deck_id,
    '中小企業診断士_企業経営理論::02_競争戦略::ブルーオーシャン戦略'
)

question = '''<span class="important">アオウミ海賊</span>の戦い方＝<b>ブルーオーシャン戦略</b>。<br><br>・<b>提唱者・発表年・所属機関</b>は？<br>・レッドオーシャンとの違いは？<br>・<b>4つのアクション（ERRC）</b>とは？<br>・<b>戦略キャンバス／価値曲線</b>の役割は？<br>・代表例は？'''

answer = '''<b>Blue Ocean Strategy</b>（ブルーオーシャン戦略）

<div class="formula">
<b>■ 提唱</b><br>
<b>W. Chan Kim</b> × <b>Renée Mauborgne</b><br>
<b>INSEAD</b>（フランスのビジネススクール）教授<br>
『<b>Blue Ocean Strategy</b>』<b>2005年</b>出版<br>
（新版: 2015年。日本語訳: ダイヤモンド社）
</div>

<div class="formula">
<b>■ Red vs Blue</b>
<table>
<tr><th></th><th>レッドオーシャン（赤い海）</th><th>ブルーオーシャン（青い海）</th></tr>
<tr><td>市場</td><td>既存・血で染まった市場</td><td><b>新市場を創造</b></td></tr>
<tr><td>競争</td><td>限られた需要の奪い合い</td><td><b>競争自体を無意味化</b></td></tr>
<tr><td>戦略</td><td>コスト or 差別化の二者択一</td><td><b>低コスト＋差別化を両立</b></td></tr>
<tr><td>結果</td><td>疲弊・価格競争</td><td>バリュー・イノベーション</td></tr>
</table>
</div>

<div class="example">
<b>■ 4つのアクション（ERRC フレームワーク）</b><br>
業界の常識に対して4つの問いを立てる:<br><br>
<b>E</b>liminate（<b>取り除く</b>）: 業界で当たり前だが本当は不要なもの<br>
<b>R</b>educe（<b>減らす</b>）: 業界標準より思い切り減らすもの<br>
<b>R</b>aise（<b>増やす</b>）: 業界標準より大胆に増やすもの<br>
<b>C</b>reate（<b>付け加える</b>）: 業界で誰も提供していないもの<br><br>
→ <b>E・R で低コスト、R・C で差別化</b>を同時達成
</div>

<div class="example">
<b>■ 戦略キャンバス／価値曲線</b><br>
横軸: 業界の競争要因<br>
縦軸: 各要因への投資レベル<br>
→ 既存プレイヤーと<b>全く異なる価値曲線</b>を描けば青い海<br>
→ 曲線が似ていれば赤い海
</div>

<div class="example">
<b>■ 代表例（ERRC付き）</b><br>
<b>任天堂 Wii</b>: ハイスペ競争をやめ、家族・高齢者層に拡大<br>
　E: 高画質／R: ボタン数／R: 直感操作／C: モーション操作<br><br>
<b>Cirque du Soleil</b>: サーカス + アートで新カテゴリ<br>
　E: 動物・ストーリー軽視／R: 規模／R: 芸術性／C: テーマ性<br><br>
<b>QB ハウス</b>: 1000円・10分カット<br>
　E: シャンプー・予約／R: 会話／R: 回転率／C: エアウォッシャー
</div>

<div class="example">
<b>■ シーン再生フック（フロンティア山）</b><br>
<b>アオウミ海賊</b>が、誰も行かない<b>青い谷</b>に独自の新カテゴリを発明。<br>
競争のない楽園で、海賊旗を掲げた<b>独立王国</b>を築く。
</div>

<div class="source">出典: W. Chan Kim &amp; Renée Mauborgne『ブルー・オーシャン戦略』（ダイヤモンド社、原著2005年・新版2015年）; DIAMOND Harvard Business Review 関連記事</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

output_path = '/Users/sasaki/02_Personal/anki/anki/scripts/smec/km/smec_km_0214_ブルーオーシャン戦略_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
