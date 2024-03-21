# Open Interview
Open Interview Assistant simplifies your job interview preparation by leveraging AI technology from leading platforms like OpenAI, Anthropic, and Google. It generates relevant technical interview questions and answers tailored to your job description and resume.

## Features

- 📄 Generate technical interview Q&A from job description and resume 
- 🗂 Create Word docs (.docx) from generated Q&A
- 🔊 Generate audio files (text-to-speech) for Q&A
- ⚙️ Customize parameters like job position, interview type, language, sentence length, etc.



- [Open Interview](#open-interview)
  - [Features](#features)
  - [Prerequisites](#prerequisites)
    - [OpenAI API Key and Credits](#openai-api-key-and-credits)
    - [Anthropic API Key and Credits](#anthropic-api-key-and-credits)
  - [Installation](#installation)
  - [Quick Start](#quick-start)
    - [Using Claude](#using-claude)
    - [Using GPT](#using-gpt)
  - [Usage](#usage)
    - [OpenAI GPT](#openai-gpt)
    - [Anthropic Claude](#anthropic-claude)
  - [FAQ](#faq)
  - [Issues](#issues)
  - [Contributors](#contributors)
  - [Contacts](#contacts)
  - [License ©️](#license-️)




## Prerequisites

- Python 3.7+
- API key from OpenAI, Anthropic, and Google.


<details><summary>OpenAI API Key and Credits</summary>

You can get an OpenAI API Key 1. Sign up or log in to your OpenAI account. 2. Navigate to the API section. 3. Follow the instructions to generate a new API key. For detailed steps, visit [OpenAI API Documentation](https://beta.openai.com/docs/api-reference/authentication). To add billing credits: 1. Go to the Billing section in your OpenAI account. 2. Choose to add credits or update your billing method. For more information on managing billing and credits, check out [OpenAI Billing FAQ](https://help.openai.com/en/articles/5726858-billing-faq).
</details>

<details>
<summary>Anthropic API Key and Credits</summary>

You can get an Claude AI API key by: 1. Sign up at [anthropic.com](https://www.anthropic.com/) 2. Click "API Keys" in the top menu 3. Click "Create API Key" To add billing credits: 1. Click "Billing" in top menu 2. Click "Add Credits" to purchase More info: [anthropic.com/docs](https://www.anthropic.com/docs)
</details>

## Installation

```bash
pip install open-interview
```

```bash
git clone https://github.com/yourusername/InterviewAssistant.git
pip install -r requirements.txt
```

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
    from openinterview import save_qa_as_tts
    save_qa_as_tts(generated_qa_dict, "interviews/audio")
    ```

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
    from openinterview import save_qa_as_tts
    save_qa_as_tts(generated_qa_dict, "interviews/audio")
    ```


## [FAQ](https://github.com/dsdanielpark/open-interview/blob/main/documents/README_FAQ.md)

You can find most help on the [FAQ](https://github.com/dsdanielpark/open-interview/blob/main/documents/README_FAQ.md) and [Issue](https://github.com/dsdanielpark/open-interview/issues) pages. 


            
## [Issues](https://github.com/dsdanielpark/open-interview/issues)
Sincerely grateful for any reports on new features or bugs. Your valuable feedback on the code is highly appreciated. Both [Issue reports](https://github.com/dsdanielpark/Gemini-API/issues) and [Pull requests](https://github.com/dsdanielpark/Gemini-API/pulls) contributing to improvements are always welcome. 




## Contributors
Contributions are welcome! Feel free to submit issues or pull requests. We strive to maintain an active and courteous open community.


## Contacts

Core maintainer:

- [Daniel Park](https://github.com/DSDanielPark) / parkminwoo1991@gmail.com
 


## License ©️ 
[Apache 2.0](https://opensource.org/license/apache-2-0) license, 2024. 
<br>
