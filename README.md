# LangChain Hello World

A starter project demonstrating how to use [LangChain](https://www.langchain.com/) with OpenAI's GPT models to build an interactive, conversational AI pipeline in Python.

## Overview

This project builds a multi-turn chat pipeline structured in four layers:

1. **Validate** — checks via LLM whether the input is a real person or public personality before doing anything else; re-prompts if not
2. **Load** — fetches up to 5 Wikipedia articles and combines them into a single context string
3. **Profile** — constructs an LCEL chain (`PromptTemplate | ChatOpenAI`) to generate an initial markdown-formatted profile
4. **Converse** — enters an interactive loop supporting follow-up questions, new person lookups, and graceful exit

The generated profile has four sections:
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

### Interactive commands

| Input | Action |
|---|---|
| Any text | Ask a follow-up question about the current person |
| `new` | Look up a different person (resets conversation) |
| `exit` / `bye` / `quit` | Exit the program |
| `Ctrl+C` | Exit the program |

### Example session

```
Enter a person's name to look up: XAUUSD
'XAUUSD' doesn't seem to be a person. Please enter a valid name.
Enter a person's name to look up: Elon Musk

--- Wikipedia preview for 'Elon Musk' ---
...

## 1. Background Summary
...

You: What companies has he founded?
Assistant: ...

You: new
Enter a person's name to look up: bye
'bye' doesn't seem to be a person. Please enter a valid name.
Enter a person's name to look up: Marie Curie
...

You: bye
Goodbye!
```

## Code Structure

| Component | Location | Purpose |
|---|---|---|
| `PROMPT_TEMPLATE` | `main.py` (module level) | Markdown prompt defining the four profile sections |
| `is_person()` | `main.py` | LLM-based validator — returns `True` only for real people/personalities |
| `load_wikipedia_info()` | `main.py` | Fetches and combines up to 5 Wikipedia articles |
| `generate_profile()` | `main.py` | Runs the initial chain and seeds the conversation history |
| `main()` | `main.py` | Orchestrates validation, lookup, and the follow-up chat loop |

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
├── main.py          # PROMPT_TEMPLATE, loader, profile generator, and chat loop
├── pyproject.toml   # Project metadata and dependencies
├── uv.lock          # Locked dependency versions
└── .env             # API keys (not committed)
```
