import re
from setuptools import find_packages, setup


def read(file_path, version=False):
    with open(file_path, encoding="UTF-8") as f:
        content = f.read()
    if version:
        match = re.search(r"""^__version__ = ['"]([^'"]*)['"]""", content, re.M)
        if not match:
            raise RuntimeError(f"{file_path} doesn't contain __version__")
        return match.group(1)
    return content


setup(
    name="open-interview",
    version=read("openinterview/__init__.py", version=True),
    author="Daniel Park",
    author_email="parkminwoo1991@gmail.com",
    description="The python package that returns Response of Google Gemini through API.",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/dsdanielpark/open-interview",
    packages=find_packages(exclude=[]),
    python_requires=">=3.7",
    install_requires=[
        "openai==0.28",
        "anthropic",
        "python-docx",
        "utilfunction",
        "python-gemini-api",
        "lxml",
        "gTTS",
        "SpeechRecognition",
        "PyPDF2",
        "pygame",
    ],
    extras_require={
        "openaivoice": [
            "openai",
        ]
    },
    keywords="Interview, LLM, ChatGPT, OpenAI, Claude, Anthropic",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
