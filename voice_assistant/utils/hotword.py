import pvporcupine
import sounddevice as sd
import numpy as np

HOTWORD = "jarvis"

ACCESS_KEY = "y4yzhRuxXRxmtslZBJkbuBxuW9p2Rgjw1HChHvb/1UHTQiLTVlBKgg=="  # Replace with your real key
porcupine = pvporcupine.create(access_key=ACCESS_KEY, keywords=[HOTWORD])

SAMPLERATE = 16000
FRAMES_PER_BUFFER = porcupine.frame_length

def listen_for_hotword():
    print("[HOTWORD] Listening for hotword 'jarvis'...")
    with sd.InputStream(channels=1, samplerate=SAMPLERATE, dtype='int16', blocksize=FRAMES_PER_BUFFER) as stream:
        while True:
            pcm = stream.read(FRAMES_PER_BUFFER)[0].flatten()
            result = porcupine.process(pcm)
            if result >= 0:
                print("[HOTWORD] Hotword 'jarvis' detected!")
                return True 