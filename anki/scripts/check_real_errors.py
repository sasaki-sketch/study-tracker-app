#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
実際のエラーを確認
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

def check_real_errors(back_content):
    """実際のエラーをチェック（改良版）"""
    errors = []

    # エラーパターン1: スペース + ight) (本当に\rightが壊れている場合)
    if ' ight)' in back_content or '\night)' in back_content:
        errors.append("\\right が壊れている: ' ight)' を検出")

    # エラーパターン2: スペース + eft( (本当に\leftが壊れている場合)
    if ' eft(' in back_content or '\neft(' in back_content:
        errors.append("\\left が壊れている: ' eft(' を検出")

    # エラーパターン3: 日本語の前にバックスラッシュ（本物の\+日本語）
    # \\日本語 は正しい（例: \\白 in LaTeX command）
    # \日本語 が間違い（Pythonエスケープシーケンス）
    # でもHTML内では\は一つに見える...

    # より正確なチェック: LaTeXコマンド以外の場所に\+日本語があるか
    japanese_backslash = re.findall(r'\\([ぁ-んァ-ヶー一-龠]{2,})', back_content)
    if japanese_backslash:
        # LaTeXコマンドっぽくない（2文字以上の日本語）場合のみエラー
        errors.append(f"日本語の前にバックスラッシュ: {japanese_backslash}")

    # エラーパターン4: LaTeXコマンドの最初のバックスラッシュが欠けている
    # rac{ (should be \frac{)
    broken_latex = []
    if re.search(r'[^\\a-zA-Z]rac\{', back_content):
        broken_latex.append('frac')
    if re.search(r'[^\\a-zA-Z]imes', back_content):
        broken_latex.append('times')
    if re.search(r'[^\\a-zA-Z]pprox', back_content):
        broken_latex.append('approx')
    if re.search(r'[^\\a-zA-Z]igma', back_content):
        broken_latex.append('sigma')

    if broken_latex:
        errors.append(f"LaTeXコマンド破損: {', '.join(broken_latex)}")

    return errors

def main():
    print("=" * 70)
    print("実際のエラー確認")
    print("=" * 70)
    print()

    # 統計学v2デッキの全カードを取得
    deck_name = "統計学v2"
    note_ids = invoke_anki('findNotes', query=f'deck:"{deck_name}"')

    print(f"📊 カード総数: {len(note_ids)}枚")
    print()

    error_cards = []
    for i, note_id in enumerate(note_ids, 1):
        note_info = invoke_anki('notesInfo', notes=[note_id])
        if not note_info:
            continue

        note = note_info[0]
        front = note['fields']['Front']['value']
        back = note['fields']['Back']['value']

        # フロント面からタイトル抽出
        front_text = re.sub(r'<[^>]+>', '', front).strip()[:50]

        # 実際のエラーチェック
        errors = check_real_errors(back)
        if errors:
            error_cards.append({
                'number': i,
                'front': front_text,
                'errors': errors
            })

    print("=" * 70)
    print("検証結果")
    print("=" * 70)
    print()

    if not error_cards:
        print("🎉 エラーなし！全75枚のカードが正常です！")
    else:
        print(f"❌ 実際のエラー: {len(error_cards)}枚")
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
