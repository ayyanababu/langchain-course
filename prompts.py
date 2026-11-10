from langchain_core.prompts import PromptTemplate

SUMMARY_TEMPLATE = """
given the information {information} about a person i want to create:
1. A short summary
2. two interseting facts about them
"""


def create_summary_prompt():
    return PromptTemplate(
        input_variables=["information"],
        template=SUMMARY_TEMPLATE,
    )
