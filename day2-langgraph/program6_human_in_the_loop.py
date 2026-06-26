from typing import TypedDict
from langgraph.graph import StateGraph,START,END
from langgraph.checkpoint.memory import MemorySaver

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
    return {
        "summary":f"The answer is {answer}."
    }

builder =StateGraph(State)

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

memory=MemorySaver()

graph=builder.compile(
    checkpointer=memory,
    interrupt_before=["summarize"]
)

config={
    "configurable":{
        "thread_id":"sessioni"
    }
}
graph.invoke(
    {
        "question":"capital of india"
    },
    config=config
)
snapshot=graph.get_state(config)

print(snapshot.values)
print(snapshot.next)