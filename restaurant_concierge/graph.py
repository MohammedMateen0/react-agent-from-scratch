from langgraph.graph import (
    StateGraph,
    START,
    END
)
from langgraph.checkpoint.memory import MemorySaver
from state import AgentState
from nodes import (
    search_node,
    parser_node,
    retry_node,
    answer_node,
    route,
    budget_node,
    budget_route,
    fallback_node,
    validation_node,
    validation_route
    )

builder=StateGraph(
    AgentState
)
builder.add_node(
    "parser",
    parser_node
)
builder.add_node(
    "search",
    search_node
)
builder.add_node(
    "retry",
    retry_node
)
builder.add_node(
    "answer",
    answer_node
)
builder.add_node(
    "budget",
    budget_node
)
builder.add_node(
    "fallback",
    fallback_node
)
builder.add_node(
    "validation",
    validation_node
)

builder.add_edge(
    START,
    "parser"
)
builder.add_edge(
    "parser",
    "validation"
)
builder.add_conditional_edges(
    "validation",
    validation_route,
    {
        "budget": "budget",
        "retry": "retry"
    }
)
builder.add_conditional_edges(
    "budget",
    budget_route,
    {
        "search":"search",
        "stop":END
    }
)
builder.add_conditional_edges(
    "search",
    route,
    {
        "answer":"answer",
        "retry":"retry",
        "fallback":"fallback",
        "stop":END
    }
)
builder.add_edge(
    "retry",
    "parser"
)
builder.add_edge(
    "answer",
    END
)
builder.add_edge(
    "fallback",
    END
)


memory = MemorySaver()

graph = builder.compile(
    checkpointer=memory
)


