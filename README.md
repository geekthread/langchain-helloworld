# LangChain Hello World

A starter project demonstrating how to use [LangChain](https://www.langchain.com/) with OpenAI's GPT models to build prompt-driven AI pipelines in Python.

## Overview

This project builds a minimal LangChain pipeline structured in three clear steps:

1. **Load** — prompts the user for a name, fetches up to 5 Wikipedia articles, and combines them into a single context string
2. **Build** — constructs an LCEL chain (`PromptTemplate | ChatOpenAI`) using a module-level prompt template (`PROMPT_TEMPLATE`)
3. **Invoke** — runs the chain and prints a markdown-formatted profile with four sections:
   - **Background Summary** — short paragraph on the person's background and interests
   - **Conversation Topics** — bullet list of relevant topics to discuss
   - **Questions to Learn More** — bullet list of exploratory questions
   - **Follow-Up Questions** — bullet list of follow-ups based on likely responses

A preview of the raw Wikipedia content (first 2000 chars) is printed before the profile.

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

You will be prompted to enter a person's name. The script will then fetch Wikipedia content, print a preview, and output a structured markdown profile via `gpt-4o-mini`.

## Code Structure

| Component | Location | Purpose |
|---|---|---|
| `PROMPT_TEMPLATE` | `main.py` (module level) | Markdown prompt defining the four profile sections |
| `load_wikipedia_info()` | `main.py` | Fetches and combines up to 5 Wikipedia articles |
| `main()` | `main.py` | Orchestrates input → load → build → invoke |

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
├── main.py          # PROMPT_TEMPLATE constant, loader, and main chain logic
├── pyproject.toml   # Project metadata and dependencies
├── uv.lock          # Locked dependency versions
└── .env             # API keys (not committed)
```
