#!/usr/bin/env python3
"""
English Learning - My Corrections
自分の英語ミスから学ぶAnkiカード

作成日: 2026-01-27
"""

import genanki
import random
import sys
sys.path.append('/Users/sasaki')
from anki_card_css_template import CARD_CSS

# Generate unique IDs
MODEL_ID = random.randrange(1 << 30, 1 << 31)
DECK_ID = random.randrange(1 << 30, 1 << 31)

# Model definition
model = genanki.Model(
    MODEL_ID,
    'English_Corrections',
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

# Deck definition
deck = genanki.Deck(
    DECK_ID,
    'English Learning::My Corrections'
)

# =============================================================================
# Card 1: "add the feature that" → "add a feature to"
# =============================================================================
card1_q = '''
<b>英語添削カード</b><br><br>
次の文の間違いを直してください：<br><br>
<div class="formula">
"Could you add the feature <span class="important">that my English errors modify</span> to /english-on?"
</div>
'''

card1_a = '''
<b>Corrected version:</b>
<div class="formula">
"Could you add <span class="important">a feature to correct</span> my English errors to /english-on?"
</div>

<br>
<b>Errors & Corrections:</b>
<table>
<tr><th>Error</th><th>Correction</th><th>Explanation</th></tr>
<tr><td>the feature that</td><td>a feature to</td><td>「〜する機能」は "a feature to [verb]" が自然</td></tr>
<tr><td>my English errors modify</td><td>correct my English errors</td><td>語順が逆。目的語は動詞の後に置く</td></tr>
</table>

<div class="example">
<b>Pattern to remember:</b><br>
"Could you add a feature <b>to [verb]</b> ...?"<br>
（〜する機能を追加してもらえますか？）
</div>

<div class="source">Source: My own mistake (2026-01-27)</div>
'''

# =============================================================================
# Card 2: "fix point" → "mistakes/errors"
# =============================================================================
card2_q = '''
<b>英語添削カード</b><br><br>
次の文の間違いを直してください：<br><br>
<div class="formula">
"Could you tell me the <span class="important">fix point on</span> my english <span class="important">scentence</span> to get better?"
</div>
'''

card2_a = '''
<b>Corrected version:</b>
<div class="formula">
"Could you <span class="important">point out the mistakes in</span> my <span class="important">English sentences</span> so I can improve?"
</div>

<br>
<b>Errors & Corrections:</b>
<table>
<tr><th>Error</th><th>Correction</th><th>Explanation</th></tr>
<tr><td>fix point</td><td>mistakes / errors</td><td>「fix point」は不自然。"point out mistakes" が自然</td></tr>
<tr><td>on my</td><td>in my</td><td>文章の中のミス → 前置詞は "in"</td></tr>
<tr><td>english</td><td>English</td><td>言語名は大文字で始める</td></tr>
<tr><td>scentence</td><td>sentence</td><td>スペルミス（scent = 香り）</td></tr>
<tr><td>to get better</td><td>so I can improve</td><td>より自然な表現</td></tr>
</table>

<div class="example">
<b>Useful phrases:</b><br>
• "Could you correct my English?"<br>
• "Could you point out my mistakes?"<br>
• "What's wrong with this sentence?"
</div>

<div class="source">Source: My own mistake (2026-01-27)</div>
'''

# =============================================================================
# Add cards to deck
# =============================================================================
cards = [
    (card1_q, card1_a),
    (card2_q, card2_a),
]

for q, a in cards:
    note = genanki.Note(
        model=model,
        fields=[q, a]
    )
    deck.add_note(note)

# =============================================================================
# Generate .apkg file
# =============================================================================
output_file = '/Users/sasaki/english_corrections_verified.apkg'
genanki.Package(deck).write_to_file(output_file)
print(f"✅ Generated: {output_file}")
print(f"📚 Cards created: {len(cards)}")
