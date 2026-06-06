#!/usr/bin/env python3
"""
English Grammar and Expressions Anki Cards
英語文法・表現 Ankiカード

Topic: Common grammar patterns and expressions
Deck: English Learning (existing deck)
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# Model ID and Deck ID (unique random numbers)
MODEL_ID = 1701100001
DECK_ID = 1701100002

# Create model
english_model = genanki.Model(
    MODEL_ID,
    'English Grammar Model',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
        {'name': 'Source'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '<div class="question">{{Question}}</div>',
            'afmt': '''{{FrontSide}}<hr id="answer"><div class="answer">{{Answer}}</div>
            <div class="source">{{Source}}</div>''',
        },
    ],
    css=CARD_CSS
)

# Create deck (using existing "English Learning" deck)
deck = genanki.Deck(DECK_ID, 'English Learning')

# Cards data
cards = [
    # === SPELLING CARDS ===
    {
        'question': '''<b>Spelling Check</b><br><br>
Which is correct?<br>
A) leaning statistics<br>
B) learning statistics''',
        'answer': '''<div class="formula"><b>B) learning statistics</b></div>
<div class="example">
<b>leaning</b> = 傾く、もたれる (lean の現在分詞)<br>
<b>learning</b> = 学ぶ (learn の現在分詞)
</div>
<b>Example:</b> I'm learning statistics from this book.<br>
(私はこの本から統計学を学んでいます。)''',
        'source': 'English Learning Session 2026-01-31'
    },
    {
        'question': '''<b>Spelling Check</b><br><br>
Which is correct?<br>
A) scentences<br>
B) sentenses<br>
C) sentences''',
        'answer': '''<div class="formula"><b>C) sentences</b></div>
<div class="mnemonic">
覚え方: <b>sen-ten-ces</b> (3音節)
</div>
<b>Example:</b> I practice writing English sentences every day.<br>
(私は毎日英語の文を書く練習をしています。)''',
        'source': 'English Learning Session 2026-01-31'
    },
    {
        'question': '''<b>Spelling Check</b><br><br>
Which is correct?<br>
A) differency<br>
B) difference<br>
C) differance''',
        'answer': '''<div class="formula"><b>B) difference</b></div>
<div class="mnemonic">
覚え方: differ + <b>ence</b> (名詞の接尾辞)
</div>
<b>Example:</b> What's the difference between A and B?<br>
(AとBの違いは何ですか？)''',
        'source': 'English Learning Session 2026-01-31'
    },
    {
        'question': '''<b>Spelling Check</b><br><br>
Which is correct?<br>
A) difinition<br>
B) defenition<br>
C) definition''',
        'answer': '''<div class="formula"><b>C) definition</b></div>
<div class="mnemonic">
覚え方: <b>de-fi-ni-tion</b> (4音節)
</div>
<b>Example:</b> Could you explain the definition of this term?<br>
(この用語の定義を説明してもらえますか？)''',
        'source': 'English Learning Session 2026-01-31'
    },
    {
        'question': '''<b>Spelling Check</b><br><br>
Which is correct?<br>
A) contemts<br>
B) contents<br>
C) contants''',
        'answer': '''<div class="formula"><b>B) contents</b></div>
<div class="mnemonic">
覚え方: <b>con-tents</b> (2音節) - "tent"(テント)が入っている
</div>
<b>Example:</b> I pasted the table of contents.<br>
(目次を貼り付けました。)''',
        'source': 'English Learning Session 2026-01-31'
    },

    # === GRAMMAR PATTERN CARDS ===
    {
        'question': '''<b>Grammar Pattern</b><br><br>
Fill in the blank:<br><br>
"I'm not used to _____ English sentences."<br>
(make)''',
        'answer': '''<div class="formula"><b>making</b></div>
<div class="example">
<b>Pattern:</b> be used to + 動名詞 (~ing)<br>
意味: 〜することに慣れている
</div>
<span class="important">注意:</span> "used to + 動詞原形" (以前は〜だった) と混同しない！<br><br>
<b>Comparison:</b><br>
• I'm used to <b>waking</b> up early. (早起きに慣れている)<br>
• I used to <b>wake</b> up early. (以前は早起きだった)''',
        'source': 'English Learning Session 2026-01-31'
    },
    {
        'question': '''<b>Grammar Pattern</b><br><br>
Which is correct?<br><br>
A) I have finish my homework.<br>
B) I have finished my homework.<br>
C) I have finishes my homework.''',
        'answer': '''<div class="formula"><b>B) I have finished my homework.</b></div>
<div class="example">
<b>Pattern:</b> have/has + 過去分詞<br>
(現在完了形 - Present Perfect)
</div>
<b>Examples:</b><br>
• I have <b>learned</b> a lot today. (今日たくさん学んだ)<br>
• She has <b>written</b> three emails. (彼女は3通のメールを書いた)<br>
• They have <b>finished</b> the project. (彼らはプロジェクトを終えた)''',
        'source': 'English Learning Session 2026-01-31'
    },

    # === PREPOSITION CARDS ===
    {
        'question': '''<b>Preposition</b><br><br>
Fill in the blank:<br><br>
"What's the difference _____ A and B?"''',
        'answer': '''<div class="formula"><b>between</b></div>
<div class="example">
<b>Pattern:</b> difference <b>between</b> A and B<br>
意味: AとBの違い
</div>
<span class="important">注意:</span> "difference of" は間違い！<br><br>
<b>Example:</b> What's the difference between "I want to" and "I'd like to"?<br>
(「I want to」と「I'd like to」の違いは何ですか？)''',
        'source': 'English Learning Session 2026-01-31'
    },
    {
        'question': '''<b>Preposition</b><br><br>
Fill in the blank:<br><br>
"I learned statistics _____ this book."''',
        'answer': '''<div class="formula"><b>from</b></div>
<div class="example">
<b>Pattern:</b> learn <b>from</b> ~<br>
意味: 〜から学ぶ
</div>
<b>Examples:</b><br>
• I learned English <b>from</b> watching movies. (映画を見て英語を学んだ)<br>
• We can learn <b>from</b> our mistakes. (失敗から学べる)''',
        'source': 'English Learning Session 2026-01-31'
    },
    {
        'question': '''<b>Preposition</b><br><br>
Fill in the blank:<br><br>
"Could you comment _____ my sentence?"''',
        'answer': '''<div class="formula"><b>on</b></div>
<div class="example">
<b>Pattern:</b> comment <b>on</b> ~<br>
意味: 〜についてコメントする
</div>
<b>Similar patterns:</b> (同じパターン)<br>
• focus <b>on</b> ~ (〜に集中する)<br>
• work <b>on</b> ~ (〜に取り組む)<br>
• depend <b>on</b> ~ (〜に依存する)''',
        'source': 'English Learning Session 2026-01-31'
    },
    {
        'question': '''<b>Preposition</b><br><br>
Fill in the blank:<br><br>
"Let's start _____ Chapter 1."''',
        'answer': '''<div class="formula"><b>with</b></div>
<div class="example">
<b>Pattern:</b> start <b>with</b> ~<br>
意味: 〜から始める
</div>
<span class="important">注意:</span> "start by" は「〜することで始める」(方法)<br><br>
<b>Comparison:</b><br>
• Let's start <b>with</b> the basics. (基礎から始めよう) - 対象<br>
• Let's start <b>by</b> reading the manual. (マニュアルを読むことから始めよう) - 方法''',
        'source': 'English Learning Session 2026-01-31'
    },

    # === QUESTION PATTERN CARDS ===
    {
        'question': '''<b>Question Pattern</b><br><br>
Which is correct?<br><br>
A) Have I reopen the Terminal?<br>
B) Do I need to reopen the Terminal?''',
        'answer': '''<div class="formula"><b>B) Do I need to reopen the Terminal?</b></div>
<div class="example">
<b>Pattern:</b> Do I need to + 動詞原形?<br>
意味: 〜する必要がありますか？
</div>
<b>Examples:</b><br>
• Do I need to restart the computer? (コンピュータを再起動する必要がありますか？)<br>
• Do I need to install anything? (何かインストールする必要がありますか？)<br>
• Do I need to sign up first? (最初に登録する必要がありますか？)''',
        'source': 'English Learning Session 2026-01-31'
    },

    # === EXPRESSION CARDS ===
    {
        'question': '''<b>Polite Expression</b><br><br>
Which is more polite?<br><br>
A) I want to ask a question.<br>
B) I'd like to ask a question.''',
        'answer': '''<div class="formula"><b>B) I'd like to ask a question.</b></div>
<div class="example">
<b>I want to</b> = 直接的、カジュアル (Direct, Casual)<br>
<b>I'd like to</b> = 丁寧、フォーマル (Polite, Formal)
</div>
<b>When to use:</b> (使い分け)<br>
• レストランで → I'd like to order... (丁寧)<br>
• 友達と → I want to go home. (カジュアルでOK)<br>
• 仕事・初対面 → I'd like to ask... (丁寧)<br><br>
<div class="mnemonic">
ルール: 迷ったら "I'd like to" を使えば失礼にならない！
</div>''',
        'source': 'English Learning Session 2026-01-31'
    },
    {
        'question': '''<b>Formal Writing</b><br><br>
Which is better at the beginning of a sentence?<br><br>
A) And, I want to know...<br>
B) Also, I want to know...''',
        'answer': '''<div class="formula"><b>B) Also, I want to know...</b></div>
<div class="example">
<b>And</b> = カジュアル、文頭では避ける<br>
<b>Also</b> = フォーマル、文頭でOK
</div>
<b>Alternatives for "And":</b> (Andの代わりに使える表現)<br>
• Also, ... (また)<br>
• In addition, ... (さらに)<br>
• Furthermore, ... (その上)<br>
• Moreover, ... (さらに)''',
        'source': 'English Learning Session 2026-01-31'
    },
]

# Add cards to deck
for card in cards:
    note = genanki.Note(
        model=english_model,
        fields=[card['question'], card['answer'], card['source']]
    )
    deck.add_note(note)

# Generate package
output_path = '/Users/sasaki/study_app/anki/scripts/1001_English_Grammar_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
print(f"Total cards: {len(cards)}")
