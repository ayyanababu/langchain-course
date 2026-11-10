import json
import os

from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain_tavily import TavilySearch
from llm import create_ollama_model, create_openai_model

def main():
    load_dotenv()

    model = create_openai_model()
    search = TavilySearch(max_results=5)
    tools = [search]
    agent = create_agent(model=model, tools=tools)

    # model = create_ollama_model()
    print("Chat model initialized.")
    result = agent.invoke({"messages": HumanMessage(content='Search for 3 top job posting in bangalore for UI Architect based on reactjs and advanced UI')})
    print('###result', result)

    # Keep this tool execution example for when Tavily is configured:
    # available_tools = {search.name: search}
    # for message in result.get("messages", []):
    #     for tool_call in getattr(message, "tool_calls", []):
    #         called_tool = available_tools.get(tool_call.get("name"))
    #         if called_tool:
    #             tool_result = called_tool.invoke(tool_call.get("args", {}))
    #             print("###tool result", tool_result)

    for message in result["messages"]:
        if getattr(message, "type", None) == "tool":
            data = json.loads(message.content) if isinstance(message.content, str) else message.content

            for number, item in enumerate(data.get("results", []), start=1):
                print(f"\n{number}. {item.get('title', 'Untitled')}")
                print(f"   URL: {item.get('url', '')}")
                print(f"   {item.get('content', '').strip()}")

        elif getattr(message, "type", None) == "ai" and not message.tool_calls:
            print("\nAgent answer:")
            print(message.content)


if __name__ == "__main__":
    main()
