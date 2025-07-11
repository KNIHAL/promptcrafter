from crewai import Task

def evaluation_task(agent):
    return Task(
        description=(
            "Evaluate each model output using criteria such as clarity, relevance, coherence, and tone. "
            "Assign a score or rank to each prompt-output pair."
        ),
        expected_output="A ranked list of prompts with scores and evaluation notes.",
        agent=agent
    )