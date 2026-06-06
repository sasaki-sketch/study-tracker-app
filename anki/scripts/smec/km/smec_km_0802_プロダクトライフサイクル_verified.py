"""
Ankiカード: プロダクトライフサイクル（PLC）
科目: 中小企業診断士_企業経営理論
セクション: 08 マーケティング概論・戦略
作成日: 2026-03-14
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# --- モデル定義 ---
MODEL_ID = 1710390802
DECK_ID = 1610390802

model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_企業経営理論_プロダクトライフサイクル',
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
deck = genanki.Deck(DECK_ID, '中小企業診断士_企業経営理論::08_マーケティング概論::プロダクトライフサイクル')

# --- カード ---
question = """プロダクトライフサイクル（PLC）の4段階の特徴とマーケティング戦略を答えよ"""

answer = """<b>Product Life Cycle（PLC）</b>

製品が市場に投入されてから撤退するまでの売上・利益の推移を4段階で示すモデル。

<b>① 導入期（Introduction）</b>
<ul>
<li>売上: 低い / 利益: マイナス（開発費・販促費が大きい）</li>
<li>競合: 少ない</li>
<li>戦略目標: <b>認知拡大・試用促進</b></li>
<li>価格戦略: 上澄み吸収価格（スキミング）or 市場浸透価格（ペネトレーション）</li>
</ul>

<b>② 成長期（Growth）</b>
<ul>
<li>売上: 急増 / 利益: 増加（規模の経済が効く）</li>
<li>競合: 参入増加</li>
<li>戦略目標: <b>市場シェア最大化</b></li>
<li>製品改良・流通チャネル拡大・価格引き下げ</li>
</ul>

<b>③ 成熟期（Maturity）</b>
<ul>
<li>売上: ピーク→横ばい / 利益: 安定→低下</li>
<li>競合: 最も多い → 淘汰が始まる</li>
<li>戦略目標: <b>利益最大化・シェア防衛</b></li>
<li>市場の修正（新用途・新セグメント）、製品の修正（品質・機能改良）、マーケティングミックスの修正</li>
</ul>

<b>④ 衰退期（Decline）</b>
<ul>
<li>売上: 減少 / 利益: 減少</li>
<li>競合: 撤退が進む</li>
<li>戦略目標: <b>コスト削減 or 撤退判断</b></li>
<li>ただし<b>ロイヤルティの高い顧客が残り、利益率が維持されるケースもある</b>（R4第33問）</li>
</ul>

<div class="important">PLCは製品カテゴリ（例: スマートフォン）に適用する概念であり、個別ブランド（例: iPhone）の寿命とは異なる。また、PLCは<b>予測ツールではなく分析フレームワーク</b>である。</div>

<div class="source">出典: Kotler『Marketing Management』, 中小企業診断士R4第33問</div>"""

note = genanki.Note(model=model, fields=[question, answer])
deck.add_note(note)

# --- パッケージ出力 ---
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0802_プロダクトライフサイクル_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
