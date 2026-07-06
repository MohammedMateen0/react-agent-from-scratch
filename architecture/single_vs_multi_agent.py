class ResearchAgent:

    def run(self, question):
        return f"Research: {question}"


class WriterAgent:

    def run(self, research):
        return f"Final Report\n{research}"


question = "Best restaurants in Hyderabad"

print("-----Single Agent-----")

print(f"Agent: {question}")

print()

print("-----Multi Agent-----")

research = ResearchAgent().run(question)

report = WriterAgent().run(research)

print(report)