# LangChain Hello World

A starter project demonstrating how to use [LangChain](https://www.langchain.com/) with OpenAI's GPT models to build prompt-driven AI pipelines in Python.

## Overview

This project uses a `PromptTemplate` and `ChatOpenAI` to construct a LangChain chain that takes biographical information about a person and generates a comprehensive profile including:

- Background summary
- Conversation topics and questions
- Recommended resources, activities, and connections
- Career opportunities and potential challenges
- Goals, values, personality traits, and communication/learning styles

## Prerequisites

- Python >= 3.14
- [uv](https://github.com/astral-sh/uv) (package manager)
- An OpenAI API key

## Setup

1. Clone the repository and navigate to the project directory.

2. Install dependencies:
   ```bash
   uv sync
   ```

3. Create a `.env` file in the project root and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

```bash
uv run main.py
```

The script will generate a detailed profile for the sample input (Jeff Bezos) using `gpt-4o-mini`.

## Dependencies

| Package | Purpose |
|---|---|
| `langchain` | Core LangChain framework |
| `langchain-openai` | OpenAI integration for LangChain |
| `langchain-anthropic` | Anthropic/Claude integration |
| `langchain-google-genai` | Google Gemini integration |
| `anthropic` | Anthropic SDK |
| `python-dotenv` | Load environment variables from `.env` |
| `ruff` | Linting |
| `black` | Code formatting |
| `isort` | Import sorting |

## Project Structure

```
langchain-helloworld/
├── main.py          # Entry point with prompt template and LangChain chain
├── pyproject.toml   # Project metadata and dependencies
├── uv.lock          # Locked dependency versions
└── .env             # API keys (not committed)
```
