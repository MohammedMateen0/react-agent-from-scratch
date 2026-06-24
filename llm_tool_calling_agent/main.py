from agent import Agent
agent=Agent()


while True:
    query=input(
        "\n Ask: "
    )
    if query =="exit":
        break
    answer=agent.run(
        query
    )
    print("\nFinal: ",answer)