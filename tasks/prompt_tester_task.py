from crewai import Task
from agents.prompt_tester_agent import prompt_tester_agent

def create_evaluate_prompt_task(user_goal: str):
    return Task(
        description=f"Evaluate the prompt generated for the user goal: '{user_goal}'. Assess clarity, usefulness, and suggest improvements.",
        expected_output="Bullet-point feedback covering clarity, usefulness, and suggestions for improvement.",
        agent=prompt_tester_agent
    )
