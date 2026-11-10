import json
import os
from typing import List

from pydantic import BaseModel, Field

from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain_tavily import TavilySearch
from llm import create_ollama_model, create_openai_model

class Source(BaseModel):
    """
        Scheme for a source used by the agent
    """
    url:str = Field(description="The URL of the source")

class AgentResponse(BaseModel):
    """
        Schema for agent response with answer and soruces
    """
    answer:str = Field(description="this is agents answer to the query")
    sources: List[Source] = Field(default_factory=list, description="List of sources used to generate the answer")

def main():
    load_dotenv()

    model = create_openai_model()
    search = TavilySearch(max_results=5)
    tools = [search]
    agent = create_agent(model=model, tools=tools, response_format=AgentResponse)

    # model = create_ollama_model()
    print("Chat model initialized.")
    result = agent.invoke({"messages": HumanMessage(content='Search for 3 top job posting in bangalore for UI Architect based on reactjs and advanced UI')})
    structured_response = result["structured_response"]
    print("\n### Answer")
    print(structured_response.answer)
    print("\n### Sources")
    for source in structured_response.sources:
        print(f"- {source.url}")

    # Keep this tool execution example for when Tavily is configured:
    # available_tools = {search.name: search}
    # for message in result.get("messages", []):
    #     for tool_call in getattr(message, "tool_calls", []):
    #         called_tool = available_tools.get(tool_call.get("name"))
    #         if called_tool:
    #             tool_result = called_tool.invoke(tool_call.get("args", {}))
    #             print("###tool result", tool_result)

    # for message in result["messages"]:
    #     if getattr(message, "type", None) == "tool":
    #         data = json.loads(message.content) if isinstance(message.content, str) else message.content

    #         for number, item in enumerate(data.get("results", []), start=1):
    #             print(f"\n{number}. {item.get('title', 'Untitled')}")
    #             print(f"   URL: {item.get('url', '')}")
    #             print(f"   {item.get('content', '').strip()}")

    #     elif getattr(message, "type", None) == "ai" and not message.tool_calls:
    #         print("\nAgent answer:")
    #         print(message.content)


if __name__ == "__main__":
    main()
