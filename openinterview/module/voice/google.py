# To-Do: Need QA and error handling
import os
from gtts import gTTS
from typing import Dict
import speech_recognition as sr


def google_tts(text, save_dir, lang="en"):
    """
    Generates and saves a spoken version of the input text using Google's Text-to-Speech API.

    Parameters:
    - text (str): The text to be converted to speech.
    - save_dir (str): Directory where the speech file will be saved.
    - lang (str): The language of the text (default is English, 'en').

    Returns:
    - str: The file path of the saved speech file.

    Example:
    >>> save_path = google_tts("Hello, world!", "./cache", "en")
    >>> print(save_path)
    ./cache/tts.mp3
    """
    tts = gTTS(text=text, lang=lang)
    os.makedirs(save_dir, exist_ok=True)
    save_path = f"{save_dir}/tts.mp3"
    tts.save(save_path)
    return save_path


def google_stt(audio_file_path: str, recognizer: str = "google") -> str:
    """
    Converts speech in an audio file to text using various Speech Recognition APIs.

    Args:
        audio_file_path (str): The file path of the audio file to be transcribed.
        recognizer (str): The speech recognition service to use. Options include 'google', 'bing', 'google_cloud',
                          'houndify', 'ibm', 'sphinx', 'wit'. Default is 'google'.

    Returns:
        str: The text transcription of the audio file. Returns an error message if conversion fails or file format is incompatible.

    Raises:
        ValueError: If the audio file format is not supported or recognizer is not recognized.

    Example:
        >>> text = speech_to_text("./cache/audio.wav", recognizer='google')
        >>> print(text)
        'Hello, world!'
    """
    r = sr.Recognizer()
    try:
        with sr.AudioFile(audio_file_path) as source:
            audio_text = r.listen(source)
    except (EOFError, ValueError) as e:
        return f"Error processing audio file: {e}. Ensure file is a compatible format (WAV, AIFF, FLAC)."

    try:
        text = {
            "google": lambda audio: r.recognize_google(audio),
            # Add other recognizers here following the pattern
        }.get(recognizer, lambda audio: None)(audio_text)

        if text is None:
            raise ValueError(f"Recognizer '{recognizer}' is not supported.")

        return text
    except Exception as e:
        return f"Failed to convert speech to text: {e}."


def save_qa_as_tts(qa_dict: Dict[str, str], save_dir: str) -> None:
    """
    Generates and saves spoken versions of questions and answers from a dictionary
    using Google's Text-to-Speech API. Each question and answer pair is saved in
    a directory named after the hex code in the dictionary key, with separate MP3 files
    for the question and the answer.

    Parameters:
    - qa_dict (Dict[str, str]): A dictionary where keys are prefixed with 'Q_' or 'A_'
      followed by a hex code, indicating questions and answers, respectively. The value
      for each key is the text of the question or answer.
    - save_dir (str): The base directory where the MP3 files will be saved. Directories
      named after the hex codes in the keys will be created here.

    Note:
    This function requires the google_tts function to be defined, which takes a text
    string, a directory to save the MP3 file, and a language code, then generates and
    saves the spoken version of the text as an MP3 file in the specified directory.

    No return value. Files are saved to disk.
    """
    for key, text in qa_dict.items():
        prefix = "Q" if key.startswith("Q") else "A"
        hex_code = key.split("_")[-1]
        hex_save_dir = os.path.join(save_dir, hex_code)
        file_name = "question.mp3" if prefix == "Q" else "answer.mp3"
        full_save_path = os.path.join(hex_save_dir, file_name)
        google_tts(text, hex_save_dir, "en")
        os.rename(os.path.join(hex_save_dir, "tts.mp3"), full_save_path)
