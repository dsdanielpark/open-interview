
# Usage
This section provides examples of how to use the tool effectively. Before proceeding, ensure you meet the following requirements:

## Prerequisites

- Python 3.7+
- API key from OpenAI, Anthropic, and Google.


<details>
<summary>OpenAI API Key and Credits</summary>
<p>

You can get an OpenAI API Key by following these steps:
1. Sign up or log in to your OpenAI account.
2. Navigate to the API section.
3. Follow the instructions to generate a new API key.

For detailed steps, visit [OpenAI API Documentation](https://beta.openai.com/docs/api-reference/authentication).

To add billing credits:
1. Go to the Billing section in your OpenAI account.
2. Choose to add credits or update your billing method.

For more information on managing billing and credits, check out [OpenAI Billing FAQ](https://help.openai.com/en/articles/5726858-billing-faq).

</p>
</details>

<details>
<summary>Anthropic API Key and Credits</summary>
<p>

You can get an Anthropic Claude AI API key by: 
1. Signing up at [anthropic.com](https://www.anthropic.com/).
2. Clicking "API Keys" in the top menu.
3. Clicking "Create API Key".

To add billing credits:
1. Click "Billing" in the top menu.
2. Click "Add Credits" to purchase.

More info: [anthropic.com/docs](https://www.anthropic.com/docs)

</p>
</details>


<br>

## Installation

```bash
pip install open-interview
```

```bash
git clone https://github.com/yourusername/InterviewAssistant.git
pip install -r requirements.txt
```

<br>

## Quick Start
These examples show the minimal code required to generate interview content using either the Claude or GPT model. Replace the API keys with your actual keys, and adjust the other parameters as needed.

### Using Claude

```python
from openinterview import InterviewManager

claudeToken = "value"
claude_interview_manager = InterviewManager(api_key=claudeToken, engine="Claude")

claude_interview_manager.generate_interview(
    jd="This role demands a deep enthusiasm for AI development.",
    resume="path/resume.pdf",
    position= "AI Researcher",
    interview_type="techQAsFromResume",
    language="English",
    max_sentence=5,
    output_dir="save/dirs",
)
```

### Using GPT

```python
import openai
from openinterview import InterviewManager

openai.api_key = "value"
gpt_interview_manager = InterviewManager(api_key=openai.api_key, engine="GPT")

gpt_interview_manager.generate_interview(
    jd="This role demands a deep enthusiasm for AI development.",
    resume="path/resume.pdf",
    position= "AI Researcher",
    interview_type="techQAsFromResume",
    language="English",
    max_sentence=5,
    output_dir="save/dirs",
)
```

<br>

## Usage

### OpenAI GPT

1. Import the required modules and instantiate `InterviewGPT` with your OpenAI API key.
    
    ```python
    import openai
    openai.api_key = "value"
    from openinterview import InterviewGPT
    
    gpt_interviewer = InterviewGPT(api_key=openai.api_key)
    ```

2. Provide the job description and resume, set the desired parameters, and call the `generate_interview_content` method to generate the interview content.
    
    ```python
    jd = "This role demands a deep enthusiasm for AI development."
    resume = "I'm a passionate AI engineer. https://github.com/dsdanielpark"
    
    system_prompt = InterviewGPT.create_system_prompt(
        jd=jd,
        candidate_resume=resume,
        position="AI Researcher",
        interview_type="techQAsFromResume",
        language="English",
        max_sentence=6
        )
    
    user_prompt = InterviewGPT.create_base_prompt("generateQAs")
    
    generated_qa_dict = gpt_interviewer.generate_interview_content(
        system_prompt=system_prompt,
        user_prompt=user_prompt,
        iteration=1,
        save_dir="interviews/generated_qa"
    )
    ```

3. You can create Word documents or generate audio files from the generated questions and answers.
    
    ```python
    # Create Word document
    from openinterview import DocumentCreator
    interview_coach = DocumentCreator()
    interview_coach.create_qa_document(generated_qa_dict, "CompanyName", 11, "interviews/documents")
    
    # Generate audio files
    from openinterview import save_google_tts
    save_google_tts(generated_qa_dict, "interviews/audio")
    ```


<br>

### Anthropic Claude

1. Import the required modules and instantiate `InterviewClaude` with your Anthropic API key.
    
    ```python
    from openinterview import InterviewClaude
    
    claudeToken = "value"
    claude_interviewer = InterviewClaude(api_key=claudeToken, engine="Claude")
    ```

2. Provide the job description and resume, set the desired parameters, and call the `generate_interview_content` method to generate the interview content.
    
    ```python
    jd = "This role demands a deep enthusiasm for AI development."
    resume = "I'm a passionate AI engineer. https://github.com/dsdanielpark"
    
    system_prompt = InterviewClaude.create_system_prompt(
        jd=jd,
        candidate_resume=resume,
        position="AI Researcher",
        interview_type="techQAsFromResume",
        language="English",
        max_sentence=6
    )
    
    user_prompt = InterviewClaude.create_base_prompt("generateQAs")
    
    generated_qa_dict = claude_interviewer.generate_interview_content(
        system_prompt=system_prompt,
        user_prompt=user_prompt,
        iteration=1,
        save_dir="interviews/generated_qa"
    )
    ```

3. You can create Word documents or generate audio files from the generated questions and answers.
    
    ```python
    # Create Word document
    from openinterview import DocumentCreator
    interview_coach = DocumentCreator()
    interview_coach.create_qa_document(generated_qa_dict, "CompanyName", 11, "interviews/documents")
    
    # Generate audio files
    from openinterview import save_google_tts
    save_google_tts(generated_qa_dict, "interviews/audio")
    ```


### Playing Random Question Audio

To randomly play `question.mp3` files from a specified folder, create an instance of the `RandomPlayer` class with the folder path, and then invoke `play_random_mp3`:

```python
player = RandomPlayer("path/to/output")  # Directory containing question.mp3 files
player.play_random_mp3()
```