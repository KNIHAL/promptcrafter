from crew import crew

def main():
    user_input = input(" Enter you prompt or Explain what task prompt you want : ")
    result = crew().kickoff(inputs={"user_input": user_input})
    print(result)

if __name__ == "__main__":
    main()
