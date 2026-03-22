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

# Load OPENAI_API_KEY (and any other vars) from .env into os.environ
load_dotenv()


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

    # --- Sample input biography -------------------------------------------
    # Replace this with any person's biography to generate a new profile.
    information = """
   Jeffrey Preston Bezos (/ˈbeɪzoʊs/ BAY-zohss;[2] né Jorgensen; born January 12, 1964) is an American businessman best known as the founder, executive chairman, and former president and CEO of Amazon, the world's largest e-commerce and cloud computing company. According to Forbes, as of December 2025, Bezos's estimated net worth is US$239.4 billion, making him the fourth richest person in the world.[3] He was the wealthiest person from 2017 to 2021, according to Forbes and the Bloomberg Billionaires Index.[4]

 Bezos was born in Albuquerque, and raised in Houston and Miami. He graduated from Princeton University in 1986 with a degree in engineering. He worked on Wall Street in a variety of related fields from 1986 to early 1994. Bezos founded Amazon in mid-1994 on a road trip from New York City to Seattle. The company began as an online bookstore and has since expanded to a variety of other e-commerce products and services, including video and audio streaming, cloud computing, and artificial intelligence. It is the world's largest online sales company, the largest Internet company by revenue, and the largest provider of virtual assistants and cloud infrastructure services through its Amazon Web Services branch.

 Bezos founded the aerospace manufacturer and sub-orbital spaceflight services company Blue Origin in 2000. Blue Origin's New Shepard vehicle reached space in 2015 and afterwards successfully landed back on Earth; he flew into space on Blue Origin NS-16 in 2021. He purchased the major American newspaper The Washington Post in 2013 for $250 million (equivalent to $345,535,714 in 2025) and manages many other investments through his venture capital firm, Bezos Expeditions. In September 2021, Bezos co-founded Altos Labs with Mail.ru founder Yuri Milner.[5]

 The first centibillionaire on the Forbes Real Time Billionaires Index and the second ever to have achieved the feat since Bill Gates in 1999, Bezos was named the "richest man in modern history" after his net worth increased to $150 billion in July 2018 (equivalent to $192,320,434,667 in 2025).[6] In August 2020, according to Forbes, he had a net worth exceeding $200 billion (equivalent to $248,810,595,345 in 2025). On July 5, 2021, Bezos stepped down as the CEO and president of Amazon and took over the role of executive chairman. Amazon Web Services CEO Andy Jassy succeeded Bezos as the CEO and president of Amazon.
 """
 
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
