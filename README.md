
# Open Interview

Open Interview Assistant simplifies your job interview preparation by leveraging AI technology from leading platforms like OpenAI, Anthropic, and Google. It generates relevant technical interview questions and answers tailored to your job description and resume.

## Features

- 📄 Automatic Q&A Generation: Create technical interview questions and answers from job descriptions and resumes.
- 🗂 Document Creation: Generate Word documents (.docx) with the interview Q&A.
- 🔊 Audio Files: Convert Q&A into audio files for listening practice.
- ⚙️ Customizable Parameters: Adjust settings like job position, interview type, language, and sentence length.

<br>


## Getting Started

### Prerequisites

- Python 3.7 or later.
- API keys from OpenAI, Anthropic, and Google.


### Installation

```bash
pip install open-interview
```
```
git clone https://github.com/yourusername/InterviewAssistant.git
pip install -r requirements.txt
```

<br>


### Quick Start

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

### Usage

Check the [Usage example code document](https://github.com/dsdanielpark/open-interview/blob/main/docs/usage.md) for detailed examples.

- OpenAI GPT: Use `InterviewGPT` for GPT-based content generation.
- Anthropic Claude: Use `InterviewClaude` for Claude-based interviews.

<br>

## FAQ & Support

For questions and support, visit our [FAQ](https://github.com/dsdanielpark/open-interview/blob/main/documents/README_FAQ.md) and [Issues](https://github.com/dsdanielpark/open-interview/issues) pages. Contributors are welcome! Submit issues, feature suggestions, or pull requests.
Reach out to the core maintainer, [Daniel Park](https://github.com/DSDanielPark), for direct contributions or queries.


## License ©️ 
[Apache 2.0](https://opensource.org/license/apache-2-0) license, 2024. 


