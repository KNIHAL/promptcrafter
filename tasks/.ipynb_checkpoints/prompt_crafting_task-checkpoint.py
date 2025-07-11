from crewai import Task

def crafting_task(agent):
    return Task(
        description=(
            "Generate 5 to 10 unique prompt variations for the user-provided task: '{user_input}'"
            "Each variation should explore different tones (e.g., formal, casual), "
            "formats (instructional, question-based), and styles (step-by-step, summary)."
        ),
        expected_output="A list of at least 5 well-structured prompt strings.",
        agent=agent
    )
