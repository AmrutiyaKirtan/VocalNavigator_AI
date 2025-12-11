import re

def parse_command(text):
    """Parse the transcribed text and return a structured intent dict for basic commands."""
    text = text.lower().strip()
    # Open app
    match = re.match(r"open (.+)", text)
    if match:
        return {"type": "open_app", "app": match.group(1).strip()}
    # Close app
    match = re.match(r"close (.+)", text)
    if match:
        return {"type": "close_app", "app": match.group(1).strip()}
    # Scroll down
    if "scroll down" in text:
        return {"type": "scroll", "direction": "down"}
    # Scroll up
    if "scroll up" in text:
        return {"type": "scroll", "direction": "up"}
    # Right click
    if "right click" in text or text == "click right":
        return {"type": "click", "label": "right"}
    # Click
    if text == "click":
        return {"type": "click"}
    # Fallback
    return {"type": "unknown", "raw": text} 