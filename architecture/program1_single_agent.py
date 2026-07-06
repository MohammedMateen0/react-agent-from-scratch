class SingleAgent:

    def search(self, query):
        return f"Searching for: {query}"

    def calculate(self, expression):
        return eval(expression)

    def answer(self, question):

        if "capital" in question.lower():
            return self.search(question)

        elif "calculate" in question.lower():
            expression = question.replace("calculate", "")
            return self.calculate(expression)

        return "I can answer using my tools."


agent = SingleAgent()

print(agent.answer("capital of india"))
print(agent.answer("calculate 25*18"))