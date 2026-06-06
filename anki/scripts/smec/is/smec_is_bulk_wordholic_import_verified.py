"""
Ankiカード一括インポート: Wordholic → Anki
科目: 中小企業診断士_経営情報システム (smec_is)
元ファイル: johou_card_wordholic2026.csv
作成日: 2026-03-20
"""

import genanki
import csv
import hashlib
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1706010001
deck_id = 1706010002

my_model = genanki.Model(
    model_id,
    '中小企業診断士_経営情報システム_Wordholic移行',
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
    '中小企業診断士_経営情報システム::Wordholic移行'
)

# CSV読み込み
csv_path = '/Users/sasaki/Downloads/johou_card_wordholic2026.csv'
card_count = 0

with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for idx, row in enumerate(reader):
        front = row['FrontText'].strip()
        back = row['BackText'].strip()
        if not front or not back:
            continue
        # 改行をHTMLの<br>に変換
        front_html = front.replace('\n', '<br>')
        back_html = back.replace('\n', '<br>')
        # ユニークなGUIDを生成（科目コード + インデックス + front + back）
        unique_str = f"smec_is_{idx}_{front}_{back}"
        guid = genanki.guid_for(unique_str)
        note = genanki.Note(
            model=my_model,
            fields=[front_html, back_html],
            guid=guid
        )
        my_deck.add_note(note)
        card_count += 1

# .apkg出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/is/smec_is_bulk_wordholic_import_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
print(f"Total cards: {card_count}")
