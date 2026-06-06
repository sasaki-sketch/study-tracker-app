"""
デファクトスタンダード（De facto Standard） - 中小企業診断士 企業戦略論
De facto Standard, De jure Standard, Network Externality

作成日: 2026-03-06
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1741185701
DECK_ID = 1741185702

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_企業戦略論_デファクトスタンダード',
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
    '中小企業診断士_企業戦略論::03_競争戦略::デファクトスタンダード'
)

# カード内容
question = """デファクトスタンダードの定義、デジュールスタンダードとの違い、獲得戦略を答えよ"""

answer = """<b>De facto Standard</b>（デファクトスタンダード / 事実上の業界標準）

<b>定義</b>: 公的機関の認定ではなく、<b>市場競争を通じて</b>確立される規格

<table>
<tr><th></th><th>デファクトスタンダード</th><th>デジュールスタンダード</th></tr>
<tr><td><b>意味</b></td><td>事実上の標準</td><td>公的な標準</td></tr>
<tr><td><b>決定主体</b></td><td>市場競争の結果</td><td>ISO等の標準化機関</td></tr>
<tr><td><b>例</b></td><td>Windows、USB</td><td>JIS規格、ISO9001</td></tr>
</table>

<b>獲得戦略</b>:
<ul>
<li>ネットワーク外部性を活用し、<b>早期にユーザー数を拡大</b>する</li>
<li>ライセンス供与・オープン化で普及を加速させる</li>
<li>補完財（アプリ等）の充実を促す</li>
</ul>

<div class="important">注意（頻出ひっかけポイント）:</div>
<ul>
<li>デファクトスタンダードは<b>最も基本性能が高い製品とは限らない</b>（R2第13問ウ）</li>
<li>ソフトウェアに限定されず<b>あらゆる分野</b>で発生する（R2第13問イ）</li>
<li>直接的効果と間接的効果の定義を入れ替えるひっかけに注意（R2第13問エ）</li>
</ul>

<div class="source">出典: スタディング R2第13問解説、中小企業診断士独学攻略ブログ</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/xx/smec_xx_0305_デファクトスタンダード_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
