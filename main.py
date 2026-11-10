from dotenv import load_dotenv

from llm import create_ollama_model, create_openai_model


def main():
    load_dotenv()

    # model = create_ollama_model()
    model = create_openai_model()
    print("Chat model initialized.")


if __name__ == "__main__":
    main()
