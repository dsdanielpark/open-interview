
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
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1NWCwuunRRR2C2b0vmYk6Tm-JxV4yzSt9#scrollTo=bebO3UiGbIaD) 


These examples show the minimal code required to generate interview content using either the Claude or GPT model. Replace the API keys with your actual keys, and adjust the other parameters as needed.



> [!IMPORTANT] 
> Increasing the `iteration` argument can generate more QAs but may lead to duplicates and excessive token usage, as it's an experimental feature.



### Using Claude


```python
from openinterview import InterviewManager

claudeToken = "<your_claude_token>"
claude_interview_manager = InterviewManager(api_key=claudeToken, engine="Claude")

jd = """
The 'jd', 'resume', and other arguments
can accommodate extensive text.
"""

resume = """
Very long text can be pasted in here.
"""

claude_interview_manager.generate_interview(
    jd=jd,
    resume=resume,
    position= "AI Researcher",
    interview_type="techQAsFromResume",
    language="English", # Any language you want
    max_sentence=5,
    output_dir="save/dirs",
    iteration=1, # [Caution] You can make more QAs, But it cost token very fastly.
)
```

### Using GPT

```python
import openai
from openinterview import InterviewManager

openai.api_key = "<your_openai_token>"
gpt_interview_manager = InterviewManager(api_key=openai.api_key, engine="GPT")

gpt_interview_manager.generate_interview(
    jd="This role demands a deep enthusiasm for AI development.", # Feasible for long text
    resume="path/resume.pdf or path/resume.txt or long text",
    position= "AI Researcher",
    interview_type="techQAsFromResume",
    language="English", # Any language you want
    max_sentence=5,
    output_dir="save/dirs",
    iteration=1, # [Caution] You can make more QAs, But it cost token very fastly.
)
```

### Playing Random Question Audio

To randomly play `question.mp3` files from a specified folder, create an instance of the `RandomPlayer` class with the folder path, and then invoke `play_random_mp3`:

```python
player = RandomPlayer(directory="path/to/output", interval=120)  # Directory containing question.mp3 files
player.play_random_mp3()
```
Default plays randomly for 2 minutes. Press 'n' for next question, 'q' to quit.

<br>

## Usage

You can also execute the strongly wrapped above step by step, especially noting how the prompt in section 2 is generated.

> [!TIP] 
> When using specific models in Claude, GPT, and Gemini, you may need to re-engineer prompts based on the detailed codes' system_prompt and user_prompt outputs to create the desired documents.

### OpenAI GPT

1. Import the required modules and instantiate `InterviewGPT` with your OpenAI API key.
    
    ```python
    import openai
    from openinterview import InterviewGPT
    
    openai.api_key = "value"
    
    gpt_interviewer = InterviewGPT(api_key=openai.api_key)
    ```

2. Provide the job description and resume, set the desired parameters, and generate system and user prompts in the following format. Check the generated prompts and modify as needed. You can create the desired prompt through a few attempts via web or API.

    https://github.com/dsdanielpark/open-interview/blob/f0770da7a473f595f66df93c9eea2af5d6721595/openinterview/models/claude.py#L141
    

    ```python
    from openinterview import InterviewGPT
    
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
    print(system_prompt)

    user_prompt = InterviewGPT.create_base_prompt("generateQAs")
    print(user_prompt)
    ```
    
3. Call the `generate_interview_content` method to generate the interview content.    
    ``` 
    generated_qa_dict = gpt_interviewer.generate_interview_content(
        system_prompt=system_prompt,
        user_prompt=user_prompt,
        iteration=1,
        save_dir="interviews/generated_qa"
    )
    ```

4. You can create Word documents or generate audio files from the generated questions and answers.
    
    ```python
    # Create Word document
    from openinterview import DocumentCreator
    interview_coach = DocumentCreator()
    interview_coach.create_qa_document(generated_qa_dict, "TeamViewer15", 11, "interviews/documents")
    
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
2. Provide the job description and resume, set the desired parameters, and generate system and user prompts in the following format. Check the generated prompts and modify as needed. You can create the desired prompt through a few attempts via web or API.

    https://github.com/dsdanielpark/open-interview/blob/f0770da7a473f595f66df93c9eea2af5d6721595/openinterview/models/gpt.py#L144

    ```python
    from openinterview import InterviewGPT

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
    print(system_prompt)
    
    user_prompt = InterviewClaude.create_base_prompt("generateQAs")
    print(user_prompt)
    ```

3. Call the `generate_interview_content` method to generate the interview content.
    ```python
    generated_qa_dict = claude_interviewer.generate_interview_content(
        system_prompt=system_prompt,
        user_prompt=user_prompt,
        iteration=1,
        save_dir="interviews/generated_qa"
    )
    ```

4. You can create Word documents or generate audio files from the generated questions and answers.
    
    ```python
    # Create Word document
    from openinterview import DocumentCreator
    interview_coach = DocumentCreator()
    interview_coach.create_qa_document(generated_qa_dict, "TeamViewer15", 11, "interviews/documents")
    
    # Generate audio files
    from openinterview import save_google_tts
    save_google_tts(generated_qa_dict, "interviews/audio")
    ```
    
<br>

### Playing Random Question Audio

To randomly play `question.mp3` files from a specified folder, create an instance of the `RandomPlayer` class with the folder path, and then invoke `play_random_mp3`:

```python
player = RandomPlayer(directory="path/to/output", interval=120)  # Directory containing question.mp3 files
player.play_random_mp3()
```

<br>

## Prompt engineering

You can achieve your goals by directly utilizing the system_prompt and user_prompt based on the following information.

> [!NOTE]
> OpenAI defaults to `gpt-3.5-turbo`, while Claude's standard is `claude-3-opus-20240229` with a 4096 token limit. Given the importance of crafting model-specific prompts, the `InterviewGPT` and `InterviewClaude` classes incorporate a static method for prompt generation. However, I've provided separate examples in [prompter.py](https://github.com/dsdanielpark/open-interview/blob/main/openinterview/utils/prompter.py). Should you opt for different models, it's advisable to adapt your prompt engineering accordingly. For further information, you can visit [Open AI - Models](https://platform.openai.com/docs/models) and [Anthropic - Models](https://docs.anthropic.com/claude/docs/models-overview).

### **System Prompt:**
- The system prompt is generated based on information such as `position`, `interview_type`, `jd`, `language`, `candidate_resume`, `interviewer_resume`, `max_sentence`, `custom_prompt`, etc.
    - `position`            : Refers to AI researcher or the specific job role.                                             
    - `jd`                  : Represents the job description.                                                               
    - `interview_type`      : Indicates the type of interview. Default is 'generalQAs'.                                      
    - `language`            : Specifies the language to be used. Default is English.                                         
    - `candidate_resume`    : Represents the resume of the candidate.                                                       
    - `interviewer_resume`  : Represents the resume of the interviewer.                                                     
    - `max_sentence`        : Specifies the minimum number of sentences to be included in each answer. Default is 10.       
    - `custom_prompt`       : Provides user-defined additional instructions.                                                

- It includes specific instructions tailored to the user's role and interview type.
- Additionally, any additional user-defined instructions are also incorporated into the system prompt.
    | Type               | Prompt Content                                                                                                                                                                                                                                          |
    |--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | System Prompt      | - **Basic Information:** Generated based on Position, Interview Type, JD, Language, Candidate Resume, Interviewer Resume, Max Sentence, etc. <br>- **Additional Instructions by Interview Type:** Includes specific instructions based on Interview Type (e.g., `generalQAs`, `generalTechQAs`, `techQAsFromResume`, `techQAsFromExperts`, `techQAs`, `personalityQAs`, `reviewResume`, etc.).<br>- **Additional Instructions:** If a custom_prompt provided by the user exists, it is included in the prompt returned.                                            |

### **User Prompt:**
- User prompts vary depending on the interviewer's role.
- Specific instructions for each type of interview are provided.
- Additional instructions, such as highlighting specific sections of the resume, may also be included based on the interviewer's role.

    | Type               | Prompt Content                                                                                                                                                                                                                                          |
    |--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | User Prompt        | - **User Instructions by Interview Type:** Provides user instructions specific to Interview Type (e.g., `generateQs`, `generateQAs`, `pointOutResume`, `adviceResume`, etc.). <br>- **Prompt Format:** Returned in text format containing given arguments and specific instructions.                                                                                                                                              |
    



