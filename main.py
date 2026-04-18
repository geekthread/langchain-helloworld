"""
LangChain Hello World — Person Profile Generator

Demonstrates a minimal LangChain pipeline:
  1. Define a prompt template with a placeholder variable ({information})
  2. Bind the template to an OpenAI chat model (gpt-4o-mini)
  3. Invoke the chain with real text and print the structured response
  4. Support follow-up questions, new person lookups, and graceful exit

Environment:
  Requires OPENAI_API_KEY set in a .env file (loaded via python-dotenv).

Usage:
  uv run main.py
"""

from dotenv import load_dotenv

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import WikipediaLoader

load_dotenv(override=True)

EXIT_KEYWORDS = {"bye", "exit", "quit"}

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


def is_person(topic: str, llm: ChatOpenAI) -> bool:
    """Return True if the input looks like a real person or public personality."""
    response = llm.invoke([
        SystemMessage(content="You are a strict classifier. Reply with only 'yes' or 'no'."),
        HumanMessage(content=f"Is '{topic}' the name of a real person or public personality?"),
    ])
    return response.content.strip().lower().startswith("yes")


def load_wikipedia_info(topic: str) -> str:
    """Fetch and combine up to 5 Wikipedia articles for the given topic."""
    loader = WikipediaLoader(query=topic, load_max_docs=5)
    documents = loader.load()
    return "\n\n".join(doc.page_content for doc in documents)


def generate_profile(topic: str, information: str, llm: ChatOpenAI) -> list:
    """Generate the initial profile and return the seeded conversation history."""
    prompt = PromptTemplate(input_variables=["information"], template=PROMPT_TEMPLATE)
    chain = prompt | llm
    response = chain.invoke({"information": information})
    print(response.content)

    # Seed history so follow-ups have full context
    return [
        SystemMessage(content=f"You are a helpful assistant. The user is asking about {topic}. "
                               f"Here is the reference information:\n\n{information}"),
        HumanMessage(content="Generate a structured profile for this person."),
        AIMessage(content=response.content),
    ]


def main():
    print("Type 'new' to look up a different person, or 'exit'/'bye' to quit.\n")

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

    def lookup(topic: str) -> tuple[str, list] | None:
        if not is_person(topic, llm):
            print(f"'{topic}' doesn't seem to be a person. Please enter a valid name.")
            return None
        information = load_wikipedia_info(topic)
        history = generate_profile(topic, information, llm)
        return information, history

    while True:
        topic = input("Enter a person's name to look up: ").strip()
        result = lookup(topic)
        if result:
            _, history = result
            break

    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            return

        if not user_input:
            continue

        if user_input.lower() in EXIT_KEYWORDS:
            print("Goodbye!")
            return

        if user_input.lower() == "new":
            while True:
                topic = input("Enter a person's name to look up: ").strip()
                result = lookup(topic)
                if result:
                    _, history = result
                    break
            continue

        # Follow-up question — send full history + new message
        history.append(HumanMessage(content=user_input))
        response = llm.invoke(history)
        print(f"\nAssistant: {response.content}")
        history.append(AIMessage(content=response.content))


if __name__ == "__main__":
    main()
