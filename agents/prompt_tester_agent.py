from crewai import Agent
from llm.hf_llama import llama3_llm

prompt_tester=Agent(
    role="Promtpt Quality Analyst",
    goal="Analyze and improve the generated prompt for clarity, efficiency and effectiveness.",
    backstory="You,ve evaluated thousand of prompt and understand what makes a prompt effective.",
    verbose="True",
    llm="llama3_llm"
)