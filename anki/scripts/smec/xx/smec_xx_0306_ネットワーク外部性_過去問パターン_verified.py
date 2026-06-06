"""
ネットワーク外部性・情報財 過去問頻出パターン - 中小企業診断士 企業戦略論
Network Externality, Information Goods, De facto Standard, Commodity, Past Exam Patterns

作成日: 2026-03-06
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1741185801
DECK_ID = 1741185802

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_企業戦略論_ネットワーク外部性_過去問パターン',
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
    '中小企業診断士_企業戦略論::03_競争戦略::ネットワーク外部性_過去問パターン'
)

# カード内容
question = """ネットワーク外部性・情報財・デファクトスタンダードの過去問頻出ひっかけパターンを答えよ"""

answer = """<b>Network Externality / Information Goods — 頻出誤答パターン集</b>

<table>
<tr><th>#</th><th>ひっかけ内容</th><th>正しい理解</th><th>出題</th></tr>
<tr><td>1</td><td>直接的効果と間接的効果の<b>定義を入れ替え</b></td><td>直接的＝ユーザー同士の接続、間接的＝補完財を介した恩恵</td><td>R2第13問エ</td></tr>
<tr><td>2</td><td>デファクトスタンダードは<b>最も性能が高い製品</b>が獲得する</td><td>性能ではなく<b>市場での採用実績</b>が決定要因</td><td>R2第13問ウ</td></tr>
<tr><td>3</td><td>デファクトスタンダードは<b>ソフトウェアのみ</b>で発生</td><td>あらゆる分野で発生する</td><td>R2第13問イ</td></tr>
<tr><td>4</td><td>ISO等がデファクトスタンダードの確立に重要</td><td>ISOは<b>デジュール</b>スタンダード。デファクトは市場競争で決まる</td><td>R2第13問ア</td></tr>
<tr><td>5</td><td>ネットワーク外部性が大きいと顧客数増加で価値が<b>希薄化</b></td><td>逆。顧客数が増えるほど価値は<b>増大</b>する</td><td>R3第12問エ</td></tr>
<tr><td>6</td><td>情報財はスイッチングコストによる囲い込みが<b>有効でない</b></td><td>データ蓄積等により情報財でもスイッチングコストは有効</td><td>R3第12問イ</td></tr>
<tr><td>7</td><td>情報財の一部を無償提供すると広告以外の収入は<b>不可能</b></td><td>一部無償＋別部分有償など複数の収益モデルは可能</td><td>R3第12問ア</td></tr>
<tr><td>8</td><td>特許があれば先行者優位は<b>維持される</b></td><td>約60%は回避設計で模倣。特許単独では不十分</td><td>R5第6問ア</td></tr>
</table>

<b>情報財のコスト構造</b>（R1第8問・R3第12問で出題）:
<div class="formula">
固定費用（開発費）が<b>高い</b>、限界費用（複製費）が<b>低い</b><br>
→ コモディティ化で価格競争が激化 → 価格が<b>限界費用近傍まで下落</b> → 開発費が回収不能に
</div>

<b>正答になりやすいパターン</b>:
<ul>
<li>「ユーザー数を競合より<b>早期に増やす</b>ことが有効」（R2第13問オ）</li>
<li>「<b>スイッチングコストが高い</b>と先行者優位が維持」（R5第6問イ）</li>
<li>「コモディティ化で<b>限界費用まで価格下落</b>し開発費回収不能」（R3第12問オ）</li>
<li>情報財の空欄穴埋め: 固定費=<b>高</b>、限界費用=<b>低</b>、ネットワーク外部性（R1第8問）</li>
</ul>

<div class="source">出典: スタディング R2第13問、一発合格まとめシート R3第12問、資格部 R1第8問</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/xx/smec_xx_0306_ネットワーク外部性_過去問パターン_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
