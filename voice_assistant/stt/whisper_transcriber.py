import whisper
import warnings
warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")

def transcribe_audio(filename="audio/input.wav"):
    """Transcribe audio using local Whisper model."""
    print(f"[stt.whisper_transcriber] Transcribing {filename} with Whisper...")
    try:
        model = whisper.load_model("base")
        result = model.transcribe(filename)
        text = result["text"].strip()
        print(f"[stt.whisper_transcriber] Transcription: {text}")
        return text
    except Exception as e:
        print(f"[stt.whisper_transcriber] Error during transcription: {e}")
        return "" 