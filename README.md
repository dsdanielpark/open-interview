# Open Interview <img alt="PyPI" src="https://img.shields.io/pypi/v/open-interview?color=black">

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
  - [FAQ \& Support](#faq--support)
  - [License ©️](#license-️)


<br>

## Stellar Features ✨

- **🖋️ Dynamic Q&A Alchemy:** Craft your arsenal with precision—generate nuanced technical interview Q&As distilled from the essence of your resume and the job description.
- **📖 Document Genesis:** Automate the creation of elegant Word documents (.docx), encapsulating your personalized interview Q&As for study and reflection.
- **🎧 Sonic Refinement:** Convert your Q&As into audio files, enabling auditory mastery and convenience for your preparatory rituals.
- **🌐 Cosmos Customization:** Navigate your preparation through customizable orbits—fine-tune preferences for job designation, interview cadence, lingua franca, and narrative complexity.

<br>

## Commencing Voyage
Welcome to the nexus of your interview preparation odyssey.


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

```python
from openinterview import InterviewManager

claudeToken = "<your_claude_token>"
interview_manager = InterviewManager(api_key=claudeToken, engine="Claude")

# Generate and save interview content
interview_manager.generate_interview(...)
```

#### Using GPT

```python
from openinterview import InterviewManager

openai.api_key = "<your_gpt_token>"
interview_manager = InterviewManager(api_key=openai.api_key, engine="GPT")

# Generate and save interview content
interview_manager.generate_interview(...)
```

#### Playing Random Question Audio

To randomly play `question.mp3` files from a specified folder, create an instance of the `RandomPlayer` class with the folder path, and then invoke `play_random_mp3`:

```python
player = RandomPlayer("path/to/output")  # Directory containing question.mp3 files
player.play_random_mp3()
```
Default plays randomly for 2 minutes. Press 'n' for next question, 'q' to quit.

<br>

### Usage

For detailed examples, refer to the 📋[Usage example code document](https://github.com/dsdanielpark/open-interview/blob/main/docs/usage.md) or the 💻[tutorial script](https://github.com/dsdanielpark/open-interview/blob/main/script/example.ipynb).

- OpenAI GPT: Use `InterviewGPT` for GPT-based content generation.
- Anthropic Claude: Use `InterviewClaude` for Claude-based interviews.

<br>

## FAQ & Support

For questions and support, visit our [FAQ](https://github.com/dsdanielpark/open-interview/blob/main/documents/faq.md) and [Issues](https://github.com/dsdanielpark/open-interview/issues) pages. Contributors are welcome! Submit issues, feature suggestions, or pull requests.
Reach out to the core maintainer, [Daniel Park](https://github.com/DSDanielPark), for direct contributions or queries.


## License ©️ 
[Apache 2.0](https://opensource.org/license/apache-2-0) license, 2024. 


