from openinterview.modules.voice.google import google_tts, google_stt, save_google_tts
from openinterview.modules.voice.random_play import RandomQPlay

try:
    from openinterview.modules.voice.openai import openai_tts, openai_stt
except ImportError:
    pass
