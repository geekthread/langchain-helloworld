# LangChain Hello World

A starter project demonstrating how to use [LangChain](https://www.langchain.com/) with OpenAI's GPT models to build prompt-driven AI pipelines in Python.

## Overview

This project uses a `PromptTemplate` and `ChatOpenAI` to construct a LangChain chain that:

1. Prompts the user to enter a person's name
2. Fetches their biography from Wikipedia via `WikipediaLoader`
3. Passes the content through a GPT-4o-mini chain to generate a profile including:
   - Background summary
   - Relevant conversation topics
   - Initial questions to learn more about the person
   - Follow-up questions based on expected responses

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

The script will prompt you to enter a person's name, fetch their Wikipedia biography, and generate a structured profile using `gpt-4o-mini`.

## Dependencies

| Package | Purpose |
|---|---|
| `langchain` | Core LangChain framework |
| `langchain-openai` | OpenAI integration for LangChain |
| `langchain-community` | Community integrations including `WikipediaLoader` |
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
