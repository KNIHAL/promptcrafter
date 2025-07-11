from crew import crew

def main():
    result =crew().kickoff(inputs={'user_input': 'write the prompt to build the agent'})

    print(result)

if __name__ == "__main__":
    main()
