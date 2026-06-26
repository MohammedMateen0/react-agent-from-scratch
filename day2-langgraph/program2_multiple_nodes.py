from typing import TypedDict
from langgraph.graph import StateGraph,START,END

class State(TypedDict):
    question:str
    answer:str
    summary:str
def search_node(state):
    question=state["question"]

    if "india" in question.lower():
        return {
            "answer":"New Delhi"
        }
    return {
        "answer":"Unknown"
    }
def summarize_node(state):
    answer=state["answer"]
    summary=f"The answer is {answer}"
    return {
        "summary":summary
    }

builder=StateGraph(State)

builder.add_node(
    "search",
    search_node
)
builder.add_node(
    "summarize",
    summarize_node 
)
builder.add_edge(
    START,
    "search"
)
builder.add_edge(
    "search",
    "summarize"
)
builder.add_edge(
    "summarize",
    END
)

graph=builder.compile()
result=graph.invoke(
    {
        "question":"capital of india"
    }
)
print(result)