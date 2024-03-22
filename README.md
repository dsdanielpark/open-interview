# Open Interview <img alt="PyPI" src="https://img.shields.io/pypi/v/open-interview?color=black">
Looking to practice mock interviews tailored to your resume and job description? Seeking an technical interview simulation? 
Dive in with the Python open-source package open-interview. 

`$ pip install open-interview`





https://github.com/dsdanielpark/open-interview/assets/81407603/22f9b991-33e8-40d2-a4f2-b80199415767




Transform your job interview preparation into an unparalleled journey with **Open Interview**, where the avant-garde artificial intelligence of OpenAI, Anthropic, and Google is meticulously tailored to forge your path to success. Here, every interaction is designed to sculpt your technical and personal narrative into perfection, mirroring the exigencies of your dream job.



- [Open Interview ](#open-interview-)
  - [Stellar Features](#stellar-features-)
  - [Commencing Voyage](#commencing-voyage)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation-)
    - [Quick Start](#quick-start)
      - [Using Claude](#using-claude)
      - [Using GPT](#using-gpt)
      - [Playing Random Question Audio](#playing-random-question-audio)
    - [Usage](#usage)
  - [Contribution](#contribution)
  - [FAQ \& Support](#faq--support)
  - [License](#license-️)


<br>

## Stellar Features ✨
- **🌍 Universal Language Support:** Emphasize the ability to accommodate all languages across the following features:
- **🖋️ Dynamic Q&A Alchemy:** Craft your arsenal with precision—generate nuanced technical interview Q&As distilled from the essence of your resume and the job description.
- **📖 Document Genesis:** Automate the creation of elegant Word documents (.docx), encapsulating your personalized interview Q&As for study and reflection.
- **🎧 Sonic Refinement:** Convert your Q&As into audio files, enabling auditory mastery and convenience for your preparatory rituals.
- **🌐 Cosmos Customization:** Navigate your preparation through customizable orbits—fine-tune preferences for job designation, interview cadence, lingua franca, and narrative complexity.

<br>

## Commencing Voyage
Welcome to the nexus of your interview preparation odyssey.

> [!IMPORTANT] 
> Token usage for experimental projects can be high, possibly exhausting paid API tokens quickly. A long-response prompt is now active. Please see the document below to adjust system and user prompts accordingly.


### Prerequisites

- **Python >= 3.7:** Ensure your command module is updated to version 3.7 or beyond.
- **🔑 API Keys - OpenAI, Anthropic, Google:** Secure your access to the galaxies of OpenAI, Anthropic, and Google, embarking with the keys to unlock the full spectrum of your potential. 




### Installation 📦

```bash
pip install open-interview
```
```
git clone https://github.com/dsdanielpark/open-interview.git
pip install -r requirements.txt
```

<br>


### Quick Start   

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1NWCwuunRRR2C2b0vmYk6Tm-JxV4yzSt9#scrollTo=bebO3UiGbIaD) 





Generate interview content using Claude or GPT models with minimal setup:

#### Using Claude

> [!IMPORTANT] 
> Increasing the `iteration` argument can generate more QAs but may lead to duplicates and excessive token usage, as it's an experimental feature.


```python
from openinterview import InterviewManager

claudeToken = "<your_claude_token>"
claude_interview_manager = InterviewManager(api_key=claudeToken, engine="Claude")

jd = """
The 'jd', 'resume', and other arguments
can accommodate extensive text.
"""

claude_interview_manager.generate_interview(
    jd=jd,
    resume="path/resume.pdf or path/resume.txt or long text.",
    position= "AI Researcher",
    interview_type="techQAsFromResume",
    language="English", # Any language you want
    max_sentence=5,
    output_dir="save/dirs",
    iteration=1, # [Caution] You can make more QAs, But it cost token very fastly.
)
```

#### Using GPT

```python
import openai
from openinterview import InterviewManager

openai.api_key = "<your_openai_token>"
gpt_interview_manager = InterviewManager(api_key=openai.api_key, engine="GPT")

gpt_interview_manager.generate_interview(
    jd="This role demands a deep enthusiasm for AI development.", # Feasible for long text
    resume="path/resume.pdf or path/resume.txt or long text.",
    position= "AI Researcher",
    interview_type="techQAsFromResume",
    language="English", # Any language you want
    max_sentence=5,
    output_dir="save/dirs",
    iteration=1, # [Caution] You can make more QAs, But it cost token very fastly.
)
```



Interview_type arguments as follow:
  - *generalQAs*: Ask about technical and personal skills in-depth.
  - *generalTechQAs*: Ask basic professional questions related to the job.
  - *techQAsFromResume*: Focus on technical skills listed on the resume.
  - *techQAsFromExperts*: Questions based on interviewer's expertise.
  - *techQAs*: Questions based on both parties' experiences.
  - *personalityQAs*: Inquire about personal qualities.
  - *reviewResume*: Identify and suggest improvements for the resume.


#### Playing Random Question Audio

To randomly play `question.mp3` files from a specified folder, create an instance of the `RandomPlayer` class with the folder path, and then invoke `play_random_mp3`:

```python
from openinterview import RandomPlayer

player = RandomPlayer(directory="path/to/output", interval=120)  # Directory containing question.mp3 files
player.play_random_mp3()
```
Default plays randomly for 2 minutes. Press 'n' for next question, 'q' to quit.

<br>

### Usage

For detailed examples, refer to the 📋[Usage document for example code and prompting engineering](https://github.com/dsdanielpark/open-interview/blob/main/docs/usage.md) or the 💻[tutorial script](https://github.com/dsdanielpark/open-interview/blob/main/script/example.ipynb).

- OpenAI GPT: Use `InterviewGPT` for GPT-based content generation.
- Anthropic Claude: Use `InterviewClaude` for Claude-based interviews.
<br>

## Contribution
For detailed guidance on contributions, please refer to the [contribution guide](https://github.com/dsdanielpark/open-interview/blob/main/docs/contributions.md). We appreciate your interest in contributing and look forward to your valuable input. 

Thank you for supporting our project.

## FAQ & Support

For questions and support, visit our [FAQ](https://github.com/dsdanielpark/open-interview/blob/main/documents/faq.md) and [Issues](https://github.com/dsdanielpark/open-interview/issues) pages. Contributors are welcome! Submit issues, feature suggestions, or pull requests.
Reach out to the core maintainer, [Daniel Park](https://github.com/DSDanielPark), for direct contributions or queries.


## License ©️ 
[Apache 2.0](https://opensource.org/license/apache-2-0) license, 2024. 


