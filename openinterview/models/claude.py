import os
import json
import anthropic
from datetime import datetime
from typing import List, Dict, Any
from openinterview.utils.file_manager import load_file_content


class ClaudeGenerator:
    """
    Class for conducting interviews using Claude, an AI model from Anthropic.

    Args:
        model (str): The version of Claude model to be used. Defaults to "claude-3-opus-20240229".
        api_key (str): The API key required for accessing Anthropic's services.

    Raises:
        ValueError: If API key is not provided.

    Attributes:
        model (str): The version of Claude model being used.
        api_key (str): The API key for accessing Anthropic's services.
        client: An instance of the Anthropic client.
        messages (List[Dict[str, Any]]): A list to store interview messages.
    """

    def __init__(self, model: str = "claude-3-opus-20240229", api_key: str = None):
        if not api_key:
            raise ValueError(
                "API key is required. Visit https://console.anthropic.com/"
            )
        self.model = model
        self.api_key = api_key
        self.client = anthropic.Anthropic(
            api_key=self.api_key
        )  # Initialize the client.
        self.messages: List[Dict[str, Any]] = []

    def generate_content(
        self, system_prompt: str, user_prompt: str = "", **kwargs
    ) -> str:
        """
        Generates content based on provided prompts.

        Args:
            system_prompt (str): The system prompt.
            user_prompt (str): The user prompt. Defaults to "".

        Returns:
            str: The generated content.
        """
        self._add_message("user", user_prompt)
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=4096,
                temperature=0.0,
                system=system_prompt,
                messages=self.messages,
                **kwargs,
            )
            return response.content[0].text
        except Exception as e:
            raise Exception(f"APIErrorOccurred: {str(e)}")

    def _add_message(self, role: str, content: str) -> None:
        """
        Adds a message to the interview.

        Args:
            role (str): The role of the participant adding the message.
            content (str): The content of the message.
        """
        if not self.messages or not self.messages[0].get("role"):
            self.messages = [{"role": role, "content": content}]

    def generate_interview_content(
        self, system_prompt: str, user_prompt: str, iteration: int, save_dir: str
    ) -> Dict[str, Any]:
        """
        Generate interview content by interacting with the model.

        This method interacts with the model for the specified number of iterations,
        generating interview content based on the system prompt and a list of user prompts.
        It saves the generated content in JSON format to the specified directory.

        Args:
            system_prompt (str): The initial prompt to start the conversation.
            user_prompts (str): A list of prompts from users to continue the conversation.
            iteration (int): The number of iterations to generate interview content.
            save_dir (str): The directory path to save the generated interview content.

        Returns:
            Dict[str, Any]: A dictionary containing the generated interview content.

        Raises:
            None
        """
        total_qa_dict: Dict[str, Any] = {}
        cached_dir = os.path.join(save_dir, "cached")
        os.makedirs(cached_dir, exist_ok=True)

        for i in range(iteration):
            response_text = self.generate_content(system_prompt, user_prompt)
            batch_qa_dict = self._postprocess_response(response_text)
            batch_file_path = os.path.join(
                cached_dir,
                f"batch_output_{i}_{datetime.now().strftime('%Y%m%d%H%M%S%f')}.json",
            )
            with open(batch_file_path, "w", encoding="utf-8") as f:
                json.dump(batch_qa_dict, f, ensure_ascii=False, indent=4)
            total_qa_dict.update(
                batch_qa_dict if isinstance(batch_qa_dict, dict) else {}
            )

        print(f"Each response saved in cached folder: {cached_dir}")
        return total_qa_dict

    def _postprocess_response(self, response_text: str) -> Dict[str, Any]:
        """
        Postprocesses the response text.

        Args:
            response_text (str): The response text to be postprocessed.

        Returns:
            Dict[str, Any]: The postprocessed response as a dictionary.
        """
        try:
            return eval(response_text)
        except SyntaxError:
            return {
                "UnparsedPayload"
                + datetime.now().strftime("%Y%m%d%H%M%S%f"): response_text
            }

    def _reset_messages(self) -> None:
        self.messages = []

    @staticmethod
    def create_system_prompt(
        position: str = "AI researcher",
        jd: str = None,
        interview_type: str = "base",
        language: str = "English",
        candidate_resume: str = None,
        interviewer_resume: str = "",
        max_sentence: int = 10,
        custom_prompt: str = "",
    ) -> str:
        """
        Generates a custom interview prompt.
        """
        if jd and jd.endswith((".pdf", ".txt")):
            jd = load_file_content(jd)
        if candidate_resume and candidate_resume.endswith((".pdf", ".txt")):
            candidate_resume = load_file_content(candidate_resume)
        if interviewer_resume and interviewer_resume.endswith((".pdf", ".txt")):
            candidate_resume = load_file_content(candidate_resume)

        base = f"You are a helpful assistant and the {interview_type} interviewer for a candidate for the {position} position. Please formulate questions based on the interviewee resume as follow:\n\n{candidate_resume}.\n\nand job description as follow:\n\n{jd}.\nWrite in {language} and create answers containing at least {max_sentence} sentences each."

        if interviewer_resume:
            base += f"Given the interviewer's career background, craft sharp questions for the candidate based on the interviewer's experience and expertise.\n- Resume of interviewer:\n{interviewer_resume}"
        instructions = {
            "generalQAs": "Inquire about both technical skills and personal qualities. Ask in-depth and professionally, pressing for truth about strengths and weaknesses, and ask sequentially to gauge depth of knowledge.",
            "generalTechQAs": "Overall, ask professional questions about basic concepts commonly used, referencing the given position or resume. For example, if it's for an AI Researcher position, ask simple questions about the basic principles of CNN and the differences between CNN and ViT.",
            "techQAsFromResume": "Focus on technical skills in given resume, e.g., Unet for brain tumor segmentation.",
            "techQAsFromExperts": "Create questions from your expertise related to the position.",
            "techQAs": f"Create questions based on both your and the interviewee's experience. For example, detail on similar technical challenges.",
            "personalityQAs": "Inquire about personal qualities and competencies, such as teamwork.",
            "reviewResume": "Point out specific shortcomings in the resume, providing guidance for improvement.",
        }
        specific_instructions = instructions.get(
            interview_type,
            "Inquire about both technical skills and personal qualities.",
        )
        prompt = f"{base}\n\n{specific_instructions}"

        return (
            prompt + f"\nAdditional Instructions: {custom_prompt}"
            if custom_prompt
            else prompt
        )

    @staticmethod
    def create_base_prompt(interview_type: str) -> str:
        """
        Generates a base prompt based on the interview type.
        """
        prompts = {
            "generateQs": "Ensure responses don't duplicate. Give me Python dict form code only without anyother words, keys must always be in quotes,Keys in quotes, e.g., \"Q_2\". Ensure the 'n' following the underscore in 'Q_n' represents a 6-digit hex code, not just a simple integer.",
            "generateQAs": "ensure the response doesn't duplicate previous answers. In Python dict form, keys must always be in quotes, e.g., not Q_2 but the string type \"Q_2\". Create answers containing at least 10 sentences. Generate questions and answers starting from `Q_n`. For each Qn, where Q is followed by an 8-digit hex code, ensure the corresponding answer has the same hex code. For example, if the question dictionary key is 'Q_24838402', the answer dictionary key must be 'A_24838402'. Provide the responses in Python dictionary format only, excluding any other text.",
            "pointOutResume": "Ensure responses don't duplicate. Give me Python dict form code only without anyother words. Identify and point out improvable areas in the resume. Provide original and enhanced sentences. ",
            "adviceResume": "Ensure responses don't duplicate. Give me Python dict form code only without anyother words. Edit parts of the resume needing correction or strengthening, focusing on job relevance.",
        }
        return prompts.get(interview_type, "")
