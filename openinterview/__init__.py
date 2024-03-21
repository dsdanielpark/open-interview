from .manager import InterviewManager
from .models.claude import InterviewClaude
from .models.gpt import InterviewGPT
from .utils.doc_manager import DocumentCreator
from .utils.file_manager import load_file_content
from .utils.prompter import create_system_prompt, create_base_prompt
from .module.voice.google import google_tts, google_stt, save_qa_as_tts

try:
    from openinterview.module.voice.openai import openai_tts, openai_stt
except ImportError:
    pass


__version__ = "1.0.0"
__author__ = (
    "daniel park <parkminwoo1991@gmail.com>, antonio cheang <teapotv8@proton.me>"
)
