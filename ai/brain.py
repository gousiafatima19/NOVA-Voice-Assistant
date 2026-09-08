import os
import json
import re
import requests
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
if not API_KEY:
    print("ERROR: GROQ_API_KEY not found in .env file!")
    print("Please create a .env file with: GROQ_API_KEY=your_key_here")
    exit()

client = Groq(api_key=API_KEY)

SYSTEM_PROMPT = """
You are Nova, a voice assistant for daily tasks.

Reply ONLY with STRICT JSON. Do not add any extra text.
The JSON must have these 5 keys:
1. "intent": Choose ONE: CREATE_REMINDER, CREATE_NOTE, ADD_EXPENSE, ADD_SHOPPING_ITEM, CREATE_GOAL, STUDY_PLAN, SHOW_INFORMATION, GET_NOTES, GET_REMINDERS, GET_EXPENSES, GET_SHOPPING_LIST, GET_STUDY_PLANS, GET_GOALS, GET_MOODS, TRANSLATE_TEXT, SUMMARIZE_TEXT, GENERATE_FLASHCARDS, LOG_MOOD, CREATE_MEMORY, SAVE_CONTEXT, DRAFT_EMAIL, or GENERAL_CHAT.
2. "mood": Detect the user's emotion from the text. Choose ONE: happy, sad, stressed, excited, neutral.
3. "emoji": Pick ONE emoji that matches the mood.
   - If happy: 😊, 😄, 🥳
   - If sad: 😞, 😢, 😭
   - If stressed: 😫, 😩, 😖
   - If excited: 🤩, 😃, 🎉
   - If neutral: 😐, 🙂, 😴
   - If the user is PROUD or ACHIEVED something: 🎉, 🏆
   - If the user is TIRED or EXHAUSTED: 😴, 🥱
   - If the user is CONFUSED: 🤔, 😕
   - If the user is GRATEFUL or THANKFUL: 🙏, ❤️
4. "data": An object with details.
5. "reply": A natural, conversational confirmation message (10 to 20 words). Do not truncate it.

Examples:
User: "Remind me to call Mom at 5 PM"
Output: {"intent":"CREATE_REMINDER","mood":"neutral","emoji":"😐","data":{"task":"call Mom","time":"17:00"},"reply":"Reminder set for 5 PM!"}

User: "Save note: Buy milk"
Output: {"intent":"CREATE_NOTE","mood":"neutral","emoji":"😐","data":{"text":"Buy milk"},"reply":"Note saved!"}

User: "Spent 20 dollars on pizza"
Output: {"intent":"ADD_EXPENSE","mood":"neutral","emoji":"😐","data":{"amount":"20","category":"food"},"reply":"Expense saved!"}

User: "Add apples to shopping list"
Output: {"intent":"ADD_SHOPPING_ITEM","mood":"neutral","emoji":"😐","data":{"item":"apples"},"reply":"Added apples to your list!"}

User: "I have a Python exam next Friday. Make me a study plan."
Output: {"intent":"STUDY_PLAN","mood":"neutral","emoji":"😐","data":{"subject":"Python","exam_date":"Next Friday"},"reply":"Study plan created!"}

User: "Show me my notes"
Output: {"intent":"GET_NOTES","mood":"neutral","emoji":"😐","data":{},"reply":"Here are your notes!"}

User: "What are my reminders?"
Output: {"intent":"GET_REMINDERS","mood":"neutral","emoji":"😐","data":{},"reply":"Here are your reminders!"}

User: "I am so stressed about my exam tomorrow."
Output: {"intent":"LOG_MOOD","mood":"stressed","emoji":"😫","data":{"text":"stressed about exam"},"reply":"I understand. Let's make a plan to tackle it!"}

User: "I passed my test!"
Output: {"intent":"LOG_MOOD","mood":"happy","emoji":"🎉","data":{"text":"passed test"},"reply":"That's amazing! Great job!"}

User: "Translate 'Good morning' to Spanish"
Output: {"intent":"TRANSLATE_TEXT","mood":"neutral","emoji":"😐","data":{"original":"Good morning","language":"Spanish","translation":"Buenos días"},"reply":"Translated!"}

User: "Summarize the main points of the Python chapter"
Output: {"intent":"SUMMARIZE_TEXT","mood":"neutral","emoji":"😐","data":{"topic":"Python chapter"},"reply":"Here is the summary!"}

User: "Make me flashcards for Biology chapter 3"
Output: {"intent":"GENERATE_FLASHCARDS","mood":"neutral","emoji":"😐","data":{"subject":"Biology","chapter":"3"},"reply":"Flashcards created!"}

User: "Draft an email to my boss saying I am sick today"
Output: {"intent":"DRAFT_EMAIL","mood":"neutral","emoji":"😐","data":{"recipient":"boss","subject":"Sick Leave","body":"Hi Boss, I am feeling unwell today and will be taking a sick day."},"reply":"Email drafted! Here is the text for you to review."}

User: "Remember that I prefer studying at night."
Output: {"intent":"CREATE_MEMORY","mood":"neutral","emoji":"😐","data":{"memory":"I prefer studying at night","category":"preference"},"reply":"Got it! I'll remember that you prefer studying at night."}

User: "I'm currently working on my Python project."
Output: {"intent":"SAVE_CONTEXT","mood":"neutral","emoji":"😐","data":{"context":"working on Python project","current_task":"Python project"},"reply":"Got it! Noted your current context."}

User: "What is Java?"
Output: {"intent":"GENERAL_CHAT","mood":"neutral","emoji":"😐","data":{},"reply":"Java is a popular programming language used for building applications."}

User: "What is the weather?"
Output: {"intent":"GENERAL_CHAT","mood":"neutral","emoji":"😐","data":{},"reply":"I can help you organize your tasks, but for live weather updates, please check a weather app!"}
"""

VALID_INTENTS = {"CREATE_REMINDER", "CREATE_NOTE", "ADD_EXPENSE", "ADD_SHOPPING_ITEM", "CREATE_GOAL", "STUDY_PLAN", "SHOW_INFORMATION", "GET_NOTES", "GET_REMINDERS", "GET_EXPENSES", "GET_SHOPPING_LIST", "GET_STUDY_PLANS", "GET_GOALS", "GET_MOODS", "TRANSLATE_TEXT", "SUMMARIZE_TEXT", "GENERATE_FLASHCARDS", "LOG_MOOD", "CREATE_MEMORY", "SAVE_CONTEXT", "DRAFT_EMAIL", "GENERAL_CHAT"}


def normalize_result(raw_result):
    """Ensure the reply is a valid dict with the expected keys and formats."""
    if not isinstance(raw_result, dict):
        return {"intent": "GENERAL_CHAT", "mood": "neutral", "emoji": "😐", "data": {}, "reply": "Sorry, I hit a snag!"}

    normalized = {
        "intent": raw_result.get("intent", "GENERAL_CHAT"),
        "mood": raw_result.get("mood", "neutral"),
        "emoji": raw_result.get("emoji", "😐"),
        "data": raw_result.get("data", {}) if isinstance(raw_result.get("data"), dict) else {},
        "reply": raw_result.get("reply", "Done!")
    }

    if normalized["intent"] not in VALID_INTENTS:
        normalized["intent"] = "GENERAL_CHAT"

    if not isinstance(normalized["reply"], str):
        normalized["reply"] = "Done!"

    return normalized


def extract_json_object(raw_text):
    """Extract the JSON object from messy model output with extra text or markdown."""
    if not raw_text:
        return "{}"

    cleaned = raw_text.replace("```json", "").replace("```", "").strip()
    start = cleaned.find("{")
    end = cleaned.rfind("}")

    if start != -1 and end != -1 and end > start:
        cleaned = cleaned[start:end + 1]

    cleaned = re.sub(r",\s*([}\]])", r"\1", cleaned)

    return cleaned


def process_user_input(user_text):
    """Takes text, returns JSON."""
    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_text}
            ],
            temperature=0.3
        )
        ai_reply = response.choices[0].message.content
        ai_reply = extract_json_object(ai_reply)
        
        # ✅ Convert the string to JSON safely
        result = json.loads(ai_reply)
        return normalize_result(result)
    except Exception as e:
        print(f"Error: {e}")
        return {"intent": "GENERAL_CHAT", "mood": "neutral", "emoji": "😐", "data": {}, "reply": "Sorry, I hit a snag!"}


# This function talks to Person 2's Backend
def send_to_backend(intent, data, user_id):
    data["user_id"] = user_id
    url = "http://127.0.0.1:8000/api/assistant"
    payload = {"intent": intent, "data": data}
    try:
        response = requests.post(url, json=payload)
        return response.json()
    except Exception as e:
        return {"error": f"Could not connect to backend: {e}"}


# This function asks the backend for your existing data
def fetch_from_backend(intent, user_id):
    url = "http://127.0.0.1:8000/api/assistant"
    payload = {"intent": intent, "data": {"user_id": user_id}}
    try:
        response = requests.post(url, json=payload)
        return response.json()
    except Exception as e:
        return {"error": f"Could not fetch data: {e}"}


# This is the function Person 2 and Person 4 will call!
def get_ai_response(user_text, user_id):
    """Takes text, returns clean structured data for the backend."""
    result = process_user_input(user_text)
    
    # 1. SENDING DATA TO THE BACKEND
    if result["intent"] in ["CREATE_NOTE", "CREATE_REMINDER", "ADD_EXPENSE", "ADD_SHOPPING_ITEM", "STUDY_PLAN", "CREATE_GOAL", "LOG_MOOD", "CREATE_MEMORY", "SAVE_CONTEXT", "DRAFT_EMAIL"]:
        backend_response = send_to_backend(result["intent"], result["data"], user_id)
        print("✅ Backend says:", backend_response)
        
    # 2. FETCHING DATA FROM THE BACKEND
    elif result["intent"] in ["GET_NOTES", "GET_REMINDERS", "GET_EXPENSES", "GET_SHOPPING_LIST", "GET_STUDY_PLANS", "GET_GOALS", "GET_MOODS", "GET_MEMORIES", "GET_CONTEXT", "SHOW_INFORMATION"]:
        fetched_data = fetch_from_backend(result["intent"], user_id)
        print("✅ Fetched from database:", fetched_data)
        
        # Make Nova actually SPEAK the fetched data
        if fetched_data.get("success"):
            if result["intent"] == "GET_NOTES":
                notes = [note["text"] for note in fetched_data.get("notes", [])]
                result["reply"] = f"Here are your notes: {', '.join(notes)}"
            elif result["intent"] == "GET_REMINDERS":
                tasks = [rem["task"] for rem in fetched_data.get("reminders", [])]
                result["reply"] = f"Here are your reminders: {', '.join(tasks)}"
            elif result["intent"] == "GET_EXPENSES":
                details = [f"{exp['amount']} on {exp['category']}" for exp in fetched_data.get("expenses", [])]
                result["reply"] = f"Here are your expenses: {', '.join(details)}"
            elif result["intent"] == "GET_SHOPPING_LIST":
                items = [item["item"] for item in fetched_data.get("shopping_items", [])]
                result["reply"] = f"Here is your shopping list: {', '.join(items)}"
            elif result["intent"] == "GET_GOALS":
                goals = [goal["goal"] for goal in fetched_data.get("goals", [])]
                result["reply"] = f"Here are your goals: {', '.join(goals)}"
            elif result["intent"] == "GET_STUDY_PLANS":
                subjects = [plan["subject"] for plan in fetched_data.get("study_plans", [])]
                result["reply"] = f"Here are your study plans: {', '.join(subjects)}"
            elif result["intent"] == "SHOW_INFORMATION":
                briefing = fetched_data.get("briefing", {})
                total_expenses = briefing.get("total_expenses", 0)
                result["reply"] = f"Your total expenses are {total_expenses}. You have {len(briefing.get('reminders', []))} reminders today."
        
    # 3. INSTANT MODULES (No backend needed)
    elif result["intent"] in ["TRANSLATE_TEXT", "SUMMARIZE_TEXT", "GENERATE_FLASHCARDS", "GENERAL_CHAT"]:
        print("🔔 INSTANT MODULE: No backend needed. Just showing AI's answer!")
        
    structured_data = {
        "intent": result.get("intent"),
        "mood": result.get("mood"),
        "emoji": result.get("emoji"),
        "data": result.get("data"),
        "reply": result.get("reply")
    }
    return structured_data


# --- Testing Area ---
if __name__ == "__main__":
    print(">> Nova Brain is ready! Type 'exit' to quit.")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == "exit":
            break
        
        # NOTE: We are passing the test user_id directly for now!
        test_user_id = '70b8f321-126c-4285-af9c-2cac962f0597'
        
        result = get_ai_response(user_input, test_user_id)
        print("\n>> AI Output (JSON):")
        print(json.dumps(result, indent=2, ensure_ascii=False))  # ✅ FINAL FIX: This prints the real emoji!
        print(f"\n>> Nova says: {result['reply']}")