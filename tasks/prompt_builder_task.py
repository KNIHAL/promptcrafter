from crewai import Task
from agents.prompt_builder_agent import prompt_builder_agent

def create_generate_prompt_task(user_goal: str):
    return Task(
        description=f"Generate a clear, concise, and powerful AI prompt for this user goal: '{user_goal}'",
        expected_output="A single well-structured prompt ready to be used with an LLM like ChatGPT. No extra explanation.",
        agent=prompt_builder_agent
    )
