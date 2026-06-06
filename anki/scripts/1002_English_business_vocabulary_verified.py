#!/usr/bin/env python3
"""
English Learning Anki Cards - Business Vocabulary & Session 2
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

DECK_NAME = "English Learning::02_Business_Vocabulary"
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

# Spelling Cards - Session 2
SPELLING_CARDS = [
    {
        "question": "<div class='question'>Which spelling is correct?</div><br>A) bressret<br>B) brresret<br>C) bracelet<br>D) braselet",
        "answer": "<div class='correct'>C) bracelet</div><br><br>ブレスレット<br><br><div class='example'>Handmade bracelets are popular among overseas customers.</div>",
        "explanation": "brace-let（2音節）。「brace」（支える）+ 「let」（小さいもの）"
    },
    {
        "question": "<div class='question'>Which spelling is correct?</div><br>A) offcial<br>B) oficial<br>C) official<br>D) officel",
        "answer": "<div class='correct'>C) official</div><br><br>公式の<br><br><div class='example'>Can we get official bracelet size data?</div>",
        "explanation": "of-fi-cial（3音節）。「f」が2つ：of<b>fi</b>cial"
    },
    {
        "question": "<div class='question'>Which spelling is correct?</div><br>A) marge<br>B) merg<br>C) murge<br>D) merge",
        "answer": "<div class='correct'>D) merge</div><br><br>合併する・統合する<br><br><div class='example'>We can merge official data with our purchasing data.</div>",
        "explanation": "merge（1音節）。「marge」ではなく「merge」（e-r-g-e）"
    },
    {
        "question": "<div class='question'>Which spelling is correct?</div><br>A) frecuency<br>B) frequency<br>C) frequensy<br>D) frequancy",
        "answer": "<div class='correct'>B) frequency</div><br><br>頻度<br><br><div class='example'>I analyze customers' buying frequency.</div>",
        "explanation": "fre-quen-cy（3音節）。「qu」の後は「e」：freq<b>ue</b>ncy"
    },
    {
        "question": "<div class='question'>Which spelling is correct?</div><br>A) costomer<br>B) customar<br>C) customer<br>D) custmer",
        "answer": "<div class='correct'>C) customer</div><br><br>顧客<br><br><div class='example'>We serve overseas customers.</div>",
        "explanation": "cust-o-mer（3音節）。c<b>u</b>stomer（「o」ではなく「u」）"
    },
    {
        "question": "<div class='question'>Which spelling is correct?</div><br>A) analize<br>B) analyse<br>C) analise<br>D) analyze",
        "answer": "<div class='correct'>D) analyze (US) / B) analyse (UK)</div><br><br>分析する<br><br><div class='example'>I want to analyze customer preferences.</div>",
        "explanation": "アメリカ英語：analyze、イギリス英語：analyse。「analize」は間違い。"
    },
    {
        "question": "<div class='question'>Which spelling is correct?</div><br>A) usualy<br>B) usally<br>C) usually<br>D) ussually",
        "answer": "<div class='correct'>C) usually</div><br><br>通常<br><br><div class='example'>Usually, I analyze customers' buying frequency.</div>",
        "explanation": "usu-al-ly（3音節）。「l」が2つ：usua<b>ll</b>y"
    },
    {
        "question": "<div class='question'>Which spelling is correct?</div><br>A) handmad<br>B) handmade<br>C) hand-maid<br>D) handmaid",
        "answer": "<div class='correct'>B) handmade</div><br><br>ハンドメイドの・手作りの<br><br><div class='example'>Handmade bracelets may take many days to make.</div>",
        "explanation": "hand + made = handmade（1語）。「handmaid」は「侍女」という別の意味。"
    },
]

# Grammar Cards - Session 2
GRAMMAR_CARDS = [
    {
        "question": "<div class='question'>Fill in the blank:</div><br><br>I _____ a buying agency.<br><br>(〜に所属している)",
        "answer": "<div class='correct'>belong to</div><br><br><div class='example'>I belong to a buying agency that serves overseas customers.</div>",
        "explanation": "「belong」は必ず「to」と一緒に使う。belong to = 〜に所属している"
    },
    {
        "question": "<div class='question'>Fill in the blank:</div><br><br>We can _____ official data _____ our purchasing data.<br><br>(公式データと購買データを統合する)",
        "answer": "<div class='correct'>merge ... with</div><br><br><div class='example'>We can merge official data with our purchasing data.</div>",
        "explanation": "merge A with B = AとBを統合する"
    },
    {
        "question": "<div class='question'>Which is correct?</div><br><br>A) If we could get data, the precision will improve.<br>B) If we could get data, the precision would improve.",
        "answer": "<div class='correct'>B) If we could get data, the precision would improve.</div><br><br><div class='wrong'>A) will improve ✗</div>",
        "explanation": "仮定法過去：If + 過去形, would + 動詞の原形。「could」があるので「would」を使う。"
    },
    {
        "question": "<div class='question'>Which is correct?</div><br><br>A) What do you think about?<br>B) What do you think?",
        "answer": "<div class='correct'>B) What do you think?</div><br><br><div class='wrong'>A) What do you think about? ✗</div>",
        "explanation": "「about」の後には目的語が必要。単独で意見を求めるなら「What do you think?」"
    },
    {
        "question": "<div class='question'>Fill in the blank:</div><br><br>What do you think _____ my idea?<br><br>(私のアイデアについてどう思いますか？)",
        "answer": "<div class='correct'>about</div><br><br><div class='example'>What do you think about my idea?</div>",
        "explanation": "「about」の後に目的語がある場合は使える：What do you think about X?"
    },
    {
        "question": "<div class='question'>Which is correct for a noun?</div><br><br>A) My job is data analyzing.<br>B) My job is data analysis.",
        "answer": "<div class='correct'>B) My job is data analysis.</div><br><br><div class='wrong'>A) data analyzing ✗</div>",
        "explanation": "名詞として使う場合は「analysis」。動詞は「analyze」。"
    },
]

# Vocabulary Cards - Session 2
VOCABULARY_CARDS = [
    {
        "question": "<div class='question'>What is \"購買代行\" in English?</div>",
        "answer": "<div class='correct'>buying agency / purchasing agency</div><br><br><div class='example'>I belong to a buying agency that serves overseas customers.</div>",
        "explanation": "buying agency = purchasing agency = 購買代行"
    },
    {
        "question": "<div class='question'>What is \"購買データ\" in English?</div>",
        "answer": "<div class='correct'>purchasing data / buying data</div><br><br><div class='example'>We have a lot of purchasing data.</div>",
        "explanation": "purchasing data = buying data = 購買データ"
    },
    {
        "question": "<div class='question'>What is \"海外顧客\" in English?</div>",
        "answer": "<div class='correct'>overseas customers</div><br><br><div class='example'>We serve overseas customers purchasing from Japanese EC sites.</div>",
        "explanation": "overseas = 海外の（1語）。「oversea」ではなく「overseas」"
    },
    {
        "question": "<div class='question'>What is \"精度\" in English?</div>",
        "answer": "<div class='correct'>precision</div><br><br><div class='example'>The precision would improve if we merged the data.</div>",
        "explanation": "precision = 精度、正確さ"
    },
    {
        "question": "<div class='question'>What is \"説得力のある\" in English?</div>",
        "answer": "<div class='correct'>convincing</div><br><br><div class='example'>The analysis would become more convincing.</div>",
        "explanation": "convincing = 説得力のある、納得させる"
    },
    {
        "question": "<div class='question'>What is \"公式データ\" in English?</div>",
        "answer": "<div class='correct'>official data</div><br><br><div class='example'>Can we get official bracelet size data?</div>",
        "explanation": "official = 公式の。「f」が2つ：official"
    },
    {
        "question": "<div class='question'>What is \"確率分布\" in English?</div>",
        "answer": "<div class='correct'>probability distribution</div><br><br><div class='example'>I want to analyze the probability distribution of bracelet sizes by region.</div>",
        "explanation": "probability = 確率、distribution = 分布"
    },
    {
        "question": "<div class='question'>What does \"merge\" mean?</div>",
        "answer": "<div class='correct'>合併する・統合する</div><br><br><div class='example'>We can merge official data with our purchasing data.</div>",
        "explanation": "merge A with B = AとBを統合する。スペル注意：「marge」ではない"
    },
]

# Expression Cards
EXPRESSION_CARDS = [
    {
        "question": "<div class='question'>How do you say \"アイデアを思いついた\" in English?</div>",
        "answer": "<div class='correct'>I came up with an idea.</div><br><br>Other options:<br>• I had an idea.<br>• An idea occurred to me.",
        "explanation": "come up with = 思いつく。「I hit the idea」は不自然。"
    },
    {
        "question": "<div class='question'>How do you say \"時間がかかる\" for a task?</div><br><br>Handmade bracelets _____ many days to make.",
        "answer": "<div class='correct'>take</div><br><br><div class='example'>Handmade bracelets may take many days to make.</div>",
        "explanation": "時間がかかる = take time。「spend」は人が主語の時に使う。"
    },
]

def main():
    print("Creating English Learning Anki cards (Session 2)...")

    # Setup
    create_deck()
    create_model()

    # Add cards
    all_cards = SPELLING_CARDS + GRAMMAR_CARDS + VOCABULARY_CARDS + EXPRESSION_CARDS

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
