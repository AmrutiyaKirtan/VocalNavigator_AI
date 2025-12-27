import google.generativeai as genai

# Set your Gemini API key here
GEMINI_API_KEY = "Add your api key here"
GEMINI_MODEL = "gemini-2.0-flash"

# Centralized intent extraction prompt
INTENT_EXTRACTION_PROMPT = (
    "You are an intent extraction engine.\n"
    "Given the following user command, only return a single valid JSON object describing the intent.\n"
    "Do not include any explanation or extra text.\n"
    "Examples:\n"
    "- 'open Chrome' -> {\"type\": \"open_app\", \"app\": \"chrome\"}\n"
    "- 'open Notepad' -> {\"type\": \"open_app\", \"app\": \"notepad\"}\n"
    "- 'scroll down' -> {\"type\": \"scroll\", \"direction\": \"down\"}\n"
    "- 'click the Confirm button' -> {\"type\": \"click\", \"label\": \"confirm\"}\n"
    "Now extract the intent for: "
)

def get_gemini_response(user_text):
    """
    Send user_text to Gemini API, prepending a strict prompt to only return a single valid JSON object describing the intent.
    Requires google-generativeai package.
    """
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel(GEMINI_MODEL)
        prompt = INTENT_EXTRACTION_PROMPT + user_text
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"[Gemini API] Error: {e}")
        return "" 
