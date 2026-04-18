"""
LangChain Hello World — Person Profile Generator

Demonstrates a minimal LangChain pipeline:
  1. Define a prompt template with a placeholder variable ({information})
  2. Bind the template to an OpenAI chat model (gpt-4o-mini)
  3. Invoke the chain with real text and print the structured response

Environment:
  Requires OPENAI_API_KEY set in a .env file (loaded via python-dotenv).

Usage:
  uv run main.py
"""

from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import WikipediaLoader

# Load OPENAI_API_KEY (and any other vars) from .env into os.environ
load_dotenv(override=True)

def load_wikipedia_info(topic: str) -> str:
    """Load a biography from Wikipedia given a topic string."""
    loader = WikipediaLoader(query=topic, load_max_docs=5)
    documents = loader.load()
    return "\n\n".join(doc.page_content for doc in documents)

PROMPT_TEMPLATE = """
You are a helpful assistant. Using the information below about a person, produce a
well-formatted profile with the following sections. Use markdown: a `##` heading for
each section, and bullet points for lists.

## Information
{information}

---

## 1. Background Summary
A short paragraph summarising the person's background and interests.

## 2. Conversation Topics
A bullet list of topics that would be relevant and interesting to discuss with this person.

## 3. Questions to Learn More
A bullet list of questions to explore the person's background and interests.

## 4. Follow-Up Questions
A bullet list of follow-up questions based on likely responses to the questions above.
"""


def main():
    print("Hello from langchain-helloworld!")

    # 1. Get topic and load Wikipedia content
    topic = input("Enter a person's name to look up: ")
    information = load_wikipedia_info(topic)
    print(f"\n--- Wikipedia preview for '{topic}' ---\n{information[:2000]}...\n")

    # 2. Build the LCEL chain: prompt → LLM
    prompt = PromptTemplate(input_variables=["information"], template=PROMPT_TEMPLATE)
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
    chain = prompt | llm

    # 3. Invoke and print the formatted profile
    response = chain.invoke({"information": information})
    print(response.content)

if __name__ == "__main__":
    main()
