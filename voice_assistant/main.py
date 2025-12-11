import time
import json
import re
from audio.new_recorder import record_audio
from stt.whisper_transcriber import transcribe_audio
from nlp.command_parser import parse_command
from utils.gemini_api import get_gemini_response
from actions.system_actions import execute_action
from utils.onscreen_window import OnScreenAssistant
from utils.hotword import listen_for_hotword

LOG_PATH = "log.txt"

def log_event(event):
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {event}\n")

def process_command(text, window):
    """Process either voice or text command using the same logic"""
    print(f"[Assistant] Processing command: {text}")
    # First try keyword-based parser
    intent = parse_command(text)
    if intent["type"] != "unknown":
        print(f"[Assistant] Detected intent (keyword parser): {intent}")
        execute_action(intent)
        window.update_display(text, str(intent))
    else:
        # Fallback to Gemini for complex/natural language commands
        gemini_response = get_gemini_response(text)
        print(f"[Gemini] Response: {gemini_response}")
        window.update_display(text, gemini_response)
        try:
            match = re.search(r'(\[.*?\]|\{.*?\})', gemini_response, re.DOTALL)
            if match:
                parsed = json.loads(match.group(0))
                if isinstance(parsed, list):
                    for intent in parsed:
                        print(f"[Assistant] Detected intent (Gemini): {intent}")
                        execute_action(intent)
                else:
                    print(f"[Assistant] Detected intent (Gemini): {parsed}")
                    execute_action(parsed)
            else:
                print("[Assistant] No valid JSON object or list found in Gemini response.")
                log_event(f"No valid JSON in Gemini response: {gemini_response}")
        except Exception as e:
            print(f"[Assistant] Error parsing Gemini response as JSON: {e}")
            log_event(f"Error parsing Gemini response: {gemini_response}")

def handle_text_command(text, window):
    """Handle text commands from the input bar"""
    log_event(f"Processing text command: {text}")
    process_command(text, window)

def main_loop():
    log_event("Assistant started main loop.")
    window = OnScreenAssistant(command_callback=lambda text: handle_text_command(text, window))
    
    def voice_command_thread():
        while True:
            try:
                listen_for_hotword()
                print("\n[Assistant] Hotword detected. Listening for command...")
                if record_audio("audio/input.wav"):
                    text = transcribe_audio("audio/input.wav")
                    process_command(text, window)
            except Exception as e:
                print(f"Error in voice command thread: {e}")
                log_event(f"Error: {e}")
                time.sleep(0.2)  # Short pause after error before retrying
    
    import threading
    voice_thread = threading.Thread(target=voice_command_thread, daemon=True)
    voice_thread.start()
    
    # Run the GUI main loop
    window.run()

if __name__ == "__main__":
    main_loop() 