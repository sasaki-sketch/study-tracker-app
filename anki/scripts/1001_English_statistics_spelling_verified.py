#!/usr/bin/env python3
"""
English Learning Anki Cards - Statistics Vocabulary & Spelling
Generated from English learning session
"""

import requests
import json

ANKI_CONNECT_URL = "http://localhost:8765"

def invoke(action, **params):
    """Call AnkiConnect API"""
    request = {"action": action, "version": 6, "params": params}
    response = requests.post(ANKI_CONNECT_URL, json=request)
    return response.json()

# Card CSS (imported style)
CARD_CSS = """
/* Light Mode */
.card { font-family: "Hiragino Sans", "Yu Gothic", sans-serif; font-size: 18px; text-align: left; color: #333; background-color: #fff; padding: 20px; line-height: 1.6; }
.question { font-size: 20px; margin-bottom: 15px; }
.answer { font-size: 18px; margin-top: 15px; }
.source { font-size: 12px; color: #888; margin-top: 20px; padding-top: 10px; border-top: 1px solid #eee; }
.formula { background-color: #f0f4f8; padding: 15px; border-radius: 8px; margin: 10px 0; border: 1px solid #d0d7de; color: #1a1a1a; }
.important { color: #dc3545; font-weight: bold; }
.example { background-color: #d4edda; padding: 12px; border-radius: 8px; margin: 10px 0; border: 1px solid #28a745; color: #155724; }
.wrong { color: #dc3545; text-decoration: line-through; }
.correct { color: #28a745; font-weight: bold; }

/* Dark Mode */
.night_mode .card { background-color: #1e1e1e; color: #e0e0e0; }
.night_mode .source { color: #a0aec0; border-top-color: #4a5568; }
.night_mode .formula { background-color: #2d3748; border: 1px solid #4a5568; color: #f7fafc; }
.night_mode .important { color: #fc8181; }
.night_mode .example { background-color: #1a4731; border: 1px solid #2f855a; color: #c6f6d5; }
.night_mode .wrong { color: #fc8181; }
.night_mode .correct { color: #68d391; }
"""

DECK_NAME = "English Learning::01_Statistics_Vocabulary"
MODEL_NAME = "English Learning - Spelling"

def create_model():
    """Create note type if it doesn't exist"""
    models = invoke("modelNames")
    if MODEL_NAME not in models.get("result", []):
        invoke("createModel",
            modelName=MODEL_NAME,
            inOrderFields=["Question", "Answer", "Explanation"],
            css=CARD_CSS,
            cardTemplates=[{
                "Name": "Card 1",
                "Front": "{{Question}}",
                "Back": "{{FrontSide}}<hr id='answer'>{{Answer}}<br><br><div class='source'>{{Explanation}}</div>"
            }]
        )
        print(f"Created model: {MODEL_NAME}")

def create_deck():
    """Create deck if it doesn't exist"""
    invoke("createDeck", deck=DECK_NAME)
    print(f"Created/verified deck: {DECK_NAME}")

def add_note(question, answer, explanation):
    """Add a single note to Anki"""
    note = {
        "deckName": DECK_NAME,
        "modelName": MODEL_NAME,
        "fields": {
            "Question": question,
            "Answer": answer,
            "Explanation": explanation
        },
        "options": {"allowDuplicate": False}
    }
    result = invoke("addNote", note=note)
    return result

# Spelling Cards
SPELLING_CARDS = [
    {
        "question": "<div class='question'>Which spelling is correct?</div><br>A) statiscal<br>B) statistcal<br>C) statistical<br>D) statisticle",
        "answer": "<div class='correct'>C) statistical</div><br><br>統計的な<br><br><div class='example'>Statistical analysis is important for research.</div>",
        "explanation": "sta-tis-ti-cal（4音節）。statistics（統計学）の形容詞形。"
    },
    {
        "question": "<div class='question'>Which spelling is correct?</div><br>A) distiribution<br>B) distribution<br>C) distrubution<br>D) distribusion",
        "answer": "<div class='correct'>B) distribution</div><br><br>分布<br><br><div class='example'>The normal distribution is symmetric around the mean.</div>",
        "explanation": "dis-tri-bu-tion（4音節）。distribute（分配する）の名詞形。"
    },
    {
        "question": "<div class='question'>Which spelling is correct?</div><br>A) mathmetical<br>B) mathmatical<br>C) mathematical<br>D) mathematicle",
        "answer": "<div class='correct'>C) mathematical</div><br><br>数学的な<br><br><div class='example'>A probability distribution is a mathematical function.</div>",
        "explanation": "math-e-mat-i-cal（5音節）。mathematics（数学）の形容詞形。「e」を忘れずに！"
    },
    {
        "question": "<div class='question'>Which spelling is correct?</div><br>A) descirbes<br>B) discribes<br>C) describs<br>D) describes",
        "answer": "<div class='correct'>D) describes</div><br><br>記述する<br><br><div class='example'>This function describes the relationship between variables.</div>",
        "explanation": "de-scribes（2音節）。scribe（書く人）から派生。"
    },
    {
        "question": "<div class='question'>Which spelling is correct?</div><br>A) grammer<br>B) gramar<br>C) grammar<br>D) gramer",
        "answer": "<div class='correct'>C) grammar</div><br><br>文法<br><br><div class='example'>English grammar can be difficult to learn.</div>",
        "explanation": "gramm-ar。「a」が2回出てくる：gr-a-mm-a-r"
    },
    {
        "question": "<div class='question'>Which spelling is correct?</div><br>A) difinition<br>B) defination<br>C) definision<br>D) definition",
        "answer": "<div class='correct'>D) definition</div><br><br>定義<br><br><div class='example'>The definition of probability is important to understand.</div>",
        "explanation": "def-i-ni-tion（4音節）。define（定義する）の名詞形。"
    },
    {
        "question": "<div class='question'>Which spelling is correct?</div><br>A) sentenses<br>B) sentenes<br>C) sentences<br>D) centences",
        "answer": "<div class='correct'>C) sentences</div><br><br>文<br><br><div class='example'>I'm getting used to making English sentences.</div>",
        "explanation": "sen-ten-ces（3音節）。「c」を忘れずに！"
    },
    {
        "question": "<div class='question'>Which spelling is correct?</div><br>A) specifical<br>B) spesific<br>C) specific<br>D) spacific",
        "answer": "<div class='correct'>C) specific</div><br><br>特定の<br><br><div class='example'>I want to learn specific statistical terms.</div>",
        "explanation": "spe-cif-ic（3音節）。「specifical」という単語は存在しない！"
    },
]

# Grammar Cards
GRAMMAR_CARDS = [
    {
        "question": "<div class='question'>Fill in the blank:</div><br><br>I'm _____ making English sentences.<br><br>(慣れてきている)",
        "answer": "<div class='correct'>getting used to</div><br><br><div class='example'>I'm getting used to making English sentences.</div>",
        "explanation": "「慣れてきている」= getting used to + -ing。進行中の変化を表す。"
    },
    {
        "question": "<div class='question'>Fill in the blank:</div><br><br>I'm _____ making English sentences.<br><br>(慣れている)",
        "answer": "<div class='correct'>used to</div><br><br><div class='example'>I'm used to making English sentences.</div>",
        "explanation": "「慣れている」= be used to + -ing。すでに慣れた状態を表す。"
    },
    {
        "question": "<div class='question'>Which is correct?</div><br><br>A) I'm used to make sentences.<br>B) I'm used to making sentences.",
        "answer": "<div class='correct'>B) I'm used to making sentences.</div><br><br><div class='wrong'>A) I'm used to make sentences. ✗</div>",
        "explanation": "「be used to」の後は動名詞（-ing）。この「to」は前置詞なので、動名詞が続く。"
    },
    {
        "question": "<div class='question'>What does this reduced form expand to?</div><br><br>\"...likelihood, <b>expressed</b> as a value between 0 and 1\"",
        "answer": "<div class='correct'>...likelihood, <b>which is expressed</b> as a value between 0 and 1</div>",
        "explanation": "過去分詞句（Past participle phrase）。「which is」を省略した形。学術論文でよく使われる。"
    },
    {
        "question": "<div class='question'>Fill in the blank:</div><br><br>I'm _____ learn statistics.<br><br>(学ぼうとしている)",
        "answer": "<div class='correct'>trying to</div><br><br><div class='example'>I'm trying to learn statistics.</div>",
        "explanation": "「〜しようとしている」= be trying to + 動詞の原形"
    },
]

# Vocabulary Cards
VOCABULARY_CARDS = [
    {
        "question": "<div class='question'>What's the correct verb for keyboard keys?</div><br><br>_____ a key<br><br>(キーを押す)",
        "answer": "<div class='correct'>press</div><br><br><div class='example'>Press Enter to submit.</div><br><br><div class='wrong'>put a key ✗</div>",
        "explanation": "キーボードのキーには「press」を使う。「put」は使わない。"
    },
    {
        "question": "<div class='question'>What's the correct verb for mouse buttons?</div><br><br>_____ a button<br><br>(ボタンをクリックする)",
        "answer": "<div class='correct'>click</div><br><br><div class='example'>Click the button to confirm.</div>",
        "explanation": "マウスボタンには「click」を使う。"
    },
    {
        "question": "<div class='question'>How do you say \"効かなかった\" in English?</div>",
        "answer": "<div class='correct'>It didn't work.</div><br><br><div class='example'>I tried to press Shift+Enter, but it didn't work.</div>",
        "explanation": "「効かない・動かない」= doesn't work / didn't work"
    },
    {
        "question": "<div class='question'>What is \"確率\" in English?</div>",
        "answer": "<div class='correct'>probability</div><br><br><div class='formula'>\\(P(A) = \\frac{\\text{favorable outcomes}}{\\text{total outcomes}}\\)</div>",
        "explanation": "probability = 確率。0から1の間の値で表される。"
    },
    {
        "question": "<div class='question'>What is \"確率分布\" in English?</div>",
        "answer": "<div class='correct'>probability distribution</div><br><br><div class='example'>A probability distribution is a mathematical function that describes all possible values of a random variable.</div>",
        "explanation": "probability distribution = 確率分布。確率変数の取りうる値とその確率を記述する関数。"
    },
]

# Punctuation Cards
PUNCTUATION_CARDS = [
    {
        "question": "<div class='question'>Which punctuation is correct?</div><br><br>A) Yes,I got it.<br>B) Yes, I got it.",
        "answer": "<div class='correct'>B) Yes, I got it.</div><br><br><div class='wrong'>A) Yes,I got it. ✗</div>",
        "explanation": "カンマの後には必ずスペースを入れる。"
    },
    {
        "question": "<div class='question'>Which punctuation is correct?</div><br><br>A) I like coffee, Do you like tea?<br>B) I like coffee. Do you like tea?",
        "answer": "<div class='correct'>B) I like coffee. Do you like tea?</div><br><br><div class='wrong'>A) I like coffee, Do you like tea? ✗</div>",
        "explanation": "2つの独立した文はピリオドで区切る。カンマ＋大文字は使わない。"
    },
]

def main():
    print("Creating English Learning Anki cards...")

    # Setup
    create_deck()
    create_model()

    # Add cards
    all_cards = SPELLING_CARDS + GRAMMAR_CARDS + VOCABULARY_CARDS + PUNCTUATION_CARDS

    success_count = 0
    for card in all_cards:
        result = add_note(card["question"], card["answer"], card["explanation"])
        if result.get("error") is None:
            success_count += 1
            print(f"✓ Added card")
        else:
            print(f"✗ Failed: {result.get('error')}")

    print(f"\nCompleted: {success_count}/{len(all_cards)} cards added to '{DECK_NAME}'")

if __name__ == "__main__":
    main()
