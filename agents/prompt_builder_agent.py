from crewai import Agent
from llm.hf_llama import llama3_llm

prompt_builder = Agent(
    role="Expert Prompting Engineer",
    goal="write a perfect prompt based on user input without bugs",
    backstory="You have a 10 years of experince writing effective prompt. You believe prompting is the new coding"
    verbose=True,
    llm="llama3_llm"
)