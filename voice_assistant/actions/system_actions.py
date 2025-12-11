import os
import pyautogui
import time
from utils.screen import find_text_on_screen

def execute_action(intent):
    """Execute a system action based on the parsed intent."""
    try:
        if intent["type"] == "open_app":
            app = intent.get("app")
            if app:
                print(f"[Action] Opening app: {app} ...")
                os.system(f"start {app}")
                # Add a delay to allow the app to load before any follow-up click
                time.sleep(1)
            else:
                print("[Action] No app name provided in intent.")
        elif intent["type"] == "close_app":
            app = intent.get("app")
            if app:
                print(f"[Action] Closing app: {app} ...")
                # Try to close the app by killing its process (Windows)
                os.system(f"taskkill /im {app}.exe /f")
            else:
                print("[Action] No app name provided for close action.")
        elif intent["type"] == "scroll":
            direction = intent.get("direction")
            amount = 500  # You can adjust scroll amount
            if direction == "down":
                print("[Action] Scrolling down...")
                pyautogui.scroll(-amount)
            elif direction == "up":
                print("[Action] Scrolling up...")
                pyautogui.scroll(amount)
            else:
                print(f"[Action] Unknown scroll direction: {direction}")
        elif intent["type"] == "click":
            label = intent.get("label")
            if not label:
                print("[Action] No label provided. Performing left click at current mouse position.")
                pyautogui.click()
            elif label.lower() == "right":
                print("[Action] Performing right click at current mouse position.")
                pyautogui.rightClick()
            else:
                print(f"[Action] Looking for '{label}' on screen...")
                coords = find_text_on_screen(label)
                if coords:
                    print(f"[Action] Clicking at {coords} for label '{label}'")
                    pyautogui.moveTo(coords[0], coords[1], duration=0.2)
                    pyautogui.click()
                else:
                    print(f"[Action] Could not find '{label}' on screen.")
        else:
            print(f"[Action] Unknown or unsupported intent: {intent}")
    except Exception as e:
        print(f"[Action] Error executing action: {e}") 