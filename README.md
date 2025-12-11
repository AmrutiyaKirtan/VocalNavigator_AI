# 🎤 VocalNavigator AI

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen)]()

A highly responsive, hands-free desktop assistant that listens for your voice commands and translates them into real-time system actions. Built with a modular architecture and a hybrid NLP engine for speed and flexibility.

---

## ✨ Key Features

- **Always-On Hotword Detection:** Powered by **Porcupine**, the assistant listens passively for a wake word (e.g., "Jarvis") without constant resource drain.
- **Efficient Voice Activity Detection (VAD):** Records audio only when the user is speaking and automatically stops on silence, ensuring fast and clean input for transcription.
- **High-Accuracy Transcription:** Utilizes **OpenAI's Whisper** model for robust and precise speech-to-text conversion.
- **Hybrid Intent Parsing Engine:**
    - **Keyword-Based Parser:** Instantly recognizes simple, critical commands (`open`, `close`, `click`, `scroll`) for maximum speed.
    - **LLM Fallback:** Leverages **Google's Gemini** for complex, natural language commands that require advanced understanding.
- **Real-Time Desktop Control:** Directly interacts with the OS using **PyAutoGUI** to perform actions like opening applications, managing windows, clicking, and scrolling.
- **Modular and Extendable Architecture:** Code is organized into logical modules (`audio`, `stt`, `nlp`, `actions`), making it easy to maintain and add new functionality.

---

## ⚙️ How It Works (Workflow)

[Listen for Hotword] -> [Record Command (VAD)] -> [Transcribe (Whisper)] -> [Parse Intent] -> [Execute Action]
(Porcupine) (Keyword / Gemini) (PyAutoGUI)

text

---

## 🛠️ Tech Stack

- **Hotword:** Picovoice Porcupine
- **Audio Processing:** Sounddevice, VAD (Voice Activity Detection)
- **Speech-to-Text (STT):** OpenAI Whisper
- **Natural Language Processing (NLP):** Custom Keyword Parser & Google Gemini
- **Desktop Automation:** PyAutoGUI
- **OS Interaction:** `os.system`, `taskkill`

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- A Porcupine Access Key ([Get one for free here](https://picovoice.ai/console/))
- A Google Gemini API Key ([Get one here](https://aistudio.google.com/app/apikey))

### Installation & Setup
1.  **Clone the repository:**
    ```
    git clone https://github.com/AmrutiyaKirtan/VocalNavigator_AI.git
    cd VocalNavigator_AI
    ```

2.  **Create a virtual environment:**
    ```
    python -m venv venv
    .\venv\Scripts\activate  # On Windows
    # source venv/bin/activate  # On macOS/Linux
    ```

3.  **Install the dependencies:**
    ```
    pip install -r requirements.txt
    ```

4.  **Configure your API keys:**
    Create a file named `.env` in the root directory and add your keys:
    ```
    PORCUPINE_ACCESS_KEY="your_porcupine_key_here"
    GEMINI_API_KEY="your_gemini_api_key_here"
    ```

### Running the Assistant
Simply run the main script from your terminal:
python index.py

text
Say the hotword (e.g., "Jarvis") and then your command.

---

## 📂 Project Structure
VocalNavigator_AI/
├── voice_assistant/
│ ├── audio/ # Audio recording and VAD
│ ├── stt/ # Whisper transcription module
│ ├── nlp/ # Intent parsing (Keyword & Gemini)
│ ├── actions/ # Desktop control functions
│ └── utils/ # Utility functions
├── index.py # Main application loop
├── requirements.txt # Project dependencies
└── .env # API keys (not committed)

text

---
*Created by Kirtan Amrutiya*
