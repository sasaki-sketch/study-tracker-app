"""
Ankiカード: イノベーションと補完的資産
科目: 中小企業診断士_企業経営理論
セクション: 04_技術経営・イノベーション
作成日: 2026-03-16
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1704180001
deck_id = 1704180002

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_補完的資産',
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
    '中小企業診断士_企業経営理論::04_技術経営・イノベーション::補完的資産'
)

# カード内容
question = '''ティースが提唱した「補完的資産」の定義と<span class="important">3つの分類</span>、および<span class="important">専有可能性との組み合わせ</span>でイノベーションの利益を誰が獲得するかを答えよ'''

answer = '''<b>Complementary Assets &amp; Appropriability</b>（補完的資産と専有可能性）

<p>ティース（D.J. Teece, 1986）が「Profiting from Technological Innovation」で提唱。<b>技術的にイノベーションを起こしても、利益を獲得できるとは限らない</b>。利益の帰属を決めるのは「専有可能性」と「補完的資産」の2要素。</p>

<div class="formula">
<b>補完的資産（Complementary Assets）:</b><br>
イノベーションを商業化するために必要な、技術以外の経営資源。
<table>
<tr><th>分類</th><th>定義</th><th>具体例</th></tr>
<tr><td><b>汎用的（Generic）</b></td><td>市場で容易に調達可能</td><td>一般的な製造設備、物流、事務機能</td></tr>
<tr><td><b>専門化（Specialized）</b></td><td>特定の技術・製品に一方向で依存</td><td>専用の製造ライン、専門の販売チャネル</td></tr>
<tr><td><b>共特化（Co-specialized）</b></td><td>イノベーションと資産が<b>相互に依存</b></td><td>特定技術に最適化された製造工程＋その工程でしか作れない製品</td></tr>
</table>
→ <b>共特化</b>の補完的資産を持つ企業ほど、イノベーションからの利益を確保しやすい
</div>

<div class="example">
<b>専有可能性（Appropriability Regime）:</b><br>
イノベーターが模倣者から技術を守れる程度。特許・企業秘密・暗黙知の複雑さなどで決まる。<br><br>

<b>誰が利益を得るか（2×2の組み合わせ）:</b>
<table>
<tr><th></th><th>補完的資産：<b>弱い</b></th><th>補完的資産：<b>強い</b></th></tr>
<tr><td>専有可能性：<b>強い</b></td><td><b>イノベーター</b>が利益を得る（特許で守れる）</td><td><b>イノベーター</b>が利益を得る（最強）</td></tr>
<tr><td>専有可能性：<b>弱い</b></td><td><b>誰も利益を得にくい</b>（模倣され、補完資産もない）</td><td><b>補完的資産の保有者</b>（模倣者・既存大企業）が利益を得る</td></tr>
</table>
<br>
例: EMI社がCTスキャンを発明（イノベーター）→ 専有可能性が弱く、医療機器の販売網・アフターサービス（補完的資産）を持つGEやシーメンスに利益を奪われた
</div>

<p><b>注意</b>: 技術力だけでは勝てない。専有可能性が弱い分野（模倣されやすい）では、販売網・製造能力・ブランド等の<b>補完的資産を持つ既存大企業が後発でも利益を獲得</b>する。ベンチャーは補完的資産を持たないため、アライアンスやライセンス戦略が重要になる。ダーウィンの海（事業化→産業化の壁）の本質もここにある。</p>

<div class="source">出典: D.J. Teece (1986) "Profiting from Technological Innovation"、GRIPS SciREX、レイヤーズ・コンサルティング</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

# .apkg出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0418_補完的資産_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
