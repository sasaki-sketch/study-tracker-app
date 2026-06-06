"""
Ankiカード: 種類株式（会社法108条）
科目: 中小企業診断士_経営法務
セクション: 01_会社法
作成日: 2026-03-21
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1710010101
deck_id = 1710010102

my_model = genanki.Model(
    model_id,
    '中小企業診断士_経営法務_種類株式',
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
    '中小企業診断士_経営法務::01_会社法::種類株式'
)

question = '''会社法で認められている<span class="important">種類株式</span>の9種類と、それぞれの内容・活用場面を答えよ'''

answer = '''<b>Classified Shares</b>（種類株式）

<p>会社法108条で定められた、<b>普通株式と異なる権利内容を持つ株式</b>。9種類ある。</p>

<div class="formula">
<table>
<tr><th>#</th><th>種類</th><th>わかりやすく言うと</th><th>具体例</th></tr>
<tr><td>1</td><td><b>剰余金の配当</b></td><td>配当を多くもらえる/少なくなる株</td><td>「年5%の配当を優先的に受け取れる株式」をVCに発行</td></tr>
<tr><td>2</td><td><b>残余財産の分配</b></td><td>会社が潰れた時に優先的にお金が戻ってくる株</td><td>スタートアップ投資で「潰れても投資額は優先回収」とVC契約</td></tr>
<tr><td>3</td><td><b>議決権制限</b></td><td>経営に口出しできない代わりに配当が多い等の株</td><td>経営権を渡さず資金調達したい時。<b>上限: 発行済の1/2</b></td></tr>
<tr><td>4</td><td><b>譲渡制限</b></td><td>勝手に他人に売れない株</td><td>中小企業で「知らない人に株が渡るのを防ぐ」。非公開会社の基本</td></tr>
<tr><td>5</td><td><b>取得請求権付</b></td><td>株主が「この株、買い取って」と会社に言える株</td><td>VC:「上場できなかったら会社に買い取ってもらう」</td></tr>
<tr><td>6</td><td><b>取得条項付</b></td><td>一定の条件で会社が「強制的に回収する」株</td><td>「株主が死亡したら会社が自動的に株を買い取る」→相続による株式分散を防止</td></tr>
<tr><td>7</td><td><b>全部取得条項付</b></td><td>株主総会の決議で全部まとめて回収できる株</td><td>MBOでスクイーズアウトに活用。「100株→1株に併合」と同様の効果</td></tr>
<tr><td>8</td><td><b>拒否権付（黄金株）</b></td><td><b>たった1株でも</b>重要事項を拒否できる株</td><td>先代社長が黄金株を1株保有→後継者が勝手にM&amp;Aしようとしても<b>拒否できる</b></td></tr>
<tr><td>9</td><td><b>役員選任権付</b></td><td>特定の取締役を自分で選べる株</td><td>A社とB社の合弁会社で「A社は取締役2名、B社は1名を選任できる」</td></tr>
</table>
</div>

<div class="example">
<b>事業承継での活用パターン:</b><br><br>
先代社長の悩み: 息子に経営を任せたいが、暴走が心配<br>
　↓<br>
解決策: 息子に普通株式を譲渡（経営権を渡す）<br>
　　　 先代は<b>黄金株を1株だけ保有</b>（重要事項の拒否権を確保）<br>
　↓<br>
効果: 息子は自由に経営できるが、<br>
　　 M&amp;Aや定款変更など重要事項は先代の承認が必要
</div>

<div class="example">
<b>試験での引っかけ:</b><br>
・「議決権制限株式は発行数に上限がない」→ <b>×</b> <b>発行済株式総数の1/2</b>が上限<br>
・「黄金株は大量に保有しないと意味がない」→ <b>×</b> <b>1株でも拒否権</b>を行使できる<br>
・「種類株式は上場企業のみ発行できる」→ <b>×</b> <b>非公開会社でも発行可能</b>（むしろ中小企業で活用が多い）<br>
・「取得条項付と取得請求権付は同じ」→ <b>×</b> 取得条項付は<b>会社が</b>回収、取得請求権付は<b>株主が</b>請求
</div>

<div class="source">出典: 会社法108条、中小企業診断士試験</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

output_path = '/Users/sasaki/study_app/anki/scripts/smec/law/smec_law_0101_種類株式_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
