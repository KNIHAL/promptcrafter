from crewai import Agent
from llm.local_llm import llama3_llm # If you don't have api key, use this llm.
# from llm.cloud_llm import llm       "If you have api key, use this."

def promptGenerator():
    return Agent(
        role="Prompt Tester",
        goal="Apply each generated prompt to the provided input and record the model's output",
        backstory=(
            "You are responsible for testing all the generated prompts using the target model. "
            "Your job is to execute the prompt on the input and return the result."
            ),
        verbose=True,
        allow_delegation=False,
        llm=llama3_llm # or llm=llm

    )