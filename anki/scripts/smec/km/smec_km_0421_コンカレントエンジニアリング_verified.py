"""
Ankiカード: コンカレントエンジニアリング（Concurrent Engineering）
科目: 中小企業診断士_企業経営理論
セクション: 04_技術経営・イノベーション
検証済み: 2026-03-19
出典: 中小企業診断士 企業経営理論 R2第7問
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1710421001
deck_id = 1710421002

model = genanki.Model(
    model_id,
    'smec_km_0421_コンカレントエンジニアリング',
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

deck = genanki.Deck(deck_id, '中小企業診断士_企業経営理論::04_技術経営・イノベーション::コンカレントエンジニアリング')

question = '''コンカレントエンジニアリングの定義と、関連する開発管理手法（ステージゲート・重量級PM・プラットフォームマネジャー）との違いを答えよ'''

answer = '''<b>Concurrent Engineering</b>（コンカレントエンジニアリング / CE）

<br><br>
<b>定義</b>: 各機能部門が業務を終了してから次へ引き渡す逐次型ではなく、各機能業務を<span class="important">並行させて</span>商品開発を進める手法

<br><br>
<b>関連する開発管理手法:</b>
<table>
<tr><th>手法</th><th>役割</th></tr>
<tr><td><b>ステージゲート</b></td><td>開発初期段階でアイデアを徐々に<b>絞り込む</b>プロセス</td></tr>
<tr><td><b>重量級PM</b></td><td>部門横断チームを<b>先導</b>するプロジェクトリーダー</td></tr>
<tr><td><b>プラットフォームマネジャー</b></td><td>複数の商品開発プロジェクトを<b>統括管理</b></td></tr>
</table>

<br>
<div class="example">
<b>注意</b>: 重量級PMは個別プロジェクト向け。複数プロジェクトの商品ライン共通化には<b>プラットフォームマネジャー</b>が有効
</div>

<div class="source">出典: 中小企業診断士 企業経営理論 R2第7問</div>'''

note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ作成
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0421_コンカレントエンジニアリング_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Created: {output_path}")
