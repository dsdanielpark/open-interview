from .models.gpt import InterviewGPT
from .models.claude import InterviewClaude

from .manager import InterviewManager

from .utils.doc_manager import DocumentCreator
from .utils.file_manager import load_file_content
from .utils.prompter import create_system_prompt, create_base_prompt

from .modules.voice.random_play import RandomPlayer
from .modules.voice.google import google_tts, google_stt, save_google_tts

try:
    from openinterview.modules.voice.openai import openai_tts, openai_stt
except ImportError:
    pass


__version__ = "1.0.11"
__author__ = "daniel park <parkminwoo1991@gmail.com>"
