#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
全カードの最終検証
- 全75枚のカードをチェック
- LaTeXコマンドのエラーを検出
"""

import json
import urllib.request
import re

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

def check_card_errors(back_content):
    """カードの裏面をチェックしてエラーパターンを検出"""
    errors = []

    # エラーパターン1: \right が ight になっている
    if re.search(r'[^\\]ight\)', back_content) or ' ight)' in back_content:
        errors.append("\\right が ight になっている")

    # エラーパターン2: \left が eft になっている
    if re.search(r'[^\\]eft\(', back_content) or ' eft(' in back_content:
        errors.append("\\left が eft になっている")

    # エラーパターン3: 日本語の前にバックスラッシュ
    if re.search(r'\\[ぁ-んァ-ヶー一-龠]', back_content):
        errors.append("日本語の前にバックスラッシュ")

    # エラーパターン4: LaTeXコマンドが壊れている
    broken_commands = []
    if 'rac{' in back_content and '\\frac{' not in back_content:
        broken_commands.append('\\frac → rac')
    if 'imes' in back_content and '\\times' not in back_content:
        broken_commands.append('\\times → imes')
    if 'pprox' in back_content and '\\approx' not in back_content:
        broken_commands.append('\\approx → pprox')
    if 'um_' in back_content and '\\sum_' not in back_content:
        broken_commands.append('\\sum → um')
    if 'igma' in back_content and '\\sigma' not in back_content:
        broken_commands.append('\\sigma → igma')

    if broken_commands:
        errors.append(f"LaTeXコマンド破損: {', '.join(broken_commands)}")

    return errors

def main():
    print("=" * 70)
    print("全カード最終検証")
    print("=" * 70)
    print()

    # AnkiConnect接続確認
    print("🔌 AnkiConnectに接続中...")
    version = invoke_anki('version')
    if version is None:
        print("❌ Ankiが起動していないか、AnkiConnectがインストールされていません")
        return

    print(f"✅ AnkiConnect接続成功")
    print()

    # 統計学v2デッキの全カードを取得
    deck_name = "統計学v2"
    print(f"📚 デッキ: {deck_name}")

    note_ids = invoke_anki('findNotes', query=f'deck:"{deck_name}"')
    if not note_ids:
        print("❌ カードが見つかりません")
        return

    print(f"📊 カード総数: {len(note_ids)}枚")
    print()

    # 全カードをチェック
    print("🔍 全カード検証中...")
    print()

    error_cards = []
    for i, note_id in enumerate(note_ids, 1):
        note_info = invoke_anki('notesInfo', notes=[note_id])
        if not note_info:
            continue

        note = note_info[0]
        front = note['fields']['Front']['value']
        back = note['fields']['Back']['value']

        # フロント面からタイトル抽出（簡易版）
        front_text = re.sub(r'<[^>]+>', '', front).strip()[:50]

        # エラーチェック
        errors = check_card_errors(back)
        if errors:
            error_cards.append({
                'id': note_id,
                'number': i,
                'front': front_text,
                'errors': errors
            })

    print()
    print("=" * 70)
    print("検証結果")
    print("=" * 70)
    print()

    if not error_cards:
        print("🎉 エラーなし！全75枚のカードが正常です！")
        print()
        print("✅ チェック項目:")
        print("   • \\right が正しくエスケープされている")
        print("   • \\left が正しくエスケープされている")
        print("   • 日本語の前にバックスラッシュがない")
        print("   • LaTeXコマンドが破損していない")
    else:
        print(f"❌ エラー発見: {len(error_cards)}枚")
        print()
        for card in error_cards:
            print(f"カード{card['number']}: {card['front']}")
            for error in card['errors']:
                print(f"  • {error}")
            print()

    print()
    print("=" * 70)

if __name__ == "__main__":
    main()
