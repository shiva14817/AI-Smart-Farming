import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env file
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print("API Key Found:", "YES" if api_key else "NO")

genai.configure(api_key=api_key)

MODELS = [
    "gemini-3.5-flash",
    "gemini-3.6-flash",
    "gemini-3.1-flash-lite",
    "gemini-3-pro-preview",
    "gemini-2.0-flash",
    "gemini-flash-latest",
]

for model_name in MODELS:
    print("\n" + "=" * 60)
    print("Testing:", model_name)

    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content("Say Hello")
        print("✅ SUCCESS")
        print(response.text)

    except Exception as e:
        print("❌ FAILED")
        print(e)