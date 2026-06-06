#!/usr/bin/env python3
"""
English Learning Anki Cards - Session 3
Expressions, Grammar, and Vocabulary
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

# Card CSS
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

DECK_NAME = "English Learning::03_Expressions_Grammar"
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
        "question": "<div class='question'>Which spelling is correct?</div><br>A) degital<br>B) digital<br>C) digitel<br>D) dijital",
        "answer": "<div class='correct'>B) digital</div><br><br>デジタルの<br><br><div class='example'>The digital rain effect is from The Matrix.</div>",
        "explanation": "dig-i-tal（3音節）。「digit」（数字）から派生。"
    },
    {
        "question": "<div class='question'>Which spelling is correct? (noun: 成功)</div><br>A) succsess<br>B) sucess<br>C) success<br>D) succses",
        "answer": "<div class='correct'>C) success</div><br><br>成功（名詞）<br><br><div class='example'>It was a success!</div>",
        "explanation": "suc-cess（2音節）。「cc」と「ss」の両方がある。"
    },
    {
        "question": "<div class='question'>Which spelling is correct? (adjective: 成功した)</div><br>A) succesful<br>B) successfull<br>C) successful<br>D) succesfull",
        "answer": "<div class='correct'>C) successful</div><br><br>成功した（形容詞）<br><br><div class='example'>It was successful thanks to your help.</div>",
        "explanation": "success + ful = successful。「l」は1つだけ。"
    },
    {
        "question": "<div class='question'>Which spelling is correct?</div><br>A) advence<br>B) advance<br>C) advanse<br>D) advanec",
        "answer": "<div class='correct'>B) advance</div><br><br>事前に、進める<br><br><div class='example'>Thank you in advance.</div>",
        "explanation": "ad-vance（2音節）。「advance」= 前に進む。"
    },
    {
        "question": "<div class='question'>Which spelling is correct?</div><br>A) randam<br>B) rondom<br>C) random<br>D) randome",
        "answer": "<div class='correct'>C) random</div><br><br>ランダムな、無作為の<br><br><div class='example'>Use a random number table for sampling.</div>",
        "explanation": "ran-dom（2音節）。「a」ではなく「o」：rand-o-m"
    },
    {
        "question": "<div class='question'>Which spelling is correct?</div><br>A) runnning<br>B) runing<br>C) running<br>D) running",
        "answer": "<div class='correct'>C) running</div><br><br>実行すること<br><br><div class='example'>I want to try running it in the terminal.</div>",
        "explanation": "run + n + ing = running。「n」は2つだけ（3つではない）。"
    },
    {
        "question": "<div class='question'>Which spelling is correct?</div><br>A) recieving<br>B) receving<br>C) receiving<br>D) recieivng",
        "answer": "<div class='correct'>C) receiving</div><br><br>受けること<br><br><div class='example'>When receiving a massage, say 'I'm in your hands.'</div>",
        "explanation": "receive → receiving。「i before e except after c」の例外！"
    },
    {
        "question": "<div class='question'>What's the difference?</div><br>A) raw<br>B) row",
        "answer": "<div class='correct'>raw = 生の<br>row = 行</div><br><br><div class='example'>raw data (生データ)<br>100 rows (100行)</div>",
        "explanation": "発音も意味も違う：raw [rɔː] 生の、row [roʊ] 行"
    },
]

# Grammar Cards
GRAMMAR_CARDS = [
    {
        "question": "<div class='question'>Fill in the blank:</div><br><br>It was successful _____ your help.<br><br>(あなたの助けのおかげで)",
        "answer": "<div class='correct'>thanks to</div><br><br><div class='example'>It was successful thanks to your help.</div>",
        "explanation": "「thanks to」= 〜のおかげで（原因を表す）"
    },
    {
        "question": "<div class='question'>Which is correct for expressing gratitude?</div><br><br>A) Thanks to your help!<br>B) Thank you for your help!",
        "answer": "<div class='correct'>B) Thank you for your help!</div><br><br><div class='wrong'>A) Thanks to your help! ✗ (原因を表す)</div>",
        "explanation": "感謝を表す = Thank you for。原因を表す = Thanks to"
    },
    {
        "question": "<div class='question'>Fill in the blank:</div><br><br>The digital rain _____ Japanese text from a sushi cookbook.<br><br>(〜にインスピレーションを受けた)",
        "answer": "<div class='correct'>was inspired by</div><br><br><div class='example'>The digital rain was inspired by Japanese text.</div>",
        "explanation": "「〜にインスピレーションを受けた」= was inspired by（受動態）"
    },
    {
        "question": "<div class='question'>Fill in the blank:</div><br><br>I feel _____ it's similar to scenes from The Matrix.<br><br>(〜のような気がする)",
        "answer": "<div class='correct'>like</div><br><br><div class='example'>I feel like it's similar to The Matrix.</div>",
        "explanation": "「〜のような気がする」= feel like + 節"
    },
    {
        "question": "<div class='question'>Fill in the blank:</div><br><br>I can't _____ the connection between sushi and digital rain.<br><br>(理解できない)",
        "answer": "<div class='correct'>figure out</div><br><br><div class='example'>I can't figure out the connection.</div>",
        "explanation": "「figure out」= 理解する、解明する"
    },
    {
        "question": "<div class='question'>Which is correct?</div><br><br>A) It's similar The Matrix.<br>B) It's similar to The Matrix.",
        "answer": "<div class='correct'>B) It's similar to The Matrix.</div><br><br><div class='wrong'>A) It's similar The Matrix. ✗</div>",
        "explanation": "「similar」の後には「to」が必要：similar to 〜"
    },
    {
        "question": "<div class='question'>Which is correct for a noun?</div><br><br>A) Is this a common phrase?<br>B) Is this a commonly phrase?",
        "answer": "<div class='correct'>A) Is this a common phrase?</div><br><br><div class='wrong'>B) commonly phrase ✗</div>",
        "explanation": "名詞の前は形容詞「common」。副詞「commonly」は動詞と使う。"
    },
]

# Expression Cards
EXPRESSION_CARDS = [
    {
        "question": "<div class='question'>How do you say 「お任せします」 when receiving a service (like a massage)?</div>",
        "answer": "<div class='correct'>I'm in your hands.</div><br><br>or: Thank you, I'm in your hands.",
        "explanation": "サービスを受ける前の「よろしくお願いします」の訳。信頼を伝える表現。"
    },
    {
        "question": "<div class='question'>What does 「in advance」 mean?</div>",
        "answer": "<div class='correct'>事前に / 前もって</div><br><br><div class='example'>Thank you in advance. (事前にありがとう)<br>Book in advance. (事前に予約する)</div>",
        "explanation": "何かが起こる「前に」という意味。ビジネスメールでよく使う。"
    },
    {
        "question": "<div class='question'>How do you say 「一緒に見てもらえますか？」</div>",
        "answer": "<div class='correct'>Could you follow along?</div><br><br>or: Could you follow along with my attempt?",
        "explanation": "誰かに自分の作業を見守ってほしい時に使う。"
    },
    {
        "question": "<div class='question'>What's the difference between these \"yoroshiku onegaishimasu\" translations?</div><br><br>Meeting someone vs Receiving a service",
        "answer": "<div class='correct'>Meeting: Nice to meet you.<br><br>Service: I'm in your hands.</div>",
        "explanation": "「よろしくお願いします」は文脈で訳が変わる。"
    },
]

# Vocabulary Cards
VOCABULARY_CARDS = [
    {
        "question": "<div class='question'>What is 「乱数表」 in English?</div>",
        "answer": "<div class='correct'>random number table</div><br><br><div class='example'>Use a random number table for random sampling.</div>",
        "explanation": "random = 無作為の、number = 数、table = 表"
    },
    {
        "question": "<div class='question'>What is 「行」 in English? (as in rows of a table)</div>",
        "answer": "<div class='correct'>row</div><br><br><div class='example'>The table has 100 rows and 5 columns.</div>",
        "explanation": "row = 行、column = 列。「raw」(生の) と間違えないように！"
    },
    {
        "question": "<div class='question'>What is 「列」 in English?</div>",
        "answer": "<div class='correct'>column</div><br><br><div class='example'>The table has 5 columns.</div>",
        "explanation": "column = 列、row = 行"
    },
    {
        "question": "<div class='question'>What is 「試み」 in English?</div>",
        "answer": "<div class='correct'>attempt</div><br><br><div class='example'>Could you follow along with my attempt?</div>",
        "explanation": "attempt = 試み、試行。「trying」は動詞形。"
    },
    {
        "question": "<div class='question'>What's the difference between shell mode and Python mode in Terminal?</div>",
        "answer": "<div class='correct'>Shell mode: % prompt<br>→ Run terminal commands (python3 script.py)<br><br>Python mode: >>> prompt<br>→ Type Python code only</div>",
        "explanation": "シェルモードでスクリプトを実行。Pythonモードではコードを直接入力。"
    },
]

def main():
    print("Creating English Learning Anki cards (Session 3)...")

    # Setup
    create_deck()
    create_model()

    # Add cards
    all_cards = SPELLING_CARDS + GRAMMAR_CARDS + EXPRESSION_CARDS + VOCABULARY_CARDS

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
