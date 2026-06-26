from typing import TypedDict
from langgraph.graph import StateGraph,START,END

class State(TypedDict):
    question:str
    answer:str
    summary:str
def search_node(state):

    question = state["question"].lower()

    if "india" in question:
        return {
            "answer": "New Delhi"
        }

    if "usa" in question:
        return {
            "answer": "Washington DC"
        }

    return {
        "answer": "Unknown"
    }
def summarize_node(state):
    answer=state["answer"]
    summary=f"The answer is {answer}."
    return {
        "summary":summary
    }
def route(state):
    if state["answer"]=="Unknown":
        return "retry"
    return "summarize"
def retry_node(state):
    return {
        "summary":"No answer found"
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
builder.add_node(
    "retry",
    retry_node
)
builder.add_edge(
    START,
    "search"
)
builder.add_conditional_edges(
    "search",
    route,
    {
        "retry":"retry",
        "summarize":"summarize"
    }
)
builder.add_edge(
    "summarize",
    END
)
builder.add_edge(
    "retry",
    END
)

graph=builder.compile()
result=graph.invoke(
    {
        "question":"capital of usa"
    }
)
print(result)