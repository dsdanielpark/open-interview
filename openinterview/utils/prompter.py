def create_system_prompt(
    candidate_resume: str = None,
    jd: str = None,
    interviewer_resume: str = "",
    interview_type: str = "base",
    position: str = "AI researcher",
    language: str = "English",
    max_sentence: int = 10,
    custom_prompt: str = "",
) -> str:
    """
    Generates a custom interview prompt.
    """
    base = f"You are a helpful assistant and the {interview_type} interviewer for a candidate for the {position} position. Please formulate questions based on the interviewee resume as follow:\n\n{candidate_resume}.\n\nand job description as follow:\n\n{jd}.\nWrite in {language} and create answers containing at least {max_sentence} sentences each."
    if interviewer_resume:
        base += f"Given the interviewer's career background, craft sharp questions for the candidate based on the interviewer's experience and expertise.\n- Resume of interviewer:\n{interviewer_resume}"
    instructions = {
        "techQAsFromResume": "Focus on technical skills in given resume, e.g., Unet for brain tumor segmentation.",
        "techQAsFromExperts": "Create questions from your expertise related to the position.",
        "techQAs": f"Create questions based on both your and the interviewee's experience. For example, detail on similar technical challenges.",
        "personalityQAs": "Inquire about personal qualities and competencies, such as teamwork.",
        "reviewResume": "Point out specific shortcomings in the resume, providing guidance for improvement.",
    }
    specific_instructions = instructions.get(
        interview_type, "Inquire about both technical skills and personal qualities."
    )
    prompt = f"{base}\n\n{specific_instructions}"
    return (
        prompt + f"\nAdditional Instructions: {custom_prompt}"
        if custom_prompt
        else prompt
    )


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
