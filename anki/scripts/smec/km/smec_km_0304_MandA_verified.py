"""
Ankiカード: M&Aの種類
科目: 中小企業診断士_企業経営理論
セクション: 03_成長戦略・国際経営
作成日: 2026-03-21
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1703040301
deck_id = 1703040302

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_MandA',
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
    '中小企業診断士_企業経営理論::03_成長戦略・国際経営::MandA'
)

question = '''<span class="important">M&amp;Aの種類</span>（合併・買収の分類、手法、買収防衛策）を答えよ'''

answer = '''<b>Mergers &amp; Acquisitions</b>（M&amp;A）

<div class="formula">
<b>M&amp;Aの全体像:</b><br><br>
M&amp;A<br>
　├─ <b>合併</b>（2社が1社になる）<br>
　│　├─ 吸収合併（A社がB社を吸収。B社は消滅）<br>
　│　└─ 新設合併（A社もB社も消滅→新C社を設立）<br>
　└─ <b>買収</b>（会社or事業を買う）<br>
　　　├─ 株式取得（株を買って経営権を握る）<br>
　　　└─ 事業譲受（会社丸ごとではなく特定の事業だけ買う）
</div>

<div class="formula">
<b>主な買収手法:</b>
<table>
<tr><th>手法</th><th>誰が</th><th>わかりやすく言うと</th></tr>
<tr><td><b>Take-Over Bid（TOB）</b></td><td>買収したい企業</td><td>株の<b>まとめ買い宣言</b>。市場で静かに買うと株価が上がるので、価格と期間を決めて株主に直接呼びかけ一気に集める</td></tr>
<tr><td><b>Management Buy-Out（MBO）</b></td><td><b>今の経営陣</b></td><td>社長が「この会社、自分で買います」。上場廃止して自由に経営したい時など</td></tr>
<tr><td><b>Management Buy-In（MBI）</b></td><td><b>外部の経営者</b></td><td>外から来た人が「この会社、私が経営します」と株を買い取って乗り込む</td></tr>
<tr><td><b>Leveraged Buy-Out（LBO）</b></td><td>買収者</td><td>「買う相手の財産を担保にお金を借りて買う」。自己資金が少なくても大型買収が可能</td></tr>
<tr><td><b>Employee Buy-Out（EBO）</b></td><td><b>従業員</b></td><td>社員が「自分たちの会社は自分たちで守る」と自社株を買い取る</td></tr>
</table>
</div>

<div class="mnemonic">
<b>覚え方: ○BOの○が「誰が買うか」</b><br>
・<b>M</b>anagement（現経営陣）→ MBO<br>
・Management Buy-<b>I</b>n（外から<b>I</b>n）→ MBI<br>
・<b>L</b>everaged（てこ＝借金）→ LBO<br>
・<b>E</b>mployee（従業員）→ EBO
</div>

<div class="formula">
<b>主な買収防衛策:</b>
<table>
<tr><th>防衛策</th><th>やること</th><th>なぜ防衛になるか</th></tr>
<tr><td><b>Poison Pill</b><br>（ポイズンピル/毒薬条項）</td><td>敵対的買収が起きたら既存株主に新株を安く買える権利を発動</td><td>株が大量に増える→買収者の持株比率が<b>薄まって</b>経営権を握れなくなる</td></tr>
<tr><td><b>White Knight</b><br>（ホワイトナイト/白馬の騎士）</td><td>友好的な別の会社に「うちを買ってください」と頼む</td><td>敵に買われるくらいなら<b>味方に買ってもらう</b></td></tr>
<tr><td><b>Crown Jewel</b><br>（クラウンジュエル/焦土作戦）</td><td>自社の最も価値ある事業・資産をわざと売却</td><td>「欲しかった宝石がもうない」→ 買収する<b>旨味がなくなる</b></td></tr>
<tr><td><b>Golden Parachute</b><br>（ゴールデンパラシュート）</td><td>経営陣の退職金を巨額に設定しておく</td><td>買収して経営陣をクビにすると<b>莫大な退職金が発生</b>→買収コストが膨らむ</td></tr>
<tr><td><b>Pac-Man Defense</b><br>（パックマンディフェンス）</td><td>逆に相手企業を買収しにいく</td><td>「食べられそうになったら<b>逆に食べ返す</b>」</td></tr>
<tr><td><b>Shark Repellent</b><br>（シャークリペラント/サメ除け）</td><td>買収を困難にする条項を<b>定款にあらかじめ</b>盛り込んでおく</td><td>サメ（＝買収者）が近づけないよう<b>事前に予防</b>。取締役の任期ずらし、特別決議要件の引上げなど</td></tr>
<tr><td><b>Greenmail</b><br>（グリーンメール）</td><td>買収者が大量取得した株式を、対象企業に<b>高値で買い取らせる</b>ことを狙う行為</td><td>脅迫状（blackmail）＋ドル紙幣（green）。<b>買収が目的ではなく、高値での株の買い戻しが目的</b>。防衛側が応じることも含む</td></tr>
<tr><td><b>Tin Parachute</b><br>（ティンパラシュート）</td><td>ゴールデンパラシュートの<b>従業員版</b>。全従業員に高額退職金を設定</td><td>Golden（金）→ Tin（ブリキ）に格下げだが、<b>対象人数が多い</b>ため買収コストが膨大に</td></tr>
<tr><td><b>第三者割当増資</b></td><td>友好的な第三者に<b>新株を発行</b>して買収者の持株比率を下げる</td><td>ポイズンピルと似るが、<b>実際に新株を発行</b>する点が異なる</td></tr>
</table>
</div>

<div class="formula">
<b>事前対策 vs 事後対応:</b>
<table>
<tr><th>事前対策（あらかじめ仕込む）</th><th>事後対応（買収を仕掛けられてから）</th></tr>
<tr><td>サメ除け（定款変更）<br>ゴールデンパラシュート（経営陣退職金）<br>ティンパラシュート（従業員退職金）<br>ポイズンピル（新株予約権を仕込む）</td><td>ホワイトナイト（味方に買ってもらう）<br>パックマン（逆に買収しにいく）<br>クラウンジュエル（資産売却）<br>グリーンメール（高値で買い戻し）<br>第三者割当増資（味方に新株発行）</td></tr>
</table>
※ポイズンピルは事前に仕込み、買収時に発動する<b>両方の性質</b>を持つ
</div>

<div class="example">
<b>試験での引っかけ:</b><br>
・「MBOは外部経営者による買収」→ <b>×</b> 外部は<b>MBI</b>、MBOは<b>現経営陣</b><br>
・「LBOは自己資金が豊富な企業の手法」→ <b>×</b> <b>借入金</b>で買収（少ない資金で可能）<br>
・「新設合併では一方の会社が存続する」→ <b>×</b> 両方消滅。一方存続は<b>吸収合併</b><br>
・「自社の重要な資産を売却するのはサメ除け」→ <b>×</b> 資産売却は<b>クラウンジュエル</b>。サメ除けは<b>定款変更による予防策</b><br>
・「ゴールデンパラシュートで経営陣が自社株を買い上場廃止」→ <b>×</b> それは<b>MBO</b>。ゴールデンパラシュートは<b>退職金を高額に設定</b>
</div>

<div class="source">出典: 中小企業診断士試験 R6第5問</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0304_MandA_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
