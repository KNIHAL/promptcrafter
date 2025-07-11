from crewai import Crew, Process
from agents import promptGenerator, promptTester, promptEvaluator, reportGenerator
from tasks import crafting_task, evaluation_task, reporting_task, testing_task

def crew():
    agent_pg = promptGenerator()
    agent_pt = promptTester()
    agent_pe = promptEvaluator()
    agent_rg = reportGenerator()

    return Crew(
        agents=[
            agent_pg,  
            agent_pt,  
            agent_pe,  
            agent_rg   
        ],
        tasks=[
           
            crafting_task(agent=agent_pg),  
            testing_task(agent=agent_pt),   
            evaluation_task(agent=agent_pe), 
            reporting_task(agent=agent_rg) 
        ],
        verbose=True,
        process=Process.sequential
    )
