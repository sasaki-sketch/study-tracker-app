"""
Ankiカード: クープマン大陸全体マップ（フロンティア山 × クープマン山）
科目: 中小企業診断士_企業経営理論
セクション: 02_競争戦略
作成日: 2026-04-23
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki/02_Personal/anki')
from anki_card_css_template import CARD_CSS

model_id = 1702160001
deck_id = 1702160002

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_クープマン大陸マップ',
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
    '中小企業診断士_企業経営理論::02_競争戦略::クープマン大陸マップ'
)

question = '''<span class="important">クープマン大陸全体マップ</span>を描け。<br><br>・<b>2つの山の比較</b><br>・<b>PLC（既存0802）との対応</b><br>・<b>14キャラ全覧（7+7）</b><br>・<b>山の遷移プロセス</b><br>・<b>BYD型とクープマン目標値の適用範囲</b>'''

answer = '''<b>Koopman Continent — Unified Map of Competitive Strategy</b><br>（クープマン大陸 統合マップ）

<div class="formula">
<b>■ 2つの山の比較</b>
<table>
<tr><th></th><th>🌋 フロンティア山</th><th>🏔 クープマン山</th></tr>
<tr><td>市場段階</td><td>成長（導入〜成長期）</td><td>成熟</td></tr>
<tr><td>パイ</td><td>拡大中</td><td>固定</td></tr>
<tr><td>頂点</td><td>流動・変動</td><td>73.9%で固定</td></tr>
<tr><td>主理論</td><td>破壊的イノベ、BO、キャズム</td><td><b>クープマン目標値</b></td></tr>
<tr><td>勝ち筋</td><td>武器×タイミング</td><td>シェア階段戦略</td></tr>
</table>
</div>

<div class="example">
<b>■ PLC（既存カード0802）との対応</b><br>
<b>導入期</b> → フロンティア山前半（ハタタテ旗立て〜乱戦）<br>
<b>成長期</b> → フロンティア山後半（タニワタリ軍団がキャズム越え→テイクオフ）<br>
<b>成熟期</b> → <b>クープマン山に変貌</b>（7戦士の物語が7階層の物語に再構成）<br>
<b>衰退期</b> → 将来拡張（崩落山？ 今回スコープ外）
</div>

<div class="formula">
<b>■ 14キャラ全覧</b>
<table>
<tr><th>🌋 フロンティア山（成長）</th><th>🏔 クープマン山（成熟）</th></tr>
<tr><td>1. ハタタテ開拓者（先発）</td><td>73.9% ナナサンキュー大王（独占）</td></tr>
<tr><td>2. マネマネ猿（後発）</td><td>41.7% ヨイナ公爵（安定）</td></tr>
<tr><td>3. ヒエヒエ帝王（隣接侵略）</td><td>26.1% ニロイチ豪傑（挑戦権）</td></tr>
<tr><td>4. ハカイ錬金術師（破壊）</td><td>19.3% イクミ戦士（上位）</td></tr>
<tr><td>5. アミハリ大司教（ネット効果）</td><td>10.9% テンキュー魔術師（認識）</td></tr>
<tr><td>6. アオウミ海賊（BO）</td><td>6.8% ロクヤ小人（存在）</td></tr>
<tr><td>7. タニワタリ軍団★（キャズム）</td><td>2.8% ニッパチスパイ（橋頭堡）</td></tr>
</table>
</div>

<div class="example">
<b>■ 山の遷移プロセス</b><br>
ハタタテ旗立て → 乱戦 → <b>タニワタリ軍団のキャズム越え</b><br>
　→ 市場テイクオフ → 成熟化 → <b>山が冷え固まる</b><br>
　→ <b>クープマン山へ遷移完了</b><br>
　→ ナナサンキュー大王と7階層の秩序が形成される
</div>

<div class="example">
<b>■ 適用範囲の使い分け（★試験で問われやすい）</b><br>
・<b>BYD型（隣接市場侵略）</b> → <b>フロンティア山</b>でのみ通用<br>
・<b>クープマン目標値（73.9/41.7/26.1%）</b> → <b>クープマン山</b>でのみ意味を持つ<br>
・<b>コトラー競争地位戦略</b>（0804）→ クープマン山側と対応<br>
・<b>PLCの時系列</b>（0802）→ 両山をまたぐ通し時間軸
</div>

<div class="source">出典: 設計プラン /Users/sasaki/.claude/plans/tender-moseying-meteor.md; 田岡信夫『ランチェスター戦略』; 既存カード 0410/0422/0802/0804/0208-0210</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

output_path = '/Users/sasaki/02_Personal/anki/anki/scripts/smec/km/smec_km_0216_クープマン大陸マップ_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
