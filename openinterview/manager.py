import os
from .models import InterviewClaude, InterviewGPT
from .module.voice.google import save_google_tts
from .utils.doc_manager import DocumentCreator


class InterviewManager:
    def __init__(self, api_key, engine="GPT"):
        self.api_key = api_key
        self.engine = engine

        if engine == "GPT":
            self.interviewer = InterviewGPT(api_key=api_key)
        elif engine == "Claude":
            self.interviewer = InterviewClaude(api_key=api_key)
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
    ):
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
            iteration=1,
            save_dir=os.path.join(output_dir, "generated_qa"),
        )

        document_creator = DocumentCreator()
        document_creator.create_qa_document(
            generated_qa_dict, "TeamViewer15", 11, os.path.join(output_dir, "document")
        )

        save_google_tts(generated_qa_dict, os.path.join(output_dir, "voice"))
