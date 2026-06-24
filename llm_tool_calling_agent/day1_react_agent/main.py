from agent import Agent

agent = Agent()

while True:

    question = input(
        "\nAsk: "
    )

    if question.lower() == "exit":
        break

    result = agent.run(
        question
    )

    print(
        "\nAnswer:",
        result
    )