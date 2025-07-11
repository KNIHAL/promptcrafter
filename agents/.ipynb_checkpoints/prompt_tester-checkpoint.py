from crewai import Agent
from llm import llm  

def promptTester():
    return Agent(
        role="Prompt Tester",
        goal="Apply each generated prompt to the provided input and record the model's output",
        backstory=(
            "You are responsible for testing all the generated prompts using the target model. "
            "Your job is to execute the prompt on the input and return the result."
        ),
        verbose=True,
        allow_delegation=False,
        memory=True,
        llm=llm
    )