from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
import os

load_dotenv()

OPENAI_BASE_URL = os.environ.get("OPENAI_BASE_URL")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
OPENAI_MODEL_NAME = os.environ.get("OPENAI_MODEL_NAME")

llm = ChatOpenAI(
    base_url=OPENAI_BASE_URL,
    temperature=0,
    model=OPENAI_MODEL_NAME,
    api_key=OPENAI_API_KEY,
)
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from langchain-course!\n")
    result = agent.invoke({
        "messages": HumanMessage(content="search for 3 job postings for an ai engineer"
        "using langchain in the bay area on linkedin and list their details")
    })
    print(result)


if __name__ == "__main__":
    main()
