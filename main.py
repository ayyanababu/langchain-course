from dotenv import load_dotenv

from data import INFORMATION
from llm import create_ollama_model, create_openai_model
from prompts import create_summary_prompt

load_dotenv()


def main():
    # model = create_ollama_model()
    model = create_openai_model()
    print("Chat model initialized.")

    summary_prompt = create_summary_prompt()
    chain = summary_prompt | model
    response = chain.invoke({"information": INFORMATION})
    print(response.content)


if __name__ == "__main__":
    main()
