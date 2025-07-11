from crewai import Task

def reporting_task(agent):
    return Task(
        description=(
            "Summarize the evaluation results and provide the user with the best-performing prompt, "
            "along with notes and examples explaining why it is the most effective. "
            "Write the final result to the 'example/prompt.txt' file."
        ),
        expected_output="The most effective prompt line written into 'example/prompt.txt' file.",
        agent=agent
    )