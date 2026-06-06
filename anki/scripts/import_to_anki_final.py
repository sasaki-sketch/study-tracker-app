#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AnkiConnect経由でギリシャ文字カードをAnkiにインポート（最終版）
- 改善版CSS v2.0
- 順番記憶用カードを追加
"""

import json
import urllib.request
import csv


def invoke_anki(action, **params):
    """AnkiConnectにリクエストを送信"""
    request_json = json.dumps({
        'action': action,
        'version': 6,
        'params': params
    }).encode('utf-8')

    try:
        response = urllib.request.urlopen(
            urllib.request.Request('http://localhost:8765', request_json)
        )
        result = json.loads(response.read().decode('utf-8'))

        if result['error']:
            raise Exception(f"AnkiConnect error: {result['error']}")

        return result['result']
    except Exception as e:
        print(f"❌ エラー: {e}")
        return None


def create_deck(deck_name="Greek Letters & Statistics"):
    """デッキを作成"""
    print(f"📚 デッキ '{deck_name}' を作成中...")
    result = invoke_anki('createDeck', deck=deck_name)
    if result is not None:
        print(f"✅ デッキ作成完了 (ID: {result})")
    return result


def create_model_v2():
    """改善版カスタムノートタイプを作成"""
    model_name = "Greek Letters v2 (Super Readable)"

    print(f"📝 ノートタイプ '{model_name}' を作成中...")

    # 改善版CSS v2.0 - 読み込み
    with open('IMPROVED_ANKI_CSS.css', 'r', encoding='utf-8') as f:
        css = f.read()

    # モデル作成
    result = invoke_anki(
        'createModel',
        modelName=model_name,
        inOrderFields=['Front', 'Back'],
        css=css,
        isCloze=False,
        cardTemplates=[
            {
                'Name': 'Card 1',
                'Front': '{{Front}}',
                'Back': '{{Front}}<hr id=answer>{{Back}}'
            }
        ]
    )

    if result is not None:
        print(f"✅ ノートタイプ作成完了（改善版v2.0）")
    else:
        print(f"ℹ️  既存のノートタイプを使用します")

    return model_name


def import_cards_from_csv(csv_file, deck_name, model_name):
    """CSVファイルからカードをインポート"""
    print(f"📥 {csv_file} からカードを読み込み中...")

    cards_added = 0
    cards_failed = 0

    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='\t')

        for row in reader:
            front = row['Front']
            back = row['Back']
            tags = row['Tags'].split()

            # カードを追加
            result = invoke_anki(
                'addNote',
                note={
                    'deckName': deck_name,
                    'modelName': model_name,
                    'fields': {
                        'Front': front,
                        'Back': back
                    },
                    'tags': tags,
                    'options': {
                        'allowDuplicate': False
                    }
                }
            )

            if result:
                cards_added += 1
                if cards_added % 10 == 0:
                    print(f"  ✓ {cards_added}枚インポート完了...")
            else:
                cards_failed += 1

    return cards_added, cards_failed


def add_order_memorization_cards(deck_name, model_name):
    """順番記憶用の特別カードを追加"""
    print(f"🎵 順番記憶用カードを追加中...")

    order_cards = [
        {
            'front': '<div class="question"><h3>ギリシャ文字24個の順番を覚える方法は?</h3></div>',
            'back': '''<div class="answer">
<h3 class="meaning">3つの効果的な記憶法</h3>

<div class="mnemonic">
<strong>🎵 方法1: もののけ姫の歌で覚える</strong>
<p>「もののけ姫」の「張りつめた弓の〜」のメロディーに合わせて:</p>
<p style="margin-top:10px; line-height: 2.0;">
<strong>アルファ・ベータ・ガンマ</strong><br>
<strong>デルタ・イプシロン</strong><br>
<strong>ゼータ・イータ・シータ・イオタ</strong><br>
<strong>カッパ・ラムダ・ミュー</strong><br>
<strong>ニュー・クシー・オミクロン</strong><br>
<strong>パイ・ロー・シグマ・タウ</strong><br>
<strong>ウプシロン・ファイ</strong><br>
<strong>カイ・プサイ・オメガ</strong>
</p>
</div>

<div class="context">
<strong>📊 方法2: 5文字ずつグループ化</strong>
<p><strong>グループ1:</strong> α β γ δ ε (アベガデ)</p>
<p><strong>グループ2:</strong> ζ η θ ι κ (ゼーシイカ)</p>
<p><strong>グループ3:</strong> λ μ ν ξ ο (ラミニクオ)</p>
<p><strong>グループ4:</strong> π ρ σ τ υ (パロシタウ)</p>
<p><strong>グループ5:</strong> φ χ ψ ω (ファカプオ)</p>
</div>

<div class="mnemonic">
<strong>💡 方法3: 語呂合わせ</strong>
<p>「アベガデル イゼイータシ イカラミニ グオパロシ タウプシ ファカプサオ」</p>
<p style="margin-top:10px; font-size: 19px; color: #666;">
※ラテン文字と似ている部分を意識すると覚えやすい!
</p>
</div>
</div>''',
            'tags': ['greek-alphabet', 'order-memorization', 'mnemonic-song', 'priority-S', 'essential']
        },
        {
            'front': '<div class="question"><h3>ギリシャ文字の最初の5文字は?</h3></div>',
            'back': '''<div class="answer">
<h3 class="meaning">α β γ δ ε</h3>

<div class="mnemonic">
<strong>💡 読み方:</strong>
<p>アルファ・ベータ・ガンマ・デルタ・イプシロン</p>
</div>

<div class="context">
<strong>📊 覚え方:</strong>
<p>「アベガデ」→「安倍さんがデート」</p>
<p>ラテン文字A, B, (C), D, Eに対応</p>
</div>
</div>''',
            'tags': ['greek-alphabet', 'order-memorization', 'group-1', 'priority-A']
        },
        {
            'front': '<div class="question"><h3>ギリシャ文字の6〜10番目は?</h3></div>',
            'back': '''<div class="answer">
<h3 class="meaning">ζ η θ ι κ</h3>

<div class="mnemonic">
<strong>💡 読み方:</strong>
<p>ツェータ・イータ・シータ・イオタ・カッパ</p>
</div>

<div class="context">
<strong>📊 覚え方:</strong>
<p>「ゼーシイカ」→「ゼーシーカ(Z-C-K)」</p>
<p>ラテン文字Z, H, (Θ), I, Kに近い</p>
</div>
</div>''',
            'tags': ['greek-alphabet', 'order-memorization', 'group-2', 'priority-A']
        },
        {
            'front': '<div class="question"><h3>ギリシャ文字の11〜15番目は?</h3></div>',
            'back': '''<div class="answer">
<h3 class="meaning">λ μ ν ξ ο</h3>

<div class="mnemonic">
<strong>💡 読み方:</strong>
<p>ラムダ・ミュー・ニュー・グザイ・オミクロン</p>
</div>

<div class="context">
<strong>📊 覚え方:</strong>
<p>「ラミニクオ」→「ラーメン煮込む王様」</p>
<p>μ=M(平均), ν=N(自由度), ο=O</p>
</div>
</div>''',
            'tags': ['greek-alphabet', 'order-memorization', 'group-3', 'priority-A']
        },
        {
            'front': '<div class="question"><h3>ギリシャ文字の16〜20番目は?</h3></div>',
            'back': '''<div class="answer">
<h3 class="meaning">π ρ σ τ υ</h3>

<div class="mnemonic">
<strong>💡 読み方:</strong>
<p>パイ・ロー・シグマ・タウ・ウプシロン</p>
</div>

<div class="context">
<strong>📊 覚え方:</strong>
<p>「パロシタウ」→「パロディ下」</p>
<p>π=円周率, ρ=相関, σ=標準偏差(最重要!)</p>
</div>
</div>''',
            'tags': ['greek-alphabet', 'order-memorization', 'group-4', 'priority-S']
        },
        {
            'front': '<div class="question"><h3>ギリシャ文字の最後の4文字は?</h3></div>',
            'back': '''<div class="answer">
<h3 class="meaning">φ χ ψ ω</h3>

<div class="mnemonic">
<strong>💡 読み方:</strong>
<p>ファイ・カイ・プサイ・オメガ</p>
</div>

<div class="context">
<strong>📊 覚え方:</strong>
<p>「ファカプオ」→「ファッカープ王」</p>
<p>χ=カイ二乗検定, ω=オメガ(終わり)</p>
</div>
</div>''',
            'tags': ['greek-alphabet', 'order-memorization', 'group-5', 'priority-A']
        },
        {
            'front': '<div class="question"><h3>統計で最重要な5文字を順番に言えますか?</h3></div>',
            'back': '''<div class="answer">
<h3 class="meaning">α, β, μ, σ, χ</h3>

<div class="mnemonic">
<strong>💡 覚え方:</strong>
<p><strong>「アベ・ミス・カイ」</strong>（安倍さんミスって買い物）</p>
</div>

<div class="context">
<strong>📊 意味:</strong>
<p>α = 有意水準 (1番目)</p>
<p>β = 第2種過誤 (2番目)</p>
<p>μ = 母平均 (12番目)</p>
<p>σ = 標準偏差 (18番目)</p>
<p>χ = カイ二乗検定 (22番目)</p>
</div>

<div class="info">
<small>この5つを覚えれば統計学の80%をカバー!</small>
</div>
</div>''',
            'tags': ['greek-alphabet', 'order-memorization', 'priority-S', 'essential', 'statistics-top5']
        }
    ]

    cards_added = 0
    for card in order_cards:
        result = invoke_anki(
            'addNote',
            note={
                'deckName': deck_name,
                'modelName': model_name,
                'fields': {
                    'Front': card['front'],
                    'Back': card['back']
                },
                'tags': card['tags'],
                'options': {
                    'allowDuplicate': False
                }
            }
        )

        if result:
            cards_added += 1

    print(f"✅ 順番記憶用カード {cards_added}枚を追加しました")
    return cards_added


def main():
    """メイン実行"""
    print("=" * 70)
    print("ギリシャ文字カード → Anki インポート（最終版v2.0）")
    print("=" * 70)
    print()

    # AnkiConnect接続確認
    print("🔌 AnkiConnectに接続中...")
    version = invoke_anki('version')
    if version is None:
        print("❌ Ankiが起動していないか、AnkiConnectがインストールされていません")
        print("   Ankiを起動してから再度実行してください")
        return

    print(f"✅ AnkiConnect接続成功 (version {version})")
    print()

    # デッキ作成
    deck_name = "Greek Letters & Statistics"
    create_deck(deck_name)
    print()

    # ノートタイプ作成（改善版）
    model_name = create_model_v2()
    print()

    # 基本カードインポート
    csv_file = "greek_letters_anki.csv"
    cards_added, cards_failed = import_cards_from_csv(csv_file, deck_name, model_name)
    print()

    # 順番記憶用カード追加
    order_cards_added = add_order_memorization_cards(deck_name, model_name)

    total_cards = cards_added + order_cards_added

    print()
    print("=" * 70)
    print("✨ インポート完了!")
    print("=" * 70)
    print()
    print(f"📊 結果:")
    print(f"  ✅ 基本カード: {cards_added}枚")
    print(f"  ✅ 順番記憶カード: {order_cards_added}枚")
    print(f"  ✅ 合計: {total_cards}枚")
    if cards_failed > 0:
        print(f"  ⚠️  スキップ: {cards_failed}枚")
    print()
    print(f"🎨 デザイン改善:")
    print(f"  ✓ ギリシャ文字: 180px（超巨大!）")
    print(f"  ✓ カタカナ読み: 72px（鮮やかな青）")
    print(f"  ✓ 英語読み: 36px（濃いグレー）")
    print(f"  ✓ 記憶術・使用例: 22px（ほぼ黒、読みやすい）")
    print()
    print(f"🎵 順番記憶法:")
    print(f"  ✓ もののけ姫の歌")
    print(f"  ✓ 5文字ずつグループ化")
    print(f"  ✓ 語呂合わせ")
    print(f"  ✓ 統計最重要5文字")
    print()
    print(f"🚀 次のステップ:")
    print(f"  1. Ankiで '{deck_name}' デッキを確認")
    print(f"  2. tag:order-memorization で順番カードを確認")
    print(f"  3. 学習開始!")
    print()


if __name__ == "__main__":
    main()
