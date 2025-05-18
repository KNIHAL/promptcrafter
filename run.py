from crew import run_prompt_pipeline

goal = input("Enter your goal or use-case: ")
result = run_prompt_pipeline(goal)

print("\n🧠 Final Output:\n")
print(result)
