from typing import Annotated,TypedDict
from langgraph.graph.message import add_messages
from langchain_core.messages import HumanMessage,AIMessage
from langgraph.graph import (
    StateGraph,
    START,
    END
)

class State(TypedDict):
    messages:Annotated[
        list,
        add_messages
    ]
def user_node(state):
    return {
        "messages":[
            HumanMessage(
                content="Hello"
            )
        ]
    }
def ai_node(state):
    return {
        "messages":[
            AIMessage(
                content="Hi! How can I help?"
            )
        ]
    }

builder=StateGraph(State)

builder.add_node(
    "user",
    user_node
)
builder.add_node(
    "assistant",
    ai_node
)
builder.add_edge(
    START,
    "user"
)
builder.add_edge(
    "user",
    "assistant"
)
builder.add_edge(
    "assistant",
    END
)
graph=builder.compile()
result=graph.invoke(
    {
        "messages":[]
    }
)
print(result)