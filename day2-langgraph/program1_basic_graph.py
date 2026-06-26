from typing import TypedDict
from langgraph.graph import StateGraph,START,END


class State(TypedDict):
    question:str
    answer:str

def search_node(state):
    question=state["question"]
    if "india" in question.lower():
        return {
            "answer":"New Delhi"
        }
    return {
        "answer":"unknown"
    }

builder=StateGraph(
    State
)
builder.add_node(
    "search",
    search_node
)
builder.add_edge(
    START,
    "search"
)

builder.add_edge(
    "search",
    END
)
graph=builder.compile()

result=graph.invoke(
    {
        "question":
        "capital of india"
    }
)
print(result)