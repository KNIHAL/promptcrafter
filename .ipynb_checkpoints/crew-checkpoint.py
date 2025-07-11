# /home/jupyter/promptcrafter/crew.py (FINAL CORRECTED VERSION)

from crewai import Crew, Process
from agents import promptGenerator, promptTester, promptEvaluator, reportGenerator
from tasks import crafting_task, evaluation_task, reporting_task, testing_task

def crew():
    # 1. Instantiate agents ONCE and store them in variables
    agent_pg = promptGenerator()
    agent_pt = promptTester()
    agent_pe = promptEvaluator()
    agent_rg = reportGenerator()

    return Crew(
        # 2. Reference the instantiated agent variables in the 'agents' list
        agents=[
            agent_pg,  # Use the variable
            agent_pt,  # Use the variable
            agent_pe,  # Use the variable
            agent_rg   # Use the variable
        ],
        tasks=[
            # 3. Pass the *same instantiated agent variables* to your tasks
            crafting_task(agent=agent_pg),  # Pass the variable, NOT promptGenerator()
            testing_task(agent=agent_pt),   # Pass the variable, NOT promptTester()
            evaluation_task(agent=agent_pe), # Pass the variable, NOT promptEvaluator() (and added 'agent=')
            reporting_task(agent=agent_rg)  # Pass the variable, NOT reportGenerator()
        ],
        verbose=True,
        process=Process.sequential
    )