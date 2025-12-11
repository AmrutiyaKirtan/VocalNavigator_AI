import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import webrtcvad
import time
import struct

SAMPLE_RATE = 16000
CHANNELS = 1
CHUNK_DURATION_MS = 30  # Duration of each audio chunk in milliseconds
CHUNK_SIZE = int(SAMPLE_RATE * CHUNK_DURATION_MS / 1000)  # Number of samples per chunk
SILENCE_THRESHOLD = 10  # Number of silent chunks before stopping

def record_audio(filename="audio/input.wav"):
    """
    Record audio from the microphone using WebRTC VAD.
    Stops after detecting a period of silence.
    Saves as a WAV file.
    """
    vad = webrtcvad.Vad(3)  # Aggressiveness level 3 (most aggressive)
    print("[audio.recorder] Listening... Speak now!")
    
    frames = []
    silence_count = 0
    
    def callback(indata, frame_count, time_info, status):
        frames.append(indata.copy())
        # Convert float32 audio data to int16 for VAD
        audio_chunk = (indata.flatten() * 32768).astype(np.int16)
        raw_data = struct.pack("%dh" % len(audio_chunk), *audio_chunk)
        
        # Check if the chunk contains speech
        try:
            is_speech = vad.is_speech(raw_data, SAMPLE_RATE)
            nonlocal silence_count
            if not is_speech:
                silence_count += 1
            else:
                silence_count = 0
        except Exception as e:
            print(f"VAD error: {e}")
    
    try:
        with sd.InputStream(samplerate=SAMPLE_RATE, channels=CHANNELS, 
                          callback=callback, dtype=np.float32,
                          blocksize=CHUNK_SIZE):
            while silence_count < SILENCE_THRESHOLD:
                time.sleep(0.1)
    except Exception as e:
        print(f"Error recording audio: {e}")
        return False
    
    if len(frames) == 0:
        print("No audio recorded")
        return False
    
    # Convert and save the audio
    audio_data = np.concatenate(frames, axis=0)
    write(filename, SAMPLE_RATE, audio_data)
    print(f"[audio.recorder] Audio saved to {filename}")
    return True
