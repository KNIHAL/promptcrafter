from crewai import Crew, Process
from agents import promptGenerator, promptTester, promptEvaluator, reportGenerator
from tasks import crafting_task, evaluating_task, reporting_task, testing_task

def crew():
    return Crew(
        agents=['promptGenerator', 'promptTester', 'promptEvaluator', 'reportGenerator']
        tasks=['crafting_task', 'evaluating_task', 'reporting_task', 'testing_task']
        verbose=True,
        process=Process.sequential
    )