"""
スイッチングコスト（Switching Cost） - 中小企業診断士 企業戦略論
Switching Cost, Lock-in, First-Mover Advantage

作成日: 2026-03-06
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1741185501
DECK_ID = 1741185502

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_企業戦略論_スイッチングコスト',
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

# デッキ定義
deck = genanki.Deck(
    DECK_ID,
    '中小企業診断士_企業戦略論::03_競争戦略::スイッチングコスト'
)

# カード内容
question = """スイッチングコストの定義と3つの種類を答えよ"""

answer = """<b>Switching Cost</b>（スイッチングコスト）

<b>定義</b>: 利用中の製品・サービスから代替品に乗り換える際に発生するコストの総称

<table>
<tr><th>種類</th><th>内容</th><th>例</th></tr>
<tr><td><b>金銭的コスト</b></td><td>乗り換えに伴う直接的な支出</td><td>解約違約金、新製品の購入費</td></tr>
<tr><td><b>物理的コスト</b></td><td>新しい操作・手順を習得する手間</td><td>新ソフトの操作習得、データ移行作業</td></tr>
<tr><td><b>心理的コスト</b></td><td>慣れた製品から離れる不安・抵抗感</td><td>ブランドへの愛着、未知への不安</td></tr>
</table>

<ul>
<li>スイッチングコストが高い → <b>先行者優位が維持</b>されやすい</li>
<li>スイッチングコストが高い → <b>顧客の囲い込み</b>（ロックイン）効果</li>
</ul>

<div class="important">注意:</div>
物理的・心理的コストのコントロールが戦略の核心。金銭的値下げに頼らず売上維持が可能になる

<div class="source">出典: たかぴーの中小企業診断士試験 攻略ブログ、グロービス経営大学院</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/xx/smec_xx_0303_スイッチングコスト_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
