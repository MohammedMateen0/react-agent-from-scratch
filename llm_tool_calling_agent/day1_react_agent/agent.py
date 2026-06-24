from tools import calculator,search

TOOLS={
    "calculator":calculator,
    "search":search
 }

class Agent:
    def __init__(self):
        self.max_steps=5
    '''def think(self,query):
        if any(
            char.isdigit()
            for char in query
        ):
            return {
                "tool":"calculator",
                "input":query
            }
        return {
            "tool":"search",
            "input":query
        }
    def run(self,query):
        for step in range(self.max_steps):
            action=self.think(query)
            tool_name=action["tool"]
            tool_input=action["input"]

            observation=TOOLS[
                tool_name
            ](tool_input)
            return observation
        return "Max steps exeeded"'''
    def run(self,query):
        context=query
        for step in range(self.max_steps):
            print(f"\n step {step+1}")
            if any(
                c.isdigit()
                for c in context
            ):
                action="calculator"
            else:
                action="search"
            print(f"Action {action}")
            observation=TOOLS[
                action
            ](context)
            print(
                "observation: ",
                observation
            )
            return observation
        return "failed"