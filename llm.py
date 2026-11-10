import os

from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI


def create_ollama_model():
    return ChatOllama(
        model="gemma:2b",
        temperature=0,
    )


def create_openai_model():
    return ChatOpenAI(
        model="gpt-4o-mini",
        api_key=os.environ.get("OPENAI_API_KEY"),
        temperature=0,
    )
