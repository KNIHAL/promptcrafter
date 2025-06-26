from crewai import Agent
from crewai_tools import FileWriteTool
from llm.local_llm import llama3_llm # If you don't have api key, use this llm.
# from llm.cloud_llm import llm       "If you have api key, use this."

file_Write=FileWriteTool()

def reportGenerator():
    return Agent(
        role="Report Writer",
        goal="Summarize the performance of all prompt variants and suggest the best one",
        backstory=(
        "You compile the results of the prompt tuning process, summarize findings, and recommend "
        "the best-performing prompt to the user in a clear, structured format."
        ),
    verbose=True,
    allow_delegation=False,
    tools=[file_Write],
    llm=llama3_llm # or llm=llm
    )
