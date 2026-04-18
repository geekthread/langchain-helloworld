# LangChain Hello World

A starter project demonstrating how to use [LangChain](https://www.langchain.com/) with OpenAI's GPT models to build prompt-driven AI pipelines in Python.

## Overview

This project uses a `PromptTemplate` and `ChatOpenAI` to construct a LangChain chain that:

1. Prompts the user to enter a person's name
2. Fetches their biography from Wikipedia via `WikipediaLoader`
3. Fetches up to 5 Wikipedia documents and combines them for richer context
4. Passes the combined content through a GPT-4o-mini chain to generate a formatted profile with markdown headings:
   - **Background Summary** — short paragraph on the person's background and interests
   - **Conversation Topics** — bullet list of relevant topics to discuss
   - **Questions to Learn More** — bullet list of exploratory questions
   - **Follow-Up Questions** — bullet list of follow-ups based on likely responses

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

The script will prompt you to enter a person's name, fetch up to 5 Wikipedia articles for that topic, and generate a markdown-formatted profile using `gpt-4o-mini`. A preview of the raw Wikipedia content (first 2000 chars) is printed before the profile.

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
