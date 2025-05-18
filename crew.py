from crewai import Crew
from agents.prompt_builder_agent import prompt_builder
from agents.prompt_tester_agent import prompt_tester

from tasks.prompt_builder_task import create_generate_prompt_task
from tasks.prompt_tester_task import create_evaluate_prompt_task

def run_prompt_pipeline(user_goal: str):
    generate_task = create_generate_prompt_task(user_goal)
    evaluate_task = create_evaluate_prompt_task(user_goal)

    crew = Crew(
        agents=[prompt_builder, prompt_tester],
        tasks=[generate_task, evaluate_task],
        verbose=True
    )

    result = crew.kickoff()
    return result
