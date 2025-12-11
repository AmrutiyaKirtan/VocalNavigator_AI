from PIL import ImageGrab
import pytesseract
import pyautogui
import difflib

def find_text_on_screen(label):
    """
    Capture a screenshot and use pytesseract to find the bounding box of the given label.
    Prints all detected words and their positions for debugging.
    Uses fuzzy matching to find the closest match.
    Returns (x, y) coordinates of the center of the best match, or None if not found.
    """
    screenshot = ImageGrab.grab()
    data = pytesseract.image_to_data(screenshot, output_type=pytesseract.Output.DICT)
    words = [word.strip() for word in data['text'] if word.strip()]
    print("[OCR] Detected words and positions:")
    for i, word in enumerate(data['text']):
        if word.strip():
            print(f"  '{word}' at ({data['left'][i]}, {data['top'][i]}, {data['width'][i]}, {data['height'][i]})")
    # Fuzzy match
    matches = difflib.get_close_matches(label.strip().lower(), [w.lower() for w in words], n=1, cutoff=0.6)
    if matches:
        best = matches[0]
        for i, word in enumerate(data['text']):
            if word.strip().lower() == best:
                x = data['left'][i] + data['width'][i] // 2
                y = data['top'][i] + data['height'][i] // 2
                print(f"[OCR] Best match: '{word}' at ({x}, {y})")
                return (x, y)
    print("[OCR] No close match found for label:", label)
    return None 