from crewai import Agent
from llm import llm  # assuming you have a custom LLM set up

def promptGenerator():
    return Agent(
        role="Prompt Crafter",
        goal="Generate diverse and creative prompt variations for a user-defined task",
        backstory=(
            "You are a creative language prompt crafter. You understand the structure of effective prompts "
            "and can tailor them to different tones and formats to maximize clarity and results."
        ),
        verbose=True,
        allow_delegation=False,
        memory=True,
        llm=llm
    )