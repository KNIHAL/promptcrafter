from crewai import Agent
from crewai_tools import FileWriterTool
from llm import llm    

file_Write=FileWriterTool()

def reportGenerator():
    return Agent(
        role="Report Generator",
        goal="Compile the evaluation results and present the best prompt with reasoning",
        backstory=(
            "You are responsible for summarizing findings from the prompt evaluation. "
            "You clearly present the top performing prompt with reasoning and clarity."
        ),
        verbose=True,
        allow_delegation=False,
        memory=True,
        llm=llm
    )