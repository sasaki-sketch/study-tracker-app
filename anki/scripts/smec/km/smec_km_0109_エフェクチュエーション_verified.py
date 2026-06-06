"""
Ankiカード: エフェクチュエーションの定義と5つの原則
科目: 中小企業診断士_企業経営理論
セクション: 01 経営戦略（ドメイン・全社戦略）
作成日: 2026-03-13
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# --- モデル定義 ---
MODEL_ID = 1710390109
DECK_ID = 1610390109

model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_企業経営理論_エフェクチュエーション',
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

# --- デッキ定義 ---
deck = genanki.Deck(DECK_ID, '中小企業診断士_企業経営理論::01_経営戦略::エフェクチュエーション')

# --- カード ---
question = """エフェクチュエーションの定義と5つの原則を答えよ"""

answer = """<b>Effectuation</b>（エフェクチュエーション） — サラスバシー(Sarasvathy, 2001)

「今ある手段から何ができるか」を考える起業家の思考法。目標から逆算する<b>コーゼーション（Causation）</b>と対比される。

<b>5つの原則:</b>
1. <b>Bird in Hand</b>（手中の鳥）: 自分が持つ資源（スキル・人脈・知識）から始める
2. <b>Affordable Loss</b>（許容可能な損失）: 期待利益ではなく「失っても致命的でない範囲」で行動する
3. <b>Crazy Quilt</b>（クレイジーキルト）: 競合含む多様な関係者とパートナーシップを構築する
4. <b>Lemonade</b>（レモネード）: 予期せぬ事態を障害でなくチャンスとして活用する
5. <b>Pilot in the Plane</b>（パイロット）: 予測より自分がコントロールできることに集中する

<div class="formula">
<b>命名の由来:</b><br>
① Bird in Hand — 英語のことわざ "A bird in the hand is worth two in the bush"（手の中の1羽は藪の中の2羽に勝る＝不確実な大きな利益より、確実に手元にあるものを活かせ）<br>
② Affordable Loss — そのまま「許容できる損失」。期待リターンの最大化でなく損失の上限設定から考える<br>
③ Crazy Quilt — 端切れを自由に縫い合わせるパッチワーク技法。バラバラな関係者を縫い合わせてパートナーにする<br>
④ Lemonade — "When life gives you lemons, make lemonade"（人生がレモン＝酸っぱい状況を与えたら、レモネードを作れ＝工夫して価値に変えろ）<br>
⑤ Pilot in the Plane — 操縦士は天気予報に頼るだけでなく、コックピットで自ら操縦桿を握り状況をコントロールする
</div>

<div class="example">
<b>具体例イメージ:</b><br>
① 手中の鳥: 料理好きが自分の得意レシピで飲食店を開業<br>
② 許容可能な損失: 「貯金の10%まで」と決めてスモールスタート<br>
③ クレイジーキルト: 競合の飲食店と共同イベントを開催し集客<br>
④ レモネード: 亀田製菓が型抜きミスの三日月型を「柿の種」としてヒット商品化<br>
⑤ パイロット: 市場予測に頼らず、顧客の反応を見ながら柔軟にメニュー変更
</div>

<div class="important">R3〜R5で3年連続出題。5原則の名称と内容の対応が問われる。コーゼーション（目標→手段、予測重視）との違いも押さえる。</div>

<div class="source">出典: Sarasvathy『Effectuation』(2001), IT中小企業診断士 村上知也, WirelessWire News</div>"""

note = genanki.Note(model=model, fields=[question, answer])
deck.add_note(note)

# --- パッケージ出力 ---
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0109_エフェクチュエーション_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
