from openinterview.module.voice.google import google_tts, google_stt, save_qa_as_tts

try:
    from openinterview.module.voice.openai import openai_tts, openai_stt
except ImportError:
    pass
