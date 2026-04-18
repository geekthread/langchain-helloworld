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
load_dotenv()

def load_wikipedia_info(topic: str) -> str:
    """Load a biography from Wikipedia given a topic string."""
    loader = WikipediaLoader(query=topic, load_max_docs=2)
    documents = loader.load()
    return documents[0].page_content if documents else ""

def main():
    """Build and invoke a LangChain prompt→LLM chain for a given person biography."""
    print("Hello from langchain-helloworld!")

    # --- Prompt template --------------------------------------------------
    # Uses LangChain's PromptTemplate to inject `information` at runtime.
    # The template asks the LLM to produce 14 structured sections about a person.
    prompt_template_str = """
     Given the following information , about a personon {information}, please
     provide:
     1.  A short summary of the person's background and interests.
     2.  A list of potential topics that would be relevant and interesting to discuss with this person.
     3.  A list of questions that could be asked to learn more about this person's background and interests.
     4.  A list of potential follow-up questions based on the person's responses to the initial questions.
    """

    # --- Load biography from Wikipedia ------------------------------------
    topic = input("Enter a person's name to look up: ")
    information = load_wikipedia_info(topic)
 
    # --- Build the chain --------------------------------------------------
    # PromptTemplate compiles the string template and validates input variables.
    prompt_template = PromptTemplate(
        input_variables=["information"],
        template=prompt_template_str,
    )

    # ChatOpenAI wraps the OpenAI chat completions API.
    # temperature=0.7 balances creativity vs. determinism (0 = deterministic, 1 = most random).
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

    # The `|` operator creates a LangChain Expression Language (LCEL) chain:
    # prompt_template formats the input → llm generates the response.
    chain = prompt_template | llm

    # Invoke the chain; returns an AIMessage whose .content holds the text.
    response = chain.invoke({"information": information})
    print(response)

if __name__ == "__main__":
    main()
