import os
from .utils.doc_manager import DocumentCreator
from .models import ClaudeGenerator, GptGenerator
from .modules.voice.google import save_google_tts


class InterviewManager:
    """
    Manages the creation of interview documents and audio using different AI engines.

    Attributes:
        api_key (str): The API key for accessing the underlying AI services.
        engine (str): The name of the engine to use for generating interview content. Currently supports 'GPT' or 'Claude'.

    Raises:
        ValueError: If an unsupported engine is specified.
    """

    def __init__(self, api_key, engine="GPT"):
        """
        Initializes the InterviewManager with an API key and engine choice.

        Args:
            api_key (str): The API key required to access AI services.
            engine (str, optional): The engine to use for content generation ('GPT' or 'Claude'). Defaults to 'GPT'.
        """
        self.api_key = api_key
        self.engine = engine

        if engine == "GPT":
            self.interviewer = GptGenerator(api_key=api_key)
        elif engine == "Claude":
            self.interviewer = ClaudeGenerator(api_key=api_key)
        else:
            raise ValueError("Unsupported engine. Please choose 'GPT' or 'Claude'.")

    def generate_interview(
        self,
        jd,
        resume,
        position,
        interview_type,
        language="English",
        max_sentence=6,
        output_dir="output",
        system_prompt=None,
        user_prompt=None,
        iteration: int = 1,
    ):
        """
        Generates interview content based on the job description, resume, and other parameters. Outputs include QA documents and audio files.

        Args:
            jd (str): Job description to base the interview questions on.
            resume (str): The candidate's resume.
            position (str): The position being applied for.
            interview_type (str): The type of interview to simulate.
            language (str, optional): The language for the interview. Defaults to "English".
            max_sentence (int, optional): The maximum number of sentences for the system's responses. Defaults to 6.
            output_dir (str, optional): The directory where generated content will be saved. Defaults to "output".
            system_prompt (str, optional): Custom prompt for the system to generate interview content. If None, a default is created. Defaults to None.
            user_prompt (str, optional): Custom prompt for the user's responses in the interview. If None, a default is created. Defaults to None.
            iteration (int, optional): The number of iterations for content generation. Defaults to 1.

        Generates:
            Documents and audio files based on the generated interview content, saved in the specified output directory.
        """
        if not system_prompt:
            system_prompt = self.interviewer.create_system_prompt(
                jd=jd,
                candidate_resume=resume,
                position=position,
                interview_type=interview_type,
                language=language,
                max_sentence=max_sentence,
            )
        if not user_prompt:
            user_prompt = self.interviewer.create_base_prompt("generateQAs")

        generated_qa_dict = self.interviewer.generate_interview_content(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            iteration=iteration,
            save_dir=os.path.join(output_dir, "generated_qa"),
        )

        document_creator = DocumentCreator()
        document_creator.create_qa_document(
            generated_qa_dict, "TeamViewer15", 11, os.path.join(output_dir, "document")
        )

        save_google_tts(generated_qa_dict, os.path.join(output_dir, "voice"))
